lista = [1, 2, 3, 4, 2, 5, 6, 1]
print(set(lista))

print(set("abacaxi"))

#converter set para uma lista

numeros = {1, 2, 3, 4, 2,}
frutas = {"banana"," uva", "maçã"}

#print(numeros[1]) para escolher o valor do set tem que transformar em lista

numeros = list(numeros)


print(numeros[1])

for numero in numeros:
    print(numero)

for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")


#Métodos da classe set

#{}.union

conjunto_a = {1, 2}
conjunto_b = {3, 4}

print(conjunto_a.union(conjunto_b))

#{}.intersection
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.intersection(conjunto_b))

#{}.difference

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

#{}.symmetric_difference

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.symmetric_difference(conjunto_b))

#{}.issubset

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4, 5, 6, 1}

print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))

#{}.isdisjoint

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

print(conjunto_a.isdisjoint(conjunto_b))

print(conjunto_a.isdisjoint(conjunto_c))

#{}.add / {}.copy / {}.clear

sorteio = {1, 23}

sorteio.add(25)

print(sorteio)

sorteio.add(43)

print(sorteio)

sorteio.add(23)

print(sorteio)

sorteio.copy()

print(sorteio)

sorteio.clear()
print(sorteio)

#{}.discard

numero = {10, 2, 3, 4, 50, 1, 6, 32, 7, 8, 3 ,0, 39,43,42}

print(numero)

numero.discard(1)
print(numero)

numero.discard(45)

print(numero)

#{}.pop

numero = {1, 2, 3, 4, 50, 1, 6, 7, 8, 3 ,0, 39,43,42}


print(numero.pop())
print(numero.pop())
print(numero.pop())
print(numero.pop())
print(numero.pop())
print(numero)
