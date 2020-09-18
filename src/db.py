from sqlalchemy import create_engine, dialects, MetaData, Table
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import Config

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
db_session = scoped_session(sessionmaker(bind=engine, autoflush=False))

Base = declarative_base()
Base.query = db_session.query_property()

metadata = MetaData()


def init_db():
  Base.metadata.create_all(bind=engine)
