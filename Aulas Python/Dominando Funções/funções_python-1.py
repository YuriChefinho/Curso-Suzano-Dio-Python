"""def exibir_mensagem():
    print("Olá Mundo")

def exibir_mensagem_2 (nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3 (nome='Anônimo'):
    print(f"seja bem vindo {nome}! ")

exibir_mensagem()
exibir_mensagem_2(nome="yuri")
exibir_mensagem_3()
exibir_mensagem_3("chappie")"""

"""def calcular_total (numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return  antecessor, sucessor

def func_3():
    print("Olá Mundo")
    

print(calcular_total([10,20,34]))
print(retorna_antecessor_e_sucessor(10))

print(func_3())"""


def salvar_carro (marca, modelo, ano, placa):
    print(f"carro inserio com suceso! {marca}/{modelo}/{ano}/{placa}")


salvar_carro("palio", "fiat", 1999, "ABC-1234")

salvar_carro(marca='Fiat', modelo='Palio', ano=1999, placa='ABC-1233')

salvar_carro(**{'marca': 'fiat', 'modelo': 'palio', 'ano': 1999, 'placa': 'ABC-1234'})

#conceito de args e kwargs

def exibir_poema(data_extenso, *args, **kwargs):
    texto = '\n' .join(args)
    meta_dados = '\n'.join ([f'{chave.title()}:  {valor}' for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema('zen of python', 'beautiful is better than ugly.', autor='Tim peters', ano=1999)