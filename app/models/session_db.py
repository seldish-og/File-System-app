import os
from dotenv import load_dotenv
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from .file_model import Files, SqlAlchemyBase
from .fill_db import DbFiller


load_dotenv()

db_name = os.environ.get('POSTGRES_DB')
db_user = os.environ.get('POSTGRES_USER')
db_password = os.environ.get('POSTGRES_PASSWORD')
db_host = os.environ.get('POSTGRES_HOST')
db_port = os.environ.get('POSTGRES_PORT')
main_path = os.environ.get("MAIN_PATH")


conn_str = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = sqlalchemy.create_engine(conn_str, echo=False)
Session = sessionmaker(bind=engine)

if not sqlalchemy.inspect(engine).has_table("all_files"):
    SqlAlchemyBase.metadata.create_all(bind=engine)
    db_filler = DbFiller(main_path)
    db_filler.fill_db(session=Session())
    print("DATABASE CREATED AND MIGRATED")
