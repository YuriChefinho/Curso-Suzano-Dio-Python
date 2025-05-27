#Criação e acesso aos dados
#Um dicionário é um conjunto não-ordenado de pares {Chave:Valor,} onde as chaves são únicas.

#Exemplo:

pessoa = {"nome": "Guilherme", "idade": 28 }
print(pessoa)

pessoa = dict(nome="guilherme", idade=28)
print(pessoa)

pessoa["telefone"] = "71996-8533" 
print(pessoa)

print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["telefone"])

pessoa["nome"] = "Maria"
pessoa["idade"] = 18
pessoa["telefone"] = "99500-2441"


print(pessoa)

#Dicionário Aninhado

contatos = {
    "ochefinho@gmail.com": {"nome": "yuri", "telefone": "(71)99685-4421"},
    "euportinary@gmail.com": {"nome": "yuri santos", "telefone": "(71)99685-3210"},
    "yuriportinary@gmail.com": {"nome": "yuri portinary", "telefone": "(71)98285-4421", "extra": {"a": 1}}}

print(contatos["yuriportinary@gmail.com"]["extra"]["a"])

#iteração com o dicionario

for chave in contatos:
    print(chave, contatos[chave])

print('='*100)
for chave, valor in contatos.items():
    print(chave,valor)