frutas = ["laranja", "maçã", "uva"]
print(frutas)
frutas = []

letras = list("Python")
print(letras)

numero = list(range(10))
print(numero)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)


# usando for em listas 
for itens in (carro):
    print(itens)

for indice, carro in enumerate(carro):
    print(f'{indice}: {carro}')


#compreensão de listas
numeros = [1,  30,   21,  2, 9, 65, 34]
pares = []


for numero in numeros:
    if numero % 2 == 0 :
        pares.append(numero)
        print(pares)

impar = [numero for numero in numeros if numero % 2 == 1]
print(impar)

#modificando valores da lista
numeros = [1,  30,   21,  2, 9, 65, 34]
quadrado = []
quadrado_2 = []
for numero in numeros:
    quadrado.append(numero ** 2)
    print(quadrado)

quadrado_2 = [numero ** 2 for numero in numeros ]
print(quadrado_2)