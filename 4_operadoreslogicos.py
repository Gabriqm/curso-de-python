#operador not (inverte um valor booleano)

verdadeiro = True
falso = False

print(not verdadeiro)
print(not falso)

print(not(5>2))
print(not(5<2))

#operador and (compara um booleano com outro, só retorna true se ambos forem true)

a = 5
b = 10
c = 2
d = 8

print(a>b and c>d)
print(a>b and c<d)
print(c<d and b<c)
print(a<b and b>c)

#operador or (compara um booleano com outro, só retorna false se ambos forem false)

a = 5
b = 10

print(a > b or b == 11)
print(b>a or b ==10)
print(a>b or b==10)
print(b>a or b==20)

nome = "Gabriel"
idade = 25

print(nome == "Pedro" or idade >20)

x = True
y = False
z = False

print(x and y, not x, x and x, y and y, y or x, y and z, not y, x and z)
