import os
from dotenv import load_dotenv
import sqlalchemy
import sqlalchemy.ext.declarative as dec
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session

load_dotenv()

CONNECT_URL = sqlalchemy.URL.create(
    "postgresql+psycopg2",
    username=os.environ.get('POSTGRES_USER'),
    password=os.environ.get('POSTGRES_PASSWORD'),  # plain (unescaped) text
    host=os.environ.get('POSTGRES_HOST'),
    database=os.environ.get('POSTGRES_DB'),
    port=os.environ.get('POSTGRES_PORT')
)

SqlAlchemyBase = dec.declarative_base()
__factory = None


def global_init(db_file):
    global __factory

    if __factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("Db not found")

    print(f"Connecting to {CONNECT_URL}")

    engine = sqlalchemy.create_engine(CONNECT_URL, echo=False)
    __factory = orm.sessionmaker(bind=engine)

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    return __factory()
