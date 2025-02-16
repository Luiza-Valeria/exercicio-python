menor = 0
maior = 0
for i in range(1,7 + 1):
    ano_nasc = int(input("Informe o ano do seu nascimento: "))
    idade = 2024 - ano_nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print("Dessa lista {} pessoas ja antigingiram a maioridade".format(maior))
print("Dessa lista {} pessoas ainda NÃO atingiram a maior idade".format(menor))

