from decimal import Decimal
from sqlalchemy import Column, String, Integer, DECIMAL
from dataclasses import dataclass
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.expression import false
from sqlalchemy.sql.sqltypes import Numeric

from app.configs.database import db

@dataclass
class ProdutoModel(db.Model):
    id: int
    nome: str
    descricao: str

    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False, unique=True)
    descricao = Column(String(200), nullable=False)
    preco = Column(DECIMAL, nullable=False)
