from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Float, Integer, String, DateTime
from datetime import datetime

#Cria a classe Base para definir a tipagem dos dados da tabela do SQLALCHEMY (na versão 2.x)
Base = declarative_base()

class BitcoinPreco(Base):
    
    __tablename__ = "bitcoin_preco"
    """Definindo a tipagem das colunas"""
    id = Column(Integer, primary_key=True, autoincrement=True)
    valor = Column(Float, nullable=False)
    criptomoeda = Column(String, nullable=False)
    moeda = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.now)

