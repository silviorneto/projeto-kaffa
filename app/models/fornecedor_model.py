from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship


@dataclass
class FornecedorModel(db.Model):
    id: int
    nome_fantasia: str
    cnpj: str
    telefone: str
    lista_de_produtos: list

    __tablename__ = 'fornecedor'

    id = Column(Integer, primary_key=True)
    nome_fantasia = Column(String(200), nullable=False)
    cnpj = Column(String(18), nullable=False, unique=True)
    telefone = Column(String(12), nullable=False, unique=True)

    lista_de_produtos = relationship(
        'ProdutoModel', backref=backref('fornecedor_list'), secondary='fornecedor_produto'
    )
