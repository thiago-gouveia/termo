from termcolor import colored  # Certifique-se de ter o pacote termcolor instalado (pip install termcolor)
import filtra
import indica
import termo

def exibe_palavra(palavra, letras_acertadas):
    palavra_formatada = ""
    for i in range(len(palavra)):
        if letras_acertadas[i] == 0:
            palavra_formatada += colored(palavra[i], 'blue')
        elif letras_acertadas[i] == 1:
            palavra_formatada += colored(palavra[i], 'yellow')
        else:
            palavra_formatada += colored(palavra[i], 'grey')
    return palavra_formatada

def jogo_insper_termo():
    print("===========================")
    print("|                           |")
    print("|     Bem-vindo ao Termo    |")
    print("|                           |")
    print(" ==== Design de Software ===")
    print("Comandos: desisto")
    print("Regras:")
    print(" - Você tem 6 tentativas para acertar uma palavra aleatória de 5 letras.")
    print(" - A cada tentativa, a palavra testada terá suas letras coloridas conforme:")
    print("   . Azul   : a letra está na posição correta;")
    print("   . Amarelo: a palavra tem a letra, mas está na posição errada;")
    print("   . Cinza: a palavra não tem a letra.")
    print(" - Os acentos são ignorados;")
    print(" - As palavras podem possuir letras repetidas.")

    palavras = ["termo", "python", "jogo", "insper", "software"]  # Adicione mais palavras conforme necessário

    configuracao_jogo = termo.inicializa(palavras)
    palavra_sorteada = configuracao_jogo['sorteada']
    tentativas_restantes = configuracao_jogo['tentativas']

    while tentativas_restantes > 0:
        print("\nSorteando uma palavra...")
        print(f"Já tenho uma palavra! Tente adivinhá-la!")
        print(f"Você tem {tentativas_restantes} tentativa(s)")

        palpite = input("Qual seu palpite? ").lower()

        if palpite == 'desisto':
            print(f"A palavra correta era: {palavra_sorteada}")
            print("Você desistiu. O jogo acabou.")
            break

        palpite_filtrado = filtra.filtra([palpite], len(palavra_sorteada))[0]
        posicoes = indica.inidica_posicao(palavra_sorteada, palpite_filtrado)

        print("\nResultado:")
        print(exibe_palavra(palpite_filtrado, posicoes))

        if posicoes.count(0) == len(palavra_sorteada):
            print("Parabéns! Você acertou a palavra!")
            break
        else:
            tentativas_restantes -= 1
            if tentativas_restantes == 0:
                print(f"Suas tentativas acabaram. A palavra correta era: {palavra_sorteada}")
                break
            else:
                print("Tente novamente!")

if _name_ == "_main_":
    jogo_insper_termo()
