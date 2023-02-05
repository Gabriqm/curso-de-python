l = ["Sofá", "Televisão", "Rádio", "AC", "Poltrona"]

i = 0

item_procurado = input("O que deseja buscar na casa? ")
achou = False

while i < len(l):
    if l[i] == item_procurado:
        print("Encontramos um %s!" %item_procurado)
        achou = True
    i = i + 1

if achou == False:
    print("Não encontramos o %s." %item_procurado)


# EXERCÍCIO peça dois itens ao usuário e identifique o primeiro encontrado na lista:

lista = ["Notebook", "Nintendo Switch", "PS5", "Xbox", "Kindle"]

item_1 = input("O que você quer? ")
item_2 = input("Caso não tenha, qual o outro que você quer? ")

i = 0

while i < len(lista):
    if lista[i] == item_1:
        print("Encontramos o %s primeiro." %item_1)
        break
    elif lista[i] == item_2:
        print("Encontramos o %s primeiro" %item_2)
        break
    i = i + 1
