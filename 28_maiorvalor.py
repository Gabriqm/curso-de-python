lista = [13,55,87,2,1,3670,92]

maior_valor = 0

for n in lista:
    if n > maior_valor:
        maior_valor = n

print(maior_valor)

#Exercício encontre o menor valor de uma lista:

l = [4,8,5,4,2]

menor_valor = lista[0] #ou botar um numero muito grande, pq o 0 seria o menor valor disponível e causaria encontrar 0 na resposta, o que não é.

for i in l:
    if i < menor_valor:
        menor_valor = i

print(menor_valor)