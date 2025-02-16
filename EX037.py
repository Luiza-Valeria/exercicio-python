numero = int(input("Digite um número: "))
print("--="*20)
print(""" 
          1 BINÁRIO
          2 OCTAL
          3 HEXADCIMAL""")
print("--="*20)
escolha = int(input("Para que base desejar converter: "))
if escolha == 1:
    print("{} convertido para binário fica {}".format(numero,bin(numero)))
elif escolha == 2:
    print("{} convertIdo para octa fica {}".format(numero,oct(numero)))
elif escolha == 3:
    print("{} Hexadecimal para binário fica {}".format(numero,hex(numero)))
else:
    print("VALOR INVALIDO")


