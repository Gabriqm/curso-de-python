#idade = int(input("Qual é a sua idade? "))
#if idade >= 18:
#    print("Você pode entrar na balada")

#    metodo_de_pagamento = input("Como você vai pagar a entrada? ")

#    if metodo_de_pagamento == "dinheiro":
#        print("A fila do dinheiro é a número 1")
#    else:
#        print("A fila de cartão é a número 2")
#else:
#    print("Você NÃO pode entrar na balada")

x = int(input("Escreva um número: "))
print("Seu número é %d" % x)

if x > 10:
    if x > 20:
        print("O número é maior que 20")
        print(x*2)
    else:
        print("O número é menor que 20")
        print(x*5)

else:
    print("O número precisa ser maior que 10 ")