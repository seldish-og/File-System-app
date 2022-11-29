import os
from datetime import datetime


def get_all_files(path):
    dirs = os.listdir(path)
    all_files = list()
    for entry in dirs:
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            all_files += get_all_files(full_path)
        else:
            size = os.path.getsize(full_path)
            create_time = datetime.fromtimestamp(
                os.path.getctime(full_path)).isoformat()
            change_time = datetime.fromtimestamp(
                os.path.getmtime(full_path)).isoformat()

            item = (full_path, size, create_time, change_time)
            all_files.append(item)
    return all_files


main_path = "/home/avrelian/Desktop/resumes&todo_tasks"

listOfFiles = get_all_files(path=main_path)
print(listOfFiles)
