import random
c = random.randint(0,5)
print("--=" * 20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar....")
print("--=" * 20)
n = float(input("Em que número eu pensei: "))
print("PROCESSANDO...")
if n == c:
    print("PARABÉNS! VOcë conseguiu me vencer!")
else:
    print("Voce errou, o número que pensei foi {},TENTE NOVAMENTE !".format(c))