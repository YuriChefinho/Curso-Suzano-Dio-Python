
#Maiúscula, Minúscula, Title
nome = "YuRi SaNtOs"

print(nome.upper())
print(nome.lower())
print(nome.title())

#Eliminando Espaços em Branco
texto = "   Olá Mundo  "
print('*' + texto + '*')
print('*' + texto.strip() + '*')
print('*' + texto.lstrip() + '*')
print('*' + texto.rstrip() + '*')

# Junção e Centralização
menu = "Python"

print("###" + menu + "####")
print(menu.center(14, "*"))
print(menu.center(14))
print("-".join(menu))