import os
from dotenv import load_dotenv
import sqlalchemy
import sqlalchemy.ext.declarative as dec
from sqlalchemy.orm import sessionmaker

load_dotenv()

db_name = os.environ.get('POSTGRES_DB')
db_user = os.environ.get('POSTGRES_USER')
db_password = os.environ.get('POSTGRES_PASSWORD')
db_host = os.environ.get('POSTGRES_HOST')
db_port = os.environ.get('POSTGRES_PORT')

conn_str = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = sqlalchemy.create_engine(conn_str, echo=True)
Session = sessionmaker(bind=engine)

SqlAlchemyBase = dec.declarative_base()


def create_db():
    SqlAlchemyBase.metadata.create_all(bind=engine)
