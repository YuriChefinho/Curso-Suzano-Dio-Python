
from time import sleep

boas_vindas = """
===============================
Sejá Muito Bem Vindo Ao PyBank!
===============================
"""

menu = """
[ 1 ] = Depósito
[ 2 ] = Saque
[ 3 ] = Extrato
[ 4 ] = Sair
===================> """

saldo = 1500
LIMITE_SAQUES = 500
saque_diario = 0
extrato = ''

while True:
    
    print(boas_vindas)
    opção = int(input(menu))
    sleep(.4)

    if opção == 1:
        depósito = float(input('Quanto Você Quer Depositar? '))

        if depósito >0:
            saldo += depósito
            sleep(.4)
            extrato += f"Depósito: {depósito:.2f}"

        else:
            print('Operação falhou! O valor informado é inválido. ')

    elif opção == 2:
        saque = float(input('Informe o valor do saque:'))
        

            #print(f'Deposito com SUCESSO! \nSEU SALDO É {deposito}')
