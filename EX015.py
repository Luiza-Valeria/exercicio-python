dia = float(input("Quantos dias alugados?:  "))
km = float(input("Quantos kMs rodados?:  "))

vf = (dia * 60) + (km * 0.15)

print("O total a pagar é de {}".format(vf))