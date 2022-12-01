import datetime
import sqlalchemy
import sqlalchemy.ext.declarative as dec

SqlAlchemyBase = dec.declarative_base()


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
        nullable=False
    )
    size = sqlalchemy.Column(
        sqlalchemy.Integer,
        nullable=False
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
        sqlalchemy.Text
    )

    def __init__(self, name, file_type, size, full_path, created_date, modified_date, description):
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

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            "id": self.id,
            "name": self.name,
            "file_type": self.file_type,
            "size": self.size,
            "full_path": self.full_path,
            "created_date": self.created_date,
            "modified_date": self.modified_date,
            "description": self.description
        }
