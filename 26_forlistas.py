#lista = [1,2,3,4,5]

#print(lista)

#for n in lista:
#    print(n)

##diferenciando do while:

#i = 0

#while i < len(lista):
#    print(lista[i])
#    i = i + 1

#Exercício 1:

lista = [1,2,3,4,5,6,7,8,9,10]

busca = int(input("Qual numero de 1 a 10 você quer?"))

encontrado = False

for n in lista:
    if n == busca:
        print("Encontramos o número %d!" %busca)
        encontrado = True

if encontrado == False:
    print("Não encontramos seu número na lista.")