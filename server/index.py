import os
import tempfile
import json

from flask import Flask, send_file, request
from stl.generate_model import generate_stl_model, generate_fallback_cube
from supabase import create_client
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


STATIC_FOLDER_NAME = "dist"
IS_PRODUCTION = os.environ.get("MODE") == "production"
PORT = os.environ.get("SERVER_PORT")

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

app = Flask(__name__, static_url_path="", static_folder=STATIC_FOLDER_NAME)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["1 per hour"],
    storage_uri="memory://",
)


@app.route("/send-otp-token")
@limiter.exempt
def send_otp_token():
    try:
        email = request.args.get("email", default=None)

        if email is not None:
            response = supabase.auth.sign_in_with_otp(
                {
                    "email": email,
                }
            )

            return {"success": True, "message": "OK"}
    except Exception as e:
        return {"success": False, "message": str(e)}


@app.route("/verify-otp-token")
@limiter.exempt
def verify_otp_token():
    try:
        email = request.args.get("email", default=None)
        token = request.args.get("token", default=None)

        if token is not None and email is not None:
            supabase.auth.verify_otp({"email": email, "token": token, "type": "email"})

            if not IS_PRODUCTION:
                with open("__REFRESH_TOKEN", "a") as f:
                    session = supabase.auth.get_session()
                    f.write(session.refresh_token)

            return {"success": True}
    except:
        return {"success": False}


@app.route("/is-authenticated")
@limiter.exempt
def is_authenticated():
    try:
        session = supabase.auth.get_session()

        if not IS_PRODUCTION and session is None:
            with open("__REFRESH_TOKEN", "r") as f:
                refresh_token = f.read()
                session = supabase.auth.refresh_session(refresh_token)

        if session is None:
            return {"user": None, "message": "Session is empty"}

        user = json.loads(session.user.model_dump_json())
        return {"user": user, "message": "OK"}
    except Exception as e:
        return {"user": None, "message": str(e)}


@app.route("/generate-cube-stl")
@limiter.limit("1 per day")
def generate_cube_stl():

    try:

        # retrieve values from URL params
        slot_size_x = int(request.args.get("ssx", default=20))
        slot_size_y = int(request.args.get("ssy", default=20))
        slot_size_z = int(request.args.get("ssz", default=20))
        number_of_slots_x = int(request.args.get("nx", default=2))
        number_of_slots_y = int(request.args.get("ny", default=2))
        wall_thickness = int(request.args.get("wt", default=1))
        wall_inset = int(request.args.get("wi", default=0))

        # generate STL
        stl = generate_stl_model(
            slot_size_x,
            slot_size_y,
            slot_size_z,
            number_of_slots_x,
            number_of_slots_y,
            wall_thickness,
            wall_inset,
        )

        # create temporary file
        tmp = tempfile.NamedTemporaryFile(suffix=".stl")

        # save STL to temporary gile
        stl.save_as_stl(tmp.name)
        tmp.seek(0)

        # return temporary file
        return send_file(tmp, mimetype="model/stl")

    except:

        # generate STL
        stl = generate_fallback_cube()

        # create temporary file
        tmp = tempfile.NamedTemporaryFile(suffix=".stl")

        # save STL to temporary gile
        stl.save_as_stl(tmp.name)
        tmp.seek(0)

        # return temporary file
        return send_file(tmp, mimetype="model/stl")


if __name__ == "__main__":
    if IS_PRODUCTION:
        from waitress import serve

        serve(app, host="0.0.0.0", port=PORT)
    else:
        print(f">>> {PORT}")
        app.run(debug=True, port=PORT)
