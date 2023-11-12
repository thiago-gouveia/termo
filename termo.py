
import random

def inicializa(palavras):
    sorteado = random.randint(0, len(palavras) - 1)
    
    configuracao_jogo = {
        'n': len(palavras[sorteado]),
        'sorteada': palavras[sorteado],
        'especuladas': [],
        'tentativas': len(palavras[sorteado]) + 1
    }

    return configuracao_jogo
