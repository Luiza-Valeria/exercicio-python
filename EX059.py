while True:
    n1 = int(input("Digite o primeiro número inteiro: "))
    n2 = int(input("Digite o segundo número inteiro: "))

    print('''
           [ 1 ] SOMA
           [ 2 ] MULTIPLICAR 
           [ 3 ] MAIOR
           [ 4 ] NOVOS NÚMEROS
           [ 5 ] SAIR DO PROGRAMA
    ''')
    escolha = int(input("Digite a opção desejada: "))

    if escolha == 1:
        soma = n1 + n2
        print(f"A soma de {n1} e {n2} é igual a {soma}.")
    elif escolha == 2:
        mult = n1 * n2
        print(f"A multiplicação de {n1} e {n2} é igual a {mult}.")
    elif escolha == 3:
        if n1 > n2:
            maior = n1
        elif n2 > n1:
            maior = n2
        else:
            maior = "nenhum, pois são iguais"
        print(f"O maior número é {maior}.")
    elif escolha == 4:
        print("Informe os novos números...")
        continue
    elif escolha == 5:
        print("Encerrando o programa. Até mais!")
        break  # Sai do loop
    else:
        print("Opção inválida. Tente novamente.")

    print("-=" * 20)
