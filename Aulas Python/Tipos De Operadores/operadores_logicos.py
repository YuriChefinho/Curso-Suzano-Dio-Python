saldo = 1000
saque = 200
limite = 100
conta_especial = True

print(saldo >= saque and saque <= limite or conta_especial and saldo >= saque)


print((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque))

print("=+"*30)

print(saldo >= saque)
print(saque <= limite)
print(saldo >= saque and saque <= limite)
print(saldo >= saque or saque <= limite)

contatos_emergencia = []

print(not 1000 > 2000)
print(not "saque 1500;")
print(not "")

