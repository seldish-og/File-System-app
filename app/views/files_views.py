from models import file_model, session_db
from flask import Blueprint, jsonify
from controllers import files_controllers

files_page = Blueprint('files_page', __name__)

files_controller = files_controllers.FileController()


@files_page.route("/", methods=['GET'])
def hello():
    return "<h1>SERVER IS UP</h1>"


@files_page.route("/get_all_files", methods=['GET'])
def get_all_files():
    response = files_controller.get_all_files()

    return jsonify(response)


@files_page.route("/get_file/<file_name>", methods=['GET'])
def get_file(file_name):
    response = files_controller.get_file(file_name)

    return jsonify(response)


# @app.route("/files/<filename>", methods=["POST"])
# def post_file(filename):
#     """Upload a file."""
#     if "/" in filename:
#         abort(400, "no subdirectories allowed")
#     with open(os.path.join(UPLOAD_DIRECTORY, filename), "wb") as fp:
#         fp.write(request.data)
#     return "file uploaded", 201
