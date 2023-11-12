def inidica_posicao(sorteada, especulada):
    if len(sorteada) != len(especulada):
        return []

    posicoes = []

    for i in range(len(sorteada)):
        if sorteada[i] == especulada[i]:
            posicoes.append(0)
        elif especulada[i] in sorteada:
            posicoes.append(1)
        else:
            posicoes.append(2)

    return posicoes
