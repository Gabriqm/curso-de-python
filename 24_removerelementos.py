#lista = [1,2,3,4,5,6,7]

#print(lista)

#del lista[0]

#print(lista)

#del lista[len(lista) - 1]

#print(lista)

#EXERCÍCIO:

lista = [1,2,3,4,5,6,7,8,9,10]

print(lista)

i = 0

while i<len(lista):
    if lista[i] == 4:
        del lista[i]
    i = i + 1

print(lista)