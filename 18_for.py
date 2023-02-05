palavra = "Testando"

for letra in palavra:
    print(letra)

nome = "Gabriel"

for x in nome:
    print(x)
    if x == "G":
        print ("Primeira letra do nome")

#Exercício 1:


x = int(input("Digite um número: "))

divisoes = 0

contador = x

while contador > 0:

    if x % contador == 0:
        divisoes = divisoes + 1

    contador = contador - 1

if divisoes == 2:
    print("O número %d é primo" %x)
else:
    print("O número %d não é primo" %x)

#Exercício 2:

saque = int(input("Quando dinheiro você quer? "))
print("Você quer R$ %d,00" %saque)

nota_100 = 0
nota_50 = 0
nota_20 = 0
nota_10 = 0
nota_1 = 0

while saque > 0:
    while saque >= 100:
        nota_100 = nota_100+1
        saque = saque - 100
    while saque >=50:
        nota_50 = nota_50 + 1
        saque = saque - 50
    while saque >= 20:
        nota_20 = nota_20 + 1
        saque = saque - 20
    while saque >= 10:
        nota_10 = nota_10 + 1
        saque = saque - 10
    while saque >= 1:
        nota_1 = nota_1 + 1
        saque = saque - 1



print("Você vai receber %d notas de R$100, %d notas de R$50, %d notas de R$20, %d notas de R$ 10 e %d notas de 1" % (nota_100,nota_50,nota_20, nota_10, nota_1))
