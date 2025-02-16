ano = int(input("Informe que ano estamos: "))

if ano % 4 == 0:
    print("{} é um ano BISSEXTO!!".format(ano))
else:
    print("{} NÃO é um ano BISSEXTO!!".format(ano))