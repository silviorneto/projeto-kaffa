from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

from app.configs.database import db
from dataclasses import dataclass

@dataclass
class GarcomModel(db.Model):
    id: int
    nome: str
    cpf: str
    lista_contas: list

    __tablename__ = "garcons"

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id"), nullable=False, unique=True)

    lista_contas = relationship("ContaModel", backref=backref("garcom"))
