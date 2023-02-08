def soma(a,b):
    return a+b

def multiplicacao(a,b):
    return a*b

def operacao(a,b,f):
    resultado = f(a,b)
    return resultado

a = operacao(5,5,soma)

print(a)

b = operacao(10,5,multiplicacao)

print(b)

#EXERCICIO funcao que recebe outra como parametro, nome, idade e profissão além da funcao como argumento(esta apresenta esses dados em string dinamica).

nome = input("Digite seu nome: ")
idade = int(input("Quantos anos você tem? "))
profissao = input("Qual sua profissão? ")

def identidade(nome,idade,profissao,f):
    id = f(nome,idade,profissao)
    return id

def string(nome,idade,profissao):
    frase = "Então você é %s, tem %d anos de idade e é %s." %(nome,idade,profissao)
    return frase

print(identidade(nome,idade,profissao,string))