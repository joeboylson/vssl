import os
from flask import Flask, redirect
from utils.limiter import app_limiter
from utils.environment import is_production
from routes.authentication import authentication_blueprint
from routes.stl import stl_blueprint
from routes.static import static_blueprint, STATIC_FOLDER_NAME


PORT = os.environ.get("SERVER_PORT")


def start_app():

    app = Flask(__name__, static_url_path="", static_folder=STATIC_FOLDER_NAME)

    @app.errorhandler(404)
    def page_not_found(e):
        return redirect("/")

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

    # from stl.generate_model import generate_stl_model
    # from random import randrange

    # model_args = [
    #     randrange(10, 50),  # ---slot_size_x,
    #     randrange(10, 50),  # ---slot_size_y,
    #     randrange(10, 50),  # ---slot_size_z,
    #     randrange(1, 10),  # ---number_of_slots_x,
    #     randrange(1, 10),  # ---number_of_slots_y,
    #     randrange(1, 5),  # ---wall_thickness,
    #     randrange(1, 10),  # ---wall_inset,
    #     False,  # ---with_lid_inset,
    #     False,  # ---with_pull_tab,
    # ]

    # model_args = [
    #     10,  # ---slot_size_x,
    #     10,  # ---slot_size_y,
    #     2,  # ---slot_size_z,
    #     3,  # ---number_of_slots_x,
    #     3,  # ---number_of_slots_y,
    #     1,  # ---wall_thickness,
    #     0,  # ---wall_inset,
    #     False,  # ---with_lid_inset,
    #     False,  # ---with_pull_tab,
    # ]

    # # generate STL
    # model = generate_stl_model(*model_args)
    # model.render().save_as_scad()
