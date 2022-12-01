from views import views
from flask import Flask
from flask import Blueprint, render_template, abort

app = Flask(__name__)

app.register_blueprint(views.files_page)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
