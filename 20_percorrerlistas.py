lista = ["Maçã", "Uva", "Mamão", "Goiaba"]

i = 0

while i<4:
    print(lista[i])
    i = i + 1

#Exercício 1 loop que calcula média de 5 notas:

notas = [3,9,5,6,2]

i = 0

soma = 0

while i<5:
    soma = soma + notas[i]
    i = i + 1

media = soma/5

print("O alune teve a média %.1f em física" %media)


#Exercício 2 loop pra preencher lista com valores zerados inseridos pelo usuario:

lista = [0,0,0,0,0]

print(lista)

i = 0

while i < 5:
    lista[i] = int(input("Insira o número %d da lista: "%i))
    
#    i = i + 1

#print(lista)

