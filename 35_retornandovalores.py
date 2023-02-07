def saudacao(nome):
    return "Olá %s!" %nome

sds = saudacao('Gabriel')

print(sds)

print(sds + " Tudo bem?")

def soma(a,b):
    return a + b

s = soma(5,9)
d = soma(2,3)

print(s)

print(s + 5)

print(s + d)

def profissao(nome):
    
    p = ""
    
    if nome == "Gabriel":
        p = "Programador"
    else:
        p = "Não identificado"

    return p

prof = profissao("João")

print(prof)

prof_g = profissao("Gabriel")

print(prof_g)

#Exercicio 1 função que retorna se um número é maior ou menor que 10:

def is10(x):
    n = ""
    if x > 10:
        n = "Maior que 10"
    elif x < 10:
        n = "Menor que 10"
    else:
        n = "Igual a 10"
    return n

x = is10(float(input("Digite seu número:")))

print(x)

        
#Exercício 2 funçao que recebe dado em texto se tiver mais de 20 caracteres, texto longo, se não, texto curto:

def tamanho(texto):
    resposta = ""
    if len(texto)>20:
        resposta = "Texto longo!"
    elif len(texto) < 20:
        resposta = "Texto curto!"
    else:
        resposta = "Seu texto tem 20 caracteres."
    return resposta

texto = input("Digite aqui seu texto: ")

i = tamanho(texto)

print(i)
print(len(texto))

#Exercício 3 função que recebe lista de números, retornar os pares.

def pares(lista):
    nova_lista = []

    for numero in lista:
        if numero %2 == 0:
            nova_lista.append(numero)
        
    return(nova_lista)


lista = [1,2,3,4,5,6,7,8]

lista_par = pares(lista)

print(lista_par)

lista1 = [14,17,536,7,65,876,34,342,56,765,765]

print(pares(lista1))


#Exercicio 4 crie uma lista de números e calcule a média deles:

def media_lista(list):
    i = 0

    soma = 0
    while i < len(list):
        soma = soma + list[i]
        i = i + 1
    media = soma/len(list)
    return media

list = [1,2,3,4,5,6,7,8,9,10]

q = media_lista(list)

print(q)

#Resolução do professor:

def calc_media(lista):
    media = 0
    soma = 0

    for n in lista:
        soma += n

    media = soma/len(lista)
    return media

notas = [9,8,7]

media_provas = calc_media(notas)

print(media_provas)
