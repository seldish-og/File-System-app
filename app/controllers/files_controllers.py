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
        try:
            file_path = f"{self.upload_dir}{file_name}"
            with open(file_path, "wb") as file:
                file.write(request.data)
        except Exception:
            return "Can't upload file"
        try:
            new_row = Files(
                name=file_name,
                file_type=file_name.split('.')[-1],
                full_path=file_path,
                size=os.path.getsize(file_path),
                created_date=os.path.getctime(file_path),
                modified_date=os.path.getmtime(file_path),
                description=''
            )
            self.session.add(new_row)
            self.session.commit()
        except Exception:
            return "Can't add file to database"

    def delete_file(self, file_name):
        file = self.session.query(Files).filter(
            Files.name == file_name).first()
        self.session.delete(file)
        self.session.commit()
        os.remove(file.full_path)
