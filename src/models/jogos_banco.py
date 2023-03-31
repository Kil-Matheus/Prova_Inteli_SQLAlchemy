from models.game import Game

def jogos():
    j2 = Game(nome_jogo='FORSPOKEN', plataforma='PC', preco=299, quantidade=8)
    J3 = Game(nome_jogo='DEAD ISLAND 2', plataforma='PS5', preco=350, quantidade=10)
    J4 = Game(nome_jogo='HOGWARTS LEGACY', plataforma='PC', preco=219, quantidade=7)
    J5 = Game(nome_jogo='WILD HEARTS', plataforma='XBox Series', preco=350, quantidade=7)
    j6 = Game(nome_jogo='RESIDENT EVIL 4', plataforma='PS5', preco=289, quantidade=10)
    j7 = Game(nome_jogo='THE LEGEND OF ZELDA: TEARS OF THE KINGDOM', plataforma='Switch', preco=350, quantidade=10)

    return j2, J3, J4, J5, j6, j7