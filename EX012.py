produto = float(input("Informe o preço do produto: RS "))
desconto = produto * 0.05

vf = produto - desconto

print("O produto no valor de R$ {} com desconto de 5% sai a R$ {:.2f}".format(produto,vf))

