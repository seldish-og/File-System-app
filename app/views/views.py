from flask import Blueprint, jsonify, render_template, abort
from models import files, session_db

files_page = Blueprint('files_page', __name__)

session = session_db.Session()


@files_page.route("/")
def hello():
    return "<h1>SERVER IS UP</h1>"


@files_page.route("/get_all_files")
def get_all_files():
    resp = session.query(files.Files)

    return jsonify(json_list=[row.serialize for row in resp.all()])


# @app.route("/files/<filename>", methods=["POST"])
# def post_file(filename):
#     """Upload a file."""
#     if "/" in filename:
#         abort(400, "no subdirectories allowed")

#     with open(os.path.join(UPLOAD_DIRECTORY, filename), "wb") as fp:
#         fp.write(request.data)

#     return "file uploaded", 201
