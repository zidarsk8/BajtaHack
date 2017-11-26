from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Sensor(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    url = Column(String(250), nullable=True)
    mode = Column(String(250), nullable=True)
    value = Column(String(250), nullable=True)


def init_db(db):
    engine = db.get_engine()
    Base.metadata.create_all(engine)
    db.session.commit()
