import datetime
import sqlalchemy
from session_db import SqlAlchemyBase


class Files(SqlAlchemyBase):
    __tablename__ = 'all_files'

    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = sqlalchemy.Column(
        sqlalchemy.String,
        nullable=False
    )
    file_type = sqlalchemy.Column(
        sqlalchemy.String,
        nullable=True
    )
    size = sqlalchemy.Column(
        sqlalchemy.Integer,
        nullable=True
    )
    full_path = sqlalchemy.Column(
        sqlalchemy.String,
        nullable=False
    )
    created_date = sqlalchemy.Column(
        sqlalchemy.DateTime,
        default=datetime.datetime.utcnow
    )

    annual_fee = sqlalchemy.Column(
        sqlalchemy.Integer,
        nullable=True
    )
    credit_score = sqlalchemy.Column(
        sqlalchemy.Integer,
        nullable=True
    )
