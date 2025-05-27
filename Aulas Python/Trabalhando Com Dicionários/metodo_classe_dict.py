contatos = {
    "ochefinho@gmail.com": {"nome": "yuri", "telefone": "(71)99685-4421"},
    "euportinary@gmail.com": {"nome": "yuri santos", "telefone": "(71)99685-3210"},
    "yuriportinary@gmail.com": {"nome": "yuri portinary", "telefone": "(71)98285-4421", "extra": {"a": 1}}}

print(contatos)
print("<=>"*66)

#{}.copy / {}.fromkeys / {}.clear

copia = contatos.copy()
copia["yuriportinary@gmail.com"] = {"nome": "Portinary"}
print(copia)

print("<=>"*66)

print(dict.fromkeys(["nome", "telefone"]))
print(dict.fromkeys(["nome", "telefone"], "vazio"))

contatos.clear()
print(contatos)
print("<=>"*66)

#{}.get / {}.items / {}.keys

contatos = {
    "ochefinho@gmail.com": {"nome": "yuri", "telefone": "(71)99685-4421"}}
 
#contatos["chave"] #keyError

print(contatos.get("chave"))
print(contatos.get("chave", {}))
print(contatos.get("ochefinho@gmail.com", {})) 

print(contatos)

print("<=>"*66)

print(contatos.items())

print("<=>"*66)

print(contatos.keys()) #retorna so as chaves
print("<=>"*66)


#{}.pop / {}.popitems

contatos = {
    "ochefinho@gmail.com": {"nome": "yuri", "telefone": "(71)99685-4421"}}

print(contatos.pop("ochefinho@gmail.com"))
print(contatos.pop("ochefinho@gmail.com", "não encontrou"))


contatos = {
    "ochefinho@gmail.com": {"nome": "yuri", "telefone": "(71)99685-4421"}}
print(contatos.popitem())
#print(contatos.popitem()) #KeyError
print("<=>"*66)

#{}.setdefault
contatos = {
    "ochefinho@gmail.com": {"nome": "yuri", "telefone": "(71)99685-4421"}}

contatos.setdefault("nome", "Guilherme")
print(contatos)

contatos.setdefault("idade", 28)
print(contatos)
print("<=>"*66)

#{}.update
contatos = {
    "ochefinho@gmail.com": {"nome": "yuri", "telefone": "(71)99685-4421"}}

contatos.update({"ochefinho@gmail.com": {"nome": "portinary"}})
print(contatos)

contatos.update({"yurisantos@gmail.com": {'nome': "yuri", "telefone": "71996853232"}})

print(contatos)
print("<=>"*66)

#{}.volues / {}.in
contatos = {
    "ochefinho@gmail.com": {"nome": "yuri", "telefone": "(71)99685-4421"},
    "euportinary@gmail.com": {"nome": "yuri santos", "telefone": "(71)99685-3210"},
    "yuriportinary@gmail.com": {"nome": "yuri portinary", "telefone": "(71)98285-4421", "extra": {"a": 1}}}


print(contatos.values())

lista_chaves: list = contatos.keys()

resultado = "eu " in contatos
print(resultado)

resultado = "ochefinho@gmail.com" in contatos
print(resultado)

resultado = "nome" in contatos["ochefinho@gmail.com"]
print(resultado)
print("<=>"*66)

#{}.del

contatos = {
    "ochefinho@gmail.com": {"nome": "yuri", "telefone": "(71)99685-4421"},
    "euportinary@gmail.com": {"nome": "yuri santos", "telefone": "(71)99685-3210"},
    "yuriportinary@gmail.com": {"nome": "yuri portinary", "telefone": "(71)98285-4421"}}

print(contatos)
del contatos["euportinary@gmail.com"]["telefone"]

print(contatos)
del contatos["yuriportinary@gmail.com"]

print(contatos)


carro = {"marca": "Fiat", "modelo": "palio", "placa": "ABD-9826"}
print(carro.get("motor"))