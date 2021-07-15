from dataclasses import dataclass
from datetime import date

import ipdb
from app.configs.database import db
from sqlalchemy import Column, Date, Integer, and_
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.schema import ForeignKey

from .conta_produto import ContaProdutoModel


@dataclass
class ContaModel(db.Model):
    id: int
    data: date
    id_caixa: int
    id_garcom: int
    id_mesa: int
    id_forma_pagamento: int
    lista_produtos: list

    __tablename__ = "contas"

    id = Column(Integer, primary_key=True)
    data = Column(Date, nullable=False)
    id_caixa = Column(Integer, ForeignKey("caixas.id"), nullable=False)
    id_garcom = Column(Integer, ForeignKey("garcons.id"), nullable=False)
    id_mesa = Column(Integer, ForeignKey("mesas.id"), nullable=False)
    id_forma_pagamento = Column(
        Integer, ForeignKey("forma_pagamento.id"), nullable=False
    )

    lista_produtos = relationship(
        "ProdutoModel", secondary="conta_produto", backref=backref("contas_list")
    )

    garcom_da_conta_model = relationship(
        'GarcomModel', backref=backref('contas_virtual', uselist=False)
    )

    def update_value(self):
        bill_value = 0

        for produto in self.lista_produtos:
            conta_produto: ContaProdutoModel = ContaProdutoModel.query.filter(
                and_(
                    ContaProdutoModel.id_produto == produto.id,
                    ContaProdutoModel.id_conta == self.id,
                )
            ).first()
            bill_value = bill_value + (produto.preco * conta_produto.quantity)

        return bill_value
