import random

n1 = str(input("Primeiro Aluno: "))
n2 = str(input("Segundo Aluno: "))
n3 = str(input("Terceiro Aluno: "))
n4 = str(input("Quarto ALuno: "))

lista = [n1,n2,n3,n4]
sorteio = random.choice(lista)
print("O aluno escolhido foi {} ".format(sorteio))