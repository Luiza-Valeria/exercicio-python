from random import randint
c = randint(0,11)
cont_palpite = 0
print("--=" * 20)
print("Vou pensar em um número entre 0 e 10. Tente adivinhar....")
print("--=" * 20)
print("PROCESSANDO...")

while True:
    n = int(input("Em que número eu pensei? "))
    cont_palpite += 1

    if n == c:
        print(f"Parabéns! Você acertou em {cont_palpite} tentativas.")
        break
    if n > 10:
        print("Digite um valor inteiro de 0 ate 10")
    else:
        print("Errou! Tente novamente.")