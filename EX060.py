# Solicita ao usuário um número inteiro
numero = int(input("Digite um número para calcular o fatorial: "))

fatorial = 1
contador = numero

print(f"Cálculo do fatorial de {numero}:")

while contador > 0:
    if contador == 1:
        print(f"{contador} = ", end="")
    else:
        print(f"{contador} x ", end="")

    fatorial *= contador
    contador -= 1

print(fatorial)
