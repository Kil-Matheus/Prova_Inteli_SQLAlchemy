from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models.base import Base
from models.game import Game
from models.jogos_banco import jogos

engine = create_engine('sqlite+pysqlite:///banco_prova.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

#Usado para Criar o Banco de Dados
j1 = Game(nome_jogo='DEAD SPACE REMAKE', plataforma='PS5', preco=350, quantidade=10)

#Função utilizada para enviar todos os jogos requisitados para o Banco de Dados
j2, j3, j4, j5, j6, j7 = jogos()

session.add(j1)
session.add(j2)
session.add(j3)
session.add(j4)
session.add(j5)
session.add(j6)
session.add(j7)
session.commit()

#Lista todos os jogos no Console
ver_jogo = session.query(Game).all()
print(ver_jogo)