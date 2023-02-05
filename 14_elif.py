#nome = input("Digite o seu nome: ")

#if nome == "Gabriel":
#    print("Olá, você é um admin!")
    
#    if 5>10:
#        print("Testando")
#    elif 10 > 5:
#        print("Você caiu aqui") 

#elif nome == "João":
#    print("Olá, você é um produtor de conteúdo!")
#else:
#    print("Você é um usuário comum!")


#numero = int(input("Digite um número: "))
#print(numero)

#if numero > 0 and numero <= 5:
#    print("Maior que 0")
#elif numero > 5 and numero <= 10:
#    print("Maior que 5")
#elif numero > 10 and numero <= 20:
#    print("Maior que 10")
#elif numero > 20:
#    print("Maior que 20")

#else:
#    print("Número negativo")


#Exercício 1:

#categoria = int(input("Qual a categoria do seu produto?"))

#print(categoria)

#if categoria == 1:
#    print("Seu produto é uma bolsa.")
#elif categoria == 2:
#    print("Seu produto é um tênis.")
#elif categoria == 3:
#    print("seu produto é uma mochila.")

#else:
#    print("A categoria não foi encontrada.")

#Exercício 2:

renda = int(input("Qual é a sua renda? "))

print("R$ %d" %renda)

if renda < 2000:
    print("Foi liberado R$ 1000,00 de limite.")
    limite = 1000
elif renda < 4000:
    print("Foi liberado R$ 2000,00 de limite.")
    limite = 2000
elif renda < 6000:
    print("Foi liberado R$ 3000,00 de limite.")
    limite = 3000
elif renda >= 10000:
    print("Falar com o gerente.")
    limite = 5000

print("Parabéns, seu cartão foi aprovado com R$ %d,00 de limite!" %limite)