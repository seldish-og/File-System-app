from flask import Blueprint, Flask, abort, render_template
from views import files_views

app = Flask(__name__)

app.register_blueprint(files_views.files_page)


# if __name__ == "__main__":
#     app.run(debug=True, port=8000)
