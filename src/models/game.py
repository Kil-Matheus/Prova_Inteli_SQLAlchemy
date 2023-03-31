from models.base import Base
from sqlalchemy import Column, Integer, String

class Game(Base):
    __tablename__ = 'jogos'
    id = Column(Integer, primary_key=True)
    nome_jogo = Column(String(50))
    plataforma = Column(String(50))
    preco = Column(Integer)
    quantidade = Column(Integer)

def __repr__(self):
    return f'Game(nome_jogo={self.nome_jogo}, plataforma={self.plataforma}, preco={self.preco}, quantidade={self.quantidade})'