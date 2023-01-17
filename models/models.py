from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Float, INTEGER, String, TIMESTAMP, text

Base = declarative_base()


class Operacao(Base):
    __tablename__ = "operacoes"
    id = Column(INTEGER, primary_key=True)
    name = Column(String(20), nullable=False)
    resultado = Column(Float)
    created_at = Column(TIMESTAMP, nullable=False,
                        server_default=text("CURRENT_TIMESTAMP"))
