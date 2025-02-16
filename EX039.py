ano = int(input("Digite o ano em que voce nasceu: "))
idade = 2024 - ano
print("Quem nasceu em {} tem {} anos".format(idade,idade))

if idade < 18:
    falta = 18 - idade
    print(" Ainda faltam {} anos para voce se alistar".format(falta))
elif idade == 18:
    print("Esta na hora de se alistar, IMEDIATAMENTE!!")
else:
    passou = idade - 18
    print("Já Passou {} anos que voce deveria se alistar".format(passou))