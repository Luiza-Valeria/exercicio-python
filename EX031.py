km = int(input("Quantos km tem a sua viagem: "))
print("Voce esta prestes a começar uma viagem de {}KM".format(km))
if km <= 200:
    custo = km * 0.50
    print("Sua viagem custará R${}".format(custo))
else:
    custo = km * 0.45
    print("Sua viagem custará R${}".format(custo))
