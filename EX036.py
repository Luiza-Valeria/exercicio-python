casa = float(input("Valor da casa: R$ "))
salario = float(input("Salário do comprador: R$ "))
ano = int(input("Quantos anos do financiamento? "))

prestacao = casa / (ano * 12)
limite_salario = (salario * 0.30) - salario

if prestacao > limite_salario:
    print("EMPRESTIMO APROVADO!")
else:
    print("EMPRESTIMO NEGADO!")
print("Para pagar uma casa R$ {} em {} anos a prestação será de R$ {:.2f}".format(salario,ano,prestacao))