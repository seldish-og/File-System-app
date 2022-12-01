import os
from models import session_db
from models.file_model import Files


class FileController:
    def __init__(self) -> None:
        self.session = session_db.Session()
        self.upload_dir = "../uploaded_files/"

    def get_all_files(self):
        all_files = self.session.query(Files)
        json_list = [row.serialize for row in all_files.all()]

        return json_list

    def get_file(self, file_name):
        file = self.session.query(Files).filter(Files.name == file_name)
        try:
            return file.first().serialize
        except AttributeError as ex:
            return "No such file"

    def upload_file(self, file_name, request):
        with open(f"{self.upload_dir}{file_name}", "wb") as file:
            file.write(request.data)
