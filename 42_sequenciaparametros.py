def soma_todos(*nums):
    soma = 0
    for n in nums:
        soma += n
    return soma

s = soma_todos(5,10,20,15)

print(s)

s2 = soma_todos(1,2,3)

print(s2)

#Exercício crie uma função que recebe uma sequencia de parametros e multiplique todos eles:

def mult_todos(*numeros):
    mult = 1  #não pode ser zero senão sempre vai multiplicar por 0, zerando o resultado.
    for i in numeros:
        mult *= i
    return mult

m = mult_todos(2,3,2)

print(m)
        