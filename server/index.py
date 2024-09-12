import os
from flask import Flask, send_file, redirect
from io import BytesIO
import tempfile


STATIC_FOLDER_NAME = "dist"
IS_PRODUCTION = os.environ.get("MODE") == "production"
PORT = os.environ.get("SERVER_PORT")

app = Flask(__name__, static_url_path="", static_folder=STATIC_FOLDER_NAME)


@app.route("/")
def index():
    if IS_PRODUCTION:
        return send_file(f"{STATIC_FOLDER_NAME}/index.html")
    return redirect("http://localhost:3000")


@app.route("/generate-cube-stl")
def generate_cube_stl():

    from solid2 import cube

    tmp = tempfile.NamedTemporaryFile(suffix=".stl")

    stl = cube(10, center=True)
    stl.save_as_stl(tmp.name)

    tmp.seek(0)

    return send_file(tmp, mimetype="model/stl")


if __name__ == "__main__":
    if IS_PRODUCTION:
        from waitress import serve

        serve(app, host="0.0.0.0", port=PORT)
    else:
        print(f">>> {PORT}")
        app.run(debug=True, port=PORT)
