import os
from models import session_db
from datetime import datetime
from models.session_db import create_db, Session
from models.file_model import Files


class DbCreator:
    def __init__(self) -> None:
        self.main_path = "/home/avrelian/Desktop/resumes&todo_tasks"

    def get_all_files(self, path):
        dirs = os.listdir(path)
        all_files = list()
        for entry in dirs:
            full_path = os.path.join(path, entry)
            if os.path.isdir(full_path):
                all_files += self.get_all_files(full_path)
            else:
                size = os.path.getsize(full_path)
                create_time = datetime.fromtimestamp(
                    os.path.getctime(full_path)).isoformat()
                change_time = datetime.fromtimestamp(
                    os.path.getmtime(full_path)).isoformat()

                item = (full_path, size, create_time, change_time)
                all_files.append(item)
        return all_files

    def fill_db(self, session: Session):
        all_files = self.get_all_files(self.main_path)
        for file in all_files:
            file_name = file[0].split('/')[-1]
            file_type = file_name.split('.')[-1]
            full_path, size, created_date, modified_date = file[0], file[1], file[2], file[3]

            sql_row = Files(
                name=file_name, file_type=file_type, full_path=full_path,
                size=size, created_date=created_date, modified_date=modified_date,
                description=''
            )
            session.add(sql_row)
        session.commit()

    def create_database(self):
        create_db()


db_cr = DbCreator()
db_cr.fill_db(Session())
