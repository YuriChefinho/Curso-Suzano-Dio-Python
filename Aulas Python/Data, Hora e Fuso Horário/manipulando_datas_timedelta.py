from datetime import date, datetime, timedelta

tipo_carro = input("Ocarro é (P) (G) ou (M)?").strip() # P, M, G

tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60

data_atual = datetime.now()

if tipo_carro =="p":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou {data_atual} e ficará pronto ás {data_estimada}")
elif tipo_carro =="m":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"O carro chegou {data_atual} e ficará pronto ás {data_estimada}")
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro chegou {data_atual} e ficará pronto ás {data_estimada}")



print(date.today() - timedelta(days=1))

resultado = datetime(2025, 8, 4, 5 , 19, 10) - timedelta(hours=1)

print(resultado.time())
print(datetime.now().date())

