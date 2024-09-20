from flask import Blueprint, send_file, redirect
from utils.environment import is_production
from utils.limiter import app_limiter

STATIC_FOLDER_NAME = "dist"
static_blueprint = Blueprint("static_blueprint", __name__)


@static_blueprint.route("/")
@app_limiter.exempt
def index():
    if is_production():
        return send_file(f"{STATIC_FOLDER_NAME}/index.html")
    return redirect("http://localhost:3000")
