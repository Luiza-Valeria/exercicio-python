n1 = int(input("Primeiro número: "))
n2 = int(input("Primeiro número: "))

if n1 > n2:
    print("{} é maior que {}".format(n1,n2))
if n2 > n1:
    print("{} é maior que {}".format(n2,n1))
else:
    print("Os números {} e {} são iguais".format(n1,n2))