# A tupla é uma estrutura imutável 
# Diferente da lista que é mutável
# Pratica comum usar uma "," no final de cada elemento sa tupla

frutas = ("Laranja", "pera", "uva", )

letra = tuple("python")

numeros = tuple([1, 2, 3, 4])

pais = ("Brasil", )


print(frutas[-1], frutas[-3])

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[2])

#fatiamento

tupla = ("p", "y", "t", "h", "o", "n",)

print(tupla[2:])
print(tupla[1:4])
print(tupla[-1])
print(tupla[::-1])

#iteração

carros9 = ("gol","celta","palio",)
for indice, carro in enumerate(carros9):
    print(f"{indice}: {carro}")

carros = ("gol")
print(isinstance(carros, tuple))