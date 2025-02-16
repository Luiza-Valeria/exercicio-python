from random import randint
itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print(""""SUAS OPÇÕES 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
jogador = int(input('Qual é o sua jogada? '))
print("-="*11)
print("Computador jogou {}".format(itens[computador]))
print("Jogador jogou {}".format(itens[jogador]))
print("-="*11)

if computador == 0:
    if jogador == 0: # COMPUTADOR JOGOU PEDRA
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print("COMPUTADOR VENCE")
    else:
        print("JOGDA INVÁLIDA")
elif computador == 1: # COMPUTADOR JOGOU PAPE;
    if jogador == 0:
        print("COMPUTADOR VENCEU")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCEU")
    else:
        print("JOGADA INVÁLIDA")
elif computador == 2: #COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print("JOGADOR VENCEU")
    elif jogador == 1:
        print("COMPUTADOR VENCEU")
    elif jogador == 2:
        print("EMPATE")
    else:
          print("JOGADA INVÁLIDA")