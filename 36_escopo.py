#O que está dentro da função é o escopo local, fora é o escopo global


escopo_global = "Tchau"  #variável global
numero = 10   #variável global

def teste():
    teste = 'Olá' #variável local
    numero = 10 #variável local
    print(teste)
    print(escopo_global)
    if numero == 10:
        print("Você ganhoU!")

teste()

escopo_global = "Até logo"
numero = 12

teste()

print(numero)

def testando():
    numero = 50
    print(numero)

testando()
teste()