"""def criar_carro (modelo, ano, placa, / , marca, *,motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("palio", 1999, "ABC-1234", "Fiat", motor='1.0', combustivel="Gasolina")"""

"""def somar(a, b):
    return a + b

def subitrair(a, b):
    return a - b

def exibir_resultado(a, b, função):
    resultado = função(a,b)
    print(f"o resultado da operação é = {resultado} ")

exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, subitrair)"""

salario = 2000
def salario_bonus(bonus, lista):
    global salario
    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista aux={lista_aux}")
    
    salario += bonus
    return salario

lista= [1]
salario_com_bonus = salario_bonus(500, lista)
print(salario_com_bonus)
print(lista)