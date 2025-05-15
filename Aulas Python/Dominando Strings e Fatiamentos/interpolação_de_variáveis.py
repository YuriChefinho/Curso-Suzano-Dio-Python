nome = "Yuri Santos"
idade = 28
profissão = "Programador"
linguagem = "Python"

#Old Style%
print("Olá, eu chamo %s. Eu tenho %d anos de idade, trabalho com %s e estrou matriculado no curso de %s" %(nome, idade, profissão, linguagem))

#Metodo Format
print("Olá, eu chamo {}. Eu tenho {} anos de idade, trabalho com {} e estrou matriculado no curso de {}" .format(nome, idade, profissão, linguagem))

print("Olá, eu chamo {0}. Eu tenho {1} anos de idade, trabalho com {2} e estrou matriculado no curso de {3}" .format(nome, idade, profissão, linguagem))

#f-string

print(f"Olá, eu chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissão} e estrou matriculado no curso de {linguagem}")

#Formatar strings com f-string

PI = 3.14159
print(f"Valor de PI: {PI:.2f}")

print(f"Valor de PI: {PI:10.2f}")

dados = {"nome": "Yuri", "idade": 28}

print("Nome: {nome} Idade: {idade}".format(**dados))


#Fatiamento de strings

nome = "Yuri Santos"

print(nome[0])
print(nome[-1])
print(nome[:9])
print(nome[10:])
print(nome[10:16])
print(nome[10:16:2])
print(nome[:])
print(nome[::-1])