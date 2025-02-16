frase = str(input("Digite uma frase: ")).upper().strip()

print("A letra A aparece {} vezes".format(frase.count("A")))

print("A primeira vez que e letra A aparece é na posição {}".format(frase.find("A") + 1))

print("A ultima vez que e letra A aparece é na posição {}".format(frase.rfind("A") + 1))