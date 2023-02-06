carro = {
    "portas": 4,
    "janelas": 5,
    "motor": 2.0,
    "teto_solar": True,
    "cambio": "Automático"
}

print(carro)

print(carro['portas'])

print(carro['cambio'])

#Exercício crie um dicionário com livros que gosta e imprima no terminal:

livros = {
    "Capitães da Areia": 300,
    "Ouça a canção do vento/Pinball 1973": 272,
    "Sul da fronteira, Oeste do Sol": 184,
    "Flores para Algernon": 316
}

for livro in livros:
    print(livro)
    print(livros[livro])
    print("O livro %s tem %d páginas." %(livro, livros[livro]))