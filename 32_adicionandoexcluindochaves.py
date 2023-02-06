dic = {}

print(dic)

dic["nome"] = "Gabriel"

print(dic)

print(dic["nome"])

dic["sobrenome"] = "Miranda"

print(dic)

del dic["nome"]

print(dic)

#EXERCÍCIO crie um dicionario com valores e delete dois itens:

carro = {
    "pneus": 4,
    "portas": 2,
    "motor": 1,
    "janelas": 4

}

print(carro)

carro["teto solar"] = 1

print(carro)

del carro["motor"]
del carro["janelas"]

print(carro)