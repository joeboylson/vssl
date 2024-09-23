import json
from flask import Blueprint
from flask import request
from utils.limiter import app_limiter
from utils.supabase import supabase
from utils.environment import is_production


authentication_blueprint = Blueprint("authentication_blueprint", __name__)


# Use method to create a response for all routes
def make_authentication_blueprint_response(success, message, user):
    return {"success": success, "message": message, "user": user}


@authentication_blueprint.route("/send-otp-token")
@app_limiter.exempt
def send_otp_token():
    try:
        email = request.args.get("email", default=None)

        if email is not None:
            supabase.auth.sign_in_with_otp({"email": email})

            return make_authentication_blueprint_response(
                success=True, message="Success", user=None
            )

    except Exception as e:
        return make_authentication_blueprint_response(
            success=False, message=str(e), user=None
        )


@authentication_blueprint.route("/verify-otp-token")
@app_limiter.exempt
def verify_otp_token():

    try:
        email = request.args.get("email", default=None)
        token = request.args.get("token", default=None)

        if token is not None and email is not None:
            supabase.auth.verify_otp({"email": email, "token": token, "type": "email"})

            # if not is_production():
            #     with open("__REFRESH_TOKEN", "a") as f:
            #         session = supabase.auth.get_session()
            #         f.write(session.refresh_token)

            return {"success": True}

        else:
            return make_authentication_blueprint_response(
                success=False, message="Invalid arguments", user=None
            )
    except Exception as e:
        return make_authentication_blueprint_response(
            success=False, message=str(e), user=None
        )


@authentication_blueprint.route("/is-authenticated")
@app_limiter.exempt
def is_authenticated():
    try:
        # session = supabase.auth.get_session()

        # # if not is_production() and session is None:
        # #     with open("__REFRESH_TOKEN", "r") as f:
        # #         refresh_token = f.read()
        # #         session = supabase.auth.refresh_session(refresh_token)

        # if session is None:
        #     return make_authentication_blueprint_response(
        #         success=False, message="No authenticated user", user=None
        #     )

        # user = json.loads(session.user.model_dump_json())

        return make_authentication_blueprint_response(
            success=True, message="Success", user={"email": "Demo User"}
        )

    except Exception as e:
        return make_authentication_blueprint_response(
            success=False, message=str(e), user=None
        )
