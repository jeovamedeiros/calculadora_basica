# Criando uma calculadora básica

print("::: Seja Bem Vindo a CALCULADORA do JEOVÁ ::: ")
print(" ")
print("      ------- Navegando na calculadora ------      ")
print(" ")

print("Três tentativas de cálculo: ")
print(" ")
print(" ")

i = 0

while (i < 3):

    numero1 = float(input('Digite algum número: '))
    operacaoMatematica  = input('Digite a operação desejada: ')
    numero2 = float(input('Digite algum outro número: '))
    resultado = numero1 + numero2
   

    if operacaoMatematica == '+':
        resultado = numero1 + numero2
        print('Valor da Soma é: ' + str(resultado))
        print(" ")
    elif operacaoMatematica == '-':
        resultado = numero1 - numero2
        print('Valor da Subtração é: ' + str(resultado))
        print(" ")
    elif operacaoMatematica == '*':
        resultado = numero1 * numero2
        print('Valor da Multiplicação é: ' + str(resultado))
        print(" ")
    elif operacaoMatematica == '/':
        resultado = numero1 / numero2
        print('Valor da Divisão é: ' + str(resultado))
        print(" ")
    else:
        print("Operação inválida, tente novamente")
        print(" ")
    i = i+1

print(" ::: Fim da calculadora ::: ")

    




