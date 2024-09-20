import os
from flask import Flask
from utils.limiter import app_limiter
from utils.environment import is_production
from routes.authentication import authentication_blueprint
from routes.stl import stl_blueprint
from routes.static import static_blueprint, STATIC_FOLDER_NAME


PORT = os.environ.get("SERVER_PORT")


def start_app():

    app = Flask(__name__, static_url_path="", static_folder=STATIC_FOLDER_NAME)

    app_limiter.init_app(app)
    app.register_blueprint(authentication_blueprint)
    app.register_blueprint(stl_blueprint)
    app.register_blueprint(static_blueprint)

    if is_production():
        from waitress import serve

        serve(app, host="0.0.0.0", port=PORT)
    else:
        print(f">>> {PORT}")
        app.run(debug=True, port=PORT)


if __name__ == "__main__":
    start_app()
