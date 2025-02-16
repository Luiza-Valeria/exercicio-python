count = 0
for num in range(1, 500 + 1):
    if num % 2 != 0 and num % 3 == 0:
        count += num
        print(num)
print("A SOMA DOS NÚMEROS IMPARES DIVISIVEIS POR 3 É {}".format(count))