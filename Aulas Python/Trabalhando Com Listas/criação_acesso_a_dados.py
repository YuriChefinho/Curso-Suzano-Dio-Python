#usando [].copy na lista
lista = [1, "Python", [40, 30, 20]]
ls = lista.copy()

print(lista)

ls[0] = 2
print(ls)
print(lista)



#usando [].count

cores = ["vermelho", "azul", "amarelo", "rosa", "azul"]

numero_cor = cores.count("vermelho"), cores.count("azul")

print(numero_cor)

#usando [].extend

linguagens = ["Python", "js", "c#"]

print(linguagens)

linguagens.extend(["java","c"])

print(linguagens)

#usando [].index

linguagens = ["Python", "js", "c#", "js", "java"]

print(linguagens.index("js"))

#usando [].pop

linguagens = ["Python", "php", "c#", "js", "java"]

print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop(0))


#usando [].remove

linguagens = ["Python", "php", "c#", "js", "java"]

linguagens.remove("c#")
print(linguagens)


#usando [].reverse

linguagens = ["Python", "php", "c#", "js", "java"]

linguagens.reverse()

print(linguagens)

#usando [].sort

linguagens = ["python", "php", "c#", "js", "java"]
linguagens.sort()
print(linguagens)

linguagens.sort(reverse=True)
print(linguagens)

linguagens.sort(key=lambda x: len(x))
print(linguagens)

linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)


# usando len

linguagens = ["Python", "php", "c#", "js", "java"]
len(linguagens)
print(len(linguagens))


#usando sorted

linguagens = ["Python", "php", "c#", "js", "java"]
print(sorted(linguagens, key=lambda x: len(x)))
print(sorted(linguagens))


