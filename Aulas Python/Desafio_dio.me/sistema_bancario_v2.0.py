import textwrap


def menu(): # inicio da função  menu
    
    menu = """
    ===============================
    Sejá Muito Bem Vindo Ao PyBank!
    ===============================
    [ 1 ] = Depósito
    [ 2 ] = Saque
    [ 3 ] = Extrato
    [ 0 ] = Sair

    [ 5 ] = Nova Conta
    [ 6 ] = Listar Conta
    [ 7 ] = Novo Usuário 
    ===================> """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /): # inicio da função deposito

    if valor > 0: #inicio da condição de deposito
        saldo += valor
        extrato += f"Depósito: \tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é invalido. @@@")

    return saldo, extrato #fim da condição deposito

def sacar(*, saldo, valor, extrato, limite, numero_saque, limite_saque): # inicio da função saque
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saque >= limite_saque 

    if excedeu_saldo:
        print("\n@@@ Opção falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saque:
        print("\n@@@ Operação falhou! Número máximo de saques exedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: \t\tR$ {valor:.2f}\n"
        numero_saque += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================= EXTRATO =================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f'\nSaldo:\t\tR$ {saldo:.2f}')
    print("===================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (Somente Números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereço = input("informe o endereço (logradouro, Nº - bairro - cidade/sigla estado): ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereço})

    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
        
    while True:

        opção = menu()

        if opção == "1":
            valor = float(input("informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opção == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saque=numero_saques,
                limite_saque=LIMITE_SAQUES,
            )

        elif opção == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opção == "7":
            criar_usuario(usuarios)

        elif opção == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opção == "6":
            listar_contas(contas)

        elif opção == "0":
            print('======== OBRIGADO POR USAR O PYBANK =========')
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada. ")

        

main()