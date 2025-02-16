from math import pow

p =float(input("Digite seu Peso: "))
a = float(input("Digite sua altura: "))

imc = p / a ** 2

print("O seu imc atual é de {:.2f}".format(imc))

if imc < 18.5:
    print("Voce esta Abaixo do Peso, Procure Ajuda!!")
elif imc >= 18.5 and imc < 25:
    print("Voce esta no seu Peso Ideal , Continue Assim!!!")
elif imc >= 25 and imc < 30:
    print("Voce esta com Sobrepeso, Tome cuidado!!")
elif imc >= 30 and imc < 40:
    print("Voce esta Obeso, Procure Ajuda!!!")
else:
    print("Voce esta com Obessidade Morbida, Procure um Especialista Urgnete!!!")