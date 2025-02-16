n = int(input("Digite o número que deseja ver a tabuada: "))

for num in range (1,10 + 1):
    total = n * num
    print("{} X {} = {}".format(n,num,total) )