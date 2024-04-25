from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base


engine = create_engine("postgresql+psycopg2://postgres:postgres_password@db:5432/postgres")
Session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = Session.query_property()
