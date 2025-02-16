velocidade_limite = 80
velocidade = int(input("Infome a velocidade do carro: "))

if velocidade > velocidade_limite:
    execesso = velocidade - velocidade_limite
    multa = execesso * 7
    print("Voce execedeu o limite em {} KM".format(execesso))
    print("Valor da multa R$ {}".format(multa))
else:
    print("Continue nessa velocidade")