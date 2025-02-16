import math

''''co = float(input("Informe o valor do Cateto Oposto: "))
ca = float(input("Informe o valor do Cateto Adjacente: "))

h = math.sqrt(co **2 + ca ** 2)
print("A hipotenusa vai medir {:.2f}".format(h))'''

co = float(input("Informe o valor do Cateto Oposto: "))
ca = float(input("Informe o valor do Cateto Adjacente: "))

h = math.hypot(ca,co)
print("A hipotenusa vai medir {:.2f}".format(h))



