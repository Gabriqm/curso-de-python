if 10 > 5:
    verdura = "Cenoura"
    print("Entrou no if")
    print(verdura)

print("ANTES DO IF")

if 5>10:
    print("IF FALSO")

print ("DEPOIS DO IF")

nome = "Gabriel"
idade = 25

if nome == "Gabriel" and idade ==25:
    print("Olá %s" %nome)

#Exercício 1:

idade = int(input("Qual é a sua idade? "))

if idade >= 18:
    print("Pode entrar na balada!")

#Exercício 2:

rodas = int(input("Quantas rodas tem o veículo? "))

print(rodas)

if rodas >2:
    print("Você precisa pagar pedágio")

if rodas == 2:
    print("Pode passar livremente")

#Exercício 3:

x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))

print(x)
print(y)

if x > y:
    print("O número %.2f é maior que o número %.2f" %(x,y))

if y > x:
    print("O número %.2f é maior que o número %.2f" %(y,x))

if x == y:
    print("Os números são iguais.")
