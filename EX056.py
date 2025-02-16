maior = 0
soma_idade = 0
contador = 0
contador_mulher = 0
nome_homem_mais_velho = ''

for p in range(1,5):
    print("---- {}ª PESSOA ----".format(p))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade : "))
    sexo = str(input("Sexo [M/F]: ")).strip()

    soma_idade += idade
    contador += 1
    media = soma_idade/contador

    if sexo == "M":
        if idade > maior:
            maior = idade
            nome_homem_mais_velho = nome

    if sexo == "F":
        if idade < 20:
            contador_mulher += 1

print("A media de idade do grupo é de {}".format(media))
print("O homem mais velho é {} e ele tem {} anos".format(nome_homem_mais_velho ,maior))
print("Ao todo são {} mulheres com menos de 20 anos".format(contador_mulher))