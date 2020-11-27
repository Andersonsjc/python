import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhacao!")
    print("*********************************")
    #numero_secreto = round(random.random() * 100)
    numero_secreto = random.randrange(0,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nivel de dificuldade?")
    print("(1) Facil (2) Medio (3) Dificil")

    nivel = int(input("Defina o nivel: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    #print(numero_secreto)

    #USANDO FOR
    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um numero entre 1 e 100: ")
        print("Voce digitou " , chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Voce deve digitar um numero entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Voce acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Voce errou! O seu chute foi maior do que o numero secreto.")
            elif(menor):
                print("Voce errou! O seu chute foi menor do que o numero secreto.")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

    print("Numero segreto: {}".format(numero_secreto))
    #USANDO WHILE
    #rodada = 1

    #while (rodada <= total_de_tentativas):
    #    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    #
    #    chute_str = input("Digite o seu numero: ")
    #    print("Voce digitou " , chute_str)
    #    chute = int(chute_str)
    #
    #    acertou = chute == numero_secreto
    #    maior = chute > numero_secreto
    #    menor = chute < numero_secreto
    #
    #    if(acertou):
    #        print("Parabens! Voce acertou!")
    #    else:
    #        if(maior):
    #            print("O seu chute foi maior do que o numero secreto!")
    #        elif(menor):
    #            print("O seu chute foi menor do que o numero secreto!")
    #
    #    rodada = rodada + 1

    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()
