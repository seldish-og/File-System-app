from models import file_model, session_db
from flask import Blueprint, abort, jsonify, request
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


@files_page.route("/upload_file/<file_name>", methods=["POST"])
def upload_file(file_name):
    """Upload a file."""
    if "/" in file_name:
        abort(400, "no subdirectories allowed")
    response = files_controller.upload_file(file_name, request)

    return "file uploaded", 201


@files_page.route("/delete_file/<file_name>", methods=['DELETE'])
def delete_file(file_name):
    response = files_controller.delete_file(file_name)
    return "response"
