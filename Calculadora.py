# -*- coding: UTF-8 -*-
#Python Calculator

def start():
    fun_opcao(1)
    while fun_continuar():
        fun_opcao(1)
    else:
        print('Obrigado')

def fun_continuar():
    continuar = input('Deseja continuar? y or n\n R: >> ')
    return True if continuar == 'y' else False

def fun_opcao(tentativas):
    opcao = int(input('Selecine a opção desejada:\n   1-Soma\n   2-Subtração\n   3-Multiplicação\n   4-Divisão\n R: >> '))
    if opcao not in (1,2,3,4):
        tchau() if tentativas > 2 else opcao_invalida(tentativas)
    else:
        fun_calc(opcao)

def tchau():
    print('Volte outra hora, Tchau!') 
    exit()

def opcao_invalida(tentativas):
    print('Opção invalida, tente novamente')
    tentativas += 1
    fun_opcao(tentativas)

def fun_calc(opcao):
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o segundo valor: '))
    if opcao == 1:
        #soma(valor1, valor2)
        #Teste usando lambda
        soma = lambda valor1,valor2 : valor1 + valor2
        print(f'Valor da soma é: {soma(valor1, valor2)}')
    elif opcao == 2:
        subtracao(valor1, valor2)
    elif opcao == 3:
        multiplicacao(valor1, valor2)
    else:
        divisao(valor1, valor2)

def soma(valor1, valor2): print(f'Valor da soma é: {valor1+valor2}')

def subtracao(valor1, valor2): print(f'Valor da subtração é: {valor1-valor2}')

def multiplicacao(valor1, valor2): print(f'Valor da multiplicação é: {valor1*valor2}')

def divisao(valor1, valor2): print(f'Valor da divisão é: {valor1/valor2}')

if __name__ == "__main__":
    start()
