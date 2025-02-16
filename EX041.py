ano = int(input("Ano nascimento: "))
idade = 2024 - ano

if idade <= 9:
    print("Voce esta na categoria MIRIM")
elif idade <= 14:
    print("Voce esta na categoria INFANTIL")
elif idade <= 19:
    print("Voce esta na categoria JUNIOR")
elif idade <= 20:
    print("Voce esta na categoria SENIOR")
else:
    print("Voce esta na categoria MASTER")




