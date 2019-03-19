import random


def jogar():
    print("*************************************************")
    print("Olá, bem vindo ao jogo de Pedra, Papel ou Tesoura")
    print("*************************************************")

    opcoes = ("Pedra", "Papel", "Tesoura")

    ganhou = False

    while not ganhou:
        print("")
        print("***********************")
        escolha = int(input("Selecione (0)Pedra, (1)Papel ou (2)Tesoura: "))

        maquina_escolha = opcoes[random.randrange(0, 3)]
        minha_escolha = opcoes[escolha]

        if minha_escolha == "Pedra" and maquina_escolha == "Tesoura":
            ganhou = True
            print("Você Venceu!")
        elif minha_escolha == "Papel" and maquina_escolha == "Pedra":
            ganhou = True
            print("Você Venceu!")
        elif minha_escolha == "Tesoura" and maquina_escolha == "Papel":
            ganhou = True
            print("Você Venceu!")
        elif minha_escolha == maquina_escolha:
            print("Vocês fizaram a mesma escolha!")
        else:
            print("Você Perdeu :(")

        print("Você escolheu:", minha_escolha)
        print("A máquina escolheu:", maquina_escolha)


if __name__ == "__main__":
    jogar()
