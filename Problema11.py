lista1 = [2, 1, 2, 3, 0, 6, 7, 6, 4, 8]

lista2 = []
for i in lista1:
    if i not in lista2:
        lista2.append(i)

print(lista2)