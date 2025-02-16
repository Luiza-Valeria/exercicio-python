from math import radians,sin,cos,tan

n = int(input("Informe um angulo: "))

seno = sin(radians(n))
cos = cos(radians(n))
tang = tan(radians(n))

print("O Seno do angulo {} é igual a {:.2f}".format(n,seno))
print("O Coseno do angulo {} é igual a {:.2f}".format(n, cos))
print("A tangente do angulo {} é igual a {:.2f}".format(n, tang))