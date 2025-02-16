import math

n = int(input("Digite um número: "))
dobro = n * 2
triplo = n * 3
raiz = math.sqrt(n)

print("O dobro de {} é igual a {}".format(n,dobro))
print("O triplo de {} é igual a {}".format(n,triplo))
print("A raiz quadrada de {} é igual a {:.2f}".format(n,raiz))