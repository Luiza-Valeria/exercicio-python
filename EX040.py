n1 = float(input("Primeira Nota: "))
n2 = float(input("Segunda Nota: "))
n3 = float(input("Terceira Nota: "))

media = (n1 + n2 + n3) / 3

if media < 5:
    print("Você foi REPROVADO, estude mais!")
elif media >= 5 and media <= 6.9:
    print("Você está de RECUPERAÇÃO.")
else:
    print("Parabéns, você foi APROVADO!")
