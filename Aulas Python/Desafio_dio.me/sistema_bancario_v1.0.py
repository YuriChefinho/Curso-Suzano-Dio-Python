
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
[ 0 ] = Sair
===================> """

# Variaveis de controle
saldo = 0
LIMITE_SAQUES = 3
saque_diario = 500 #Saque de até R$500
extrato = ''
saque = 0
depósito = 0
numero_saque = 0


#inicio do laço 
while True:
    
    print(boas_vindas)
    opção = int(input(menu))
    sleep(.4)

    if opção == 1: # Lógica de Depósito
        depósito = float(input('Qual O Valor Do Deposito? R$ '))

        if depósito >0:
            saldo += depósito
            sleep(.4)
            extrato += f"Depósito: R$ {depósito:.2f} "
            print(f"Depositando o valor de R$ {depósito:.2f} Aguarde...")
            sleep(2)
            print(f"Deposito de R$ {depósito:.2f} efetuado com SUCESSO.")

        else:
            print('Operação falhou! O valor informado é inválido. ')



    elif opção == 2: # Lógica de Saque
        saque = float(input('Qual O Valor Do Saque? R$ '))
        
        
        excedeu_saldo = saque > saldo
        excedeu_limite = saque > saque_diario
        excedeu_saque = numero_saque >= LIMITE_SAQUES


        if (saque <= saque_diario) and (saque > 0) and (numero_saque != 3):
            saldo -= saque
            numero_saque += 1
            print('EFETUANDO O SAQUE PORFAVOR AGUARDE...'),sleep(2)
            print(f"Saque de R$ {saque:.2f} efetuado com SUCESSO \nSaldo atual R$ {saldo:.2f}")

        elif excedeu_limite:
            print(f"O Valor  de R$ {saque:.2f} excede o valor diario de R$ 500,00")
            print("SAQUE NEGADO!!!")


        elif saque < 0:
            print('Comando invalido, tente novamente!')

        elif excedeu_saque:
            print('Limite de saque excedido')


    

    elif opção == 3: # Lógica de extrato

        print("<<IMPRIMINDO EXTRATO>>\n")
        sleep(2)
        print('Não Foram realizadas movimentações.\n' if not extrato else "")
        print(f"ULTIMO DEPOSITO      R$ {depósito:.2f} \n\nULTIMO SAQUE         R$ {saque:.2f} \n\nSALDO EM CONTA       R${saldo:.2f}")
        #print(extrato + f" O saldo da sua conta é R${saldo:.2f}")




    elif opção == 0: # Lógica de Sair
        sair = """
==============================
Obrigado por escolher o PyBank
        Até Logo!
=============================="""
        print(sair)
        break

    else:
        print('!!!COMANDO INVALIDO \nTENTE NOVAMENTE!!!')
        

            
    