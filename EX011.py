largura = float(input("Informe a largura da parede: "))
altura = float(input("Ïnforme a altura da parede: "))
area = largura * altura

print("Ä sua parede tem dimensão de {} X {} e sua aréa de {}m²".format(largura,altura,area))

tinta = area / 2

print("Para pintar essa parede , voce vai precisar de {}L de tinta".format(tinta))