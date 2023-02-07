def digaOi(nome):
    print("Olá %s!" %nome)

digaOi("Gabriel")

digaOi("Maria")

if 10>5:
    digaOi("Zé")


#função sem parâmetro:

def digaOla():
    print("Olá Mundo!")

digaOla()

#Exercício funcao que multiplica dois números:

def multiplicacao(x,y):
    z = x*y
    print(z)

x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))

multiplicacao(x,y)

