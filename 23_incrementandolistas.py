#lista = [0,1,2,3,4]

#lista.append(5)

#print(lista)

#nomes = ["Gabriel", "Maria Clara"]

#nomes.append("Benjamin")

#print(nomes)

#if nomes[1] != "Gabriel":
#    nomes.append("Leirbag")

#print(nomes)

#EXERCÍCIO 1 lista zerada e adicionar 5 elementos nela por input:

#lista=[]

#i = 0

#while i<5:
#    lista.append(int(input("Insira um número: ")))
#    i = i + 1

#print(lista)

#EXERCÍCIO 2 duas variaveis de listas crie uma terceira com todos os elementos das listas:

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]
l3 = []

i = 0

while i < len(l1):
    l3.append(l1[i])
    i = i + 1

j = 0

while j < len(l2):
    l3.append(l2[j])
    j = j + 1

print(l3)
