import tempfile
from flask import Blueprint, request, send_file
from utils.args import is_true
from utils.limiter import app_limiter
from stl.generate_model import generate_stl_model, generate_fallback_cube


stl_blueprint = Blueprint("stl_blueprint", __name__)


@stl_blueprint.route("/generate-stl")
@app_limiter.limit("1000 per day")
def generate_stl():

    def generate_stl():
        try:
            # TODO: use request query instead of request args...this is getting
            # slightly out of hand

            # retrieve values from URL params
            # NOTE: these must be in a specific order
            model_args = [
                request.args.get("ssx", default=20, type=int),
                request.args.get("ssy", default=20, type=int),
                request.args.get("ssz", default=20, type=int),
                request.args.get("nx", default=2, type=int),
                request.args.get("ny", default=2, type=int),
                request.args.get("wt", default=1, type=int),
                request.args.get("wi", default=0, type=int),
                request.args.get("wli", default=True, type=is_true),
                request.args.get("wpt", default=True, type=is_true),
            ]

            print(model_args)

            # generate STL
            return generate_stl_model(*model_args)
        except:

            # generate STL
            return generate_fallback_cube()

    # generate model
    model = generate_stl()

    # create temporary file
    tmp = tempfile.NamedTemporaryFile(suffix=".stl")

    # save STL to temporary file
    model.save_as_stl(tmp.name)
    tmp.seek(0)

    model.save_as_scad()

    # return temporary file
    return send_file(tmp, mimetype="model/stl")
