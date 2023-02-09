import random

print(random.randint(1,10)) #fornece um número aleatório em um intervalo determinado.

aleatorio = random.randint(1,1000)

print(aleatorio)

#Exercício crie um programa que gera um numero de 1 a 10, peça ao usuario para adivinhar e diga se ele acertou ou não.

x = random.randint(1,10)

y = int(input("Qual número entre 0 a 10 você acha que é?: "))

if y == x:
    print("Você acertou! O número é %d" %x)
else:
    print("Você errou, o número era %d..." %x)
