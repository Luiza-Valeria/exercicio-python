print("--=" * 15)
print("Analisador de Triangulos")
print("--=" * 15)
a = float(input("Primeiro Segmento: "))
b = float(input("Segundo Segmento: "))
c = float(input("Terceiro Segmento: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("TRIÂNGULO EQUILÁTERO")
    elif a == b or b == c or a == c:
        print("TRIÂNGULO ISÓCELES")
    else:
        print("TRIÂNGULO ESCALENO")
else:
    print("ESSES SEGMENTOS NÃO FORMAM UM TRIÂNGULO")