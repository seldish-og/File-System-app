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
            return "No such file", 404

    def upload_file(self, file_name, request):
        try:
            file_path = f"{self.upload_dir}{file_name}"
            with open(file_path, "wb") as file:
                file.write(request.data)
        except Exception:
            return "Can't upload file", 404
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
            return "Can't add file to database", 404

    def delete_file(self, file_name):
        file = self.session.query(Files).filter(
            Files.name == file_name).first()
        self.session.delete(file)
        self.session.commit()
        os.remove(file.full_path)

        return "File deleted", 200

    def get_file_bypath(self, path):
        files = self.session.query(Files).filter(
            Files.full_path.like(f'{path}%'))
        json_list = [row.serialize for row in files.all()]

        if not json_list:
            return f"NO FILES STARTS WITH <<{path}>> WERE FOUND "
        return json_list

    def get_files_folder(self, file_name):
        file = self.session.query(Files).filter(Files.name == file_name)
        try:
            print("hey")
            return file.first().full_path
        except AttributeError as ex:
            return "No such file", 404
