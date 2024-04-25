from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship

from db import Base


class Pair(Base):
    __tablename__ = f'pairs_'

    id = Column(Integer, primary_key=True)
    pair_address = Column(String(50))
    pair_abi = Column(Text)
    pair_number = Column(Integer)

    profile = relationship('Token', backref='pairs', uselist=False)


    def __repr__(self) -> str:
        return f"<pair {self.id}>"


class Token(Base):
    __tablename__ = f'token_'

    id = Column(Integer, primary_key=True)
    token_name = Column(String(50))
    token_address = Column(String(50))
    token_position = Column(Integer)
    
    pair_id = Column(Integer, ForeignKey(f'pairs_.id'))
