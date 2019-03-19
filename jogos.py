import forca
import adivinhacao
import pedra_papel_tesoura

print("******************************")
print("******Escolha o seu jogo******")
print("******************************")

print("(1) Forca (2) Adivinhação (3) Pedra, Papel ou Tesoura")

jogo = int(input("Qual jogo? "))

if jogo == 1:
    print("Jogar jogo da Forca!")
    forca.jogar()
elif jogo == 2:
    print("Jogar jogo de Adivinhação!")
    adivinhacao.jogar()
elif jogo == 3:
    print("Jogar jogo de Pedra, Papel ou Tesoura")
    pedra_papel_tesoura.jogar()
else:
    print("Opção inválida!")
