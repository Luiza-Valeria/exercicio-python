nome = str(input("Digite seu nome completo: ")).strip()
print("Seu nome em maiscúlas é {}".format(nome.upper()))
print("Seu nome em minuscúlas é {}".format(nome.lower()))

print("Seu nome tem {} letras".format(len(nome) - nome.count(' ')))

nome = nome.split()
print("O seu primeiro nome tem {} Letras".format(len(nome[0])))