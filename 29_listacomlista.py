carro_a = ["BMW", 50000]
carro_b = ["Ferrari", 60000]
carro_c = ["VW", 45000]

carros = [carro_a, carro_b, carro_c]

print(carros)

print(carros[0])

print(carros[0][0])

print(carros[0][1])

print(carros[2][0])

for carro in carros:
    print("A marca do carro é: %s" % carro[0])

#EXERCÍCIO lista com listas dentro e imprima cada item das listas que estão na lista pai:

produto_1 = ["Bota", "Branco", 150]
produto_2 = ["Casaco", "Preto", 300]
produto_3 = ["Camisa", "Vermelho", 60]

produtos = [produto_1, produto_2, produto_3]

print(produtos)

for item in produtos:
    #print(item) #só para verificar o que me retorna
    print("O produto é %s, cor %s e seu valor é R$ %d ." %(item[0], item[1], item[2]))