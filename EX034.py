sal = float(input("QUal salário do funcionario?9 R$ "))

if sal > 1250:
    aumento = sal * 0.10
    novo_sal = sal + aumento
    print("Seu novo salario com reajuste será R$ {}".format(novo_sal))
else:
    aumento = sal * 0.15
    novo_sal = sal + aumento
    print("Seu novo salario com reajuste será R$ {}".format(novo_sal))
