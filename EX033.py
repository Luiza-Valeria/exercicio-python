n1 = int(input("Digite um número: "))
n2= int(input("Digite um número: "))
n3 = int(input("Digite um número: "))

menor = n1
if n2 < n3 and n2 < n1:
    menor = n2
if n3 < n1 and n3 < n1:
    menor = n3

maior = n1
if n2 > n3 and n2 > n1:
    maior = n2
if n3 > n1 and n3 > n1:
    menor = n3
print("O menor número digitado foi {}".format(menor))
print("O maior número digitado foi {}".format(maior))