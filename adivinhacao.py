import random

def jogar():

    print("*************************************")
    print("Olá, bem vindo ao jogo de adivinhação")
    print("*************************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if nivel == 1:
        total_de_tentativas = 10
    elif nivel == 2:
        total_de_tentativas = 5
    elif nivel == 3:
        total_de_tentativas = 3
    else:
        print("Nível escolhido não existe!")

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_srt = input("Digite o seu número: ")
        chute = int(chute_srt)

        if chute < 0 or chute > 100:
            print("Você deve digitar um número entre 0 e 100")
            continue

        if numero_secreto == chute:
            print("Você acertou e fez {} pontos".format(pontos))
            break
        else:
            if chute > numero_secreto:
                print("Errooooou!! Chute para baixo")
            elif chute < numero_secreto:
                print("Errooooou!! Chute para cima ")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo!")