import datetime
import sqlalchemy
from .session_db import SqlAlchemyBase


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
    modified_date = sqlalchemy.Column(
        sqlalchemy.DateTime,
        default=datetime.datetime.utcnow
    )
    description = sqlalchemy.Column(
        sqlalchemy.Text,
        nullable=True
    )

    def __init__(self, id, name, file_type, size, full_path, created_date, modified_date, description):
        self.id = id
        self.name = name
        self.file_type = file_type
        self.size = size
        self.full_path = full_path
        self.created_date = created_date
        self.modified_date = modified_date
        self.description = description

    def __repr__(self) -> str:
        return f'''
        {self.id} = id, 
        {self.name} = name, 
        {self.file_type} = file_type, 
        {self.size} = size, 
        {self.full_path} = full_path, 
        {self.created_date} = created_date, 
        {self.modified_date} = modified_date, 
        {self.description} = description.
        '''
