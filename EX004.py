n = input("Digite algo: ")
print(type(n))
print(n, "Possui apenas número e letras ? ", n.isalnum())
print(n, "Possui apenas letras? ", n.isalpha())
print(n,"Possui Apenas números ?", n.isnumeric())
print(n,"Possui TODAS as letras em minusculo ?",n.islower())
print(n,"Possui TODAS as letras em maiusculas ?",n.isupper())

