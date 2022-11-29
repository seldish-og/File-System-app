from files import Files
import session_db


def add_user_db():
    sess = session_db.create_session()
    file = Files()
    file.name = "test"
    file.file_type = ".txt"
    file.full_path = "venv/bin"

    file.size = 1234
    sess.add(file)
    sess.commit()


add_user_db()
