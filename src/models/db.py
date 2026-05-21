from sqlalchemy import create_engine
from sqlalchemy.orm import MappedAsDataclass, DeclarativeBase, sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

class Base(MappedAsDataclass, DeclarativeBase):
    pass

engine = create_engine(url=os.getenv('DB_URL'))
session_maker = sessionmaker(bind=engine)

def Session():
    session = session_maker()
    try:
        yield session
    except:
        session.rollback()
        raise
    finally:
        session.close()
