numero_texto = input("Digite um número: ")

print(numero_texto)

numero_conv=int(numero_texto)

novo_n = 7 + numero_conv

print(novo_n)

numero_extra=int(input("Digite mais um número: "))

soma = numero_conv + numero_extra

print(soma)

novo_float=float(input("Digite o que você tem de dinheiro na carteira: "))

print(novo_float)

soma_float= 100.75 + novo_float

print(soma_float)

#Exercício 1:

x = float(input("Insira o primeiro número: "))
y = float(input("Insira mais um número: "))
 = x + y

print(type(x))
print(z)

#Exercício 2:

x = float(input("Insira aqui o seu salário: "))
y = (float(input("Insira a porcentagem de aumento (em %): ")))
k = y/100

z = (x*k) + x

print("O valor do seu salário com aumento é de R$ %.2f " %z)

#Exercício 3:

base = float(input("Insira aqui a sua base: "))
potencia = float(input("Insira aqui a potência com a qual ela será elevada: "))

resultado = base**potencia

print("O resultado de %.1f na potencia %.1f é de %f" %(base,potencia,resultado))

#Exercício 4:

x = float(input("Você tem R$359,56 na sua conta bancária, quanto gostaria de depositar? "))

novo_saldo = 359.56 + x

y = float(input("A fatura do seu cartão é de R$125,98, quanto gostaria de pagar? "))

saldo_atual = novo_saldo - y

print("Seu saldo atual é de R$%.3f" %(saldo_atual))

#Erro de Conversão: Basicamente não escrever um número e sim letra quando se deve colocar um int ou float ou colocar "," ao invés de "."

