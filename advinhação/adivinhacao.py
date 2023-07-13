import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhacao!")
print("*********************************")

numero_secreto = random.randrange(1, 100)
chances = 0

print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina um nível: "))

if(nivel == 1):
    chances = 20
elif(nivel == 2):
    chances = 10
else:
    chances = 5

for rodada in range(1, chances + 1):
    print("Tentativa {} de {}".format(rodada, chances))
    chute = int(input("Digite um número entre 1 e 100: "))

    if chute < 1 or chute > 100:
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Você acertou!")
        break
    else:
        if maior:
            print("Você errou! O seu chute foi maior do que o número secreto")
        elif menor:
            print("Você errou! O seu chute foi menor do que o número secreto")

print("FIM DE JOGO")