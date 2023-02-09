class Pessoa:
    def __init__(self,nome,idade,profissao): #o self é exigência da linguagem
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

gabriel = Pessoa("Gabriel", 25, "Programador")  #instanciando um objeto

print(gabriel)

print(type(gabriel))

print(gabriel.nome)   #para acessar os valores da classe usamos o .nome/.idade/.profissao
print(gabriel.idade)
print(gabriel.profissao)

if gabriel.nome == "Gabriel":
    print("O nome é Gabriel")

nome = gabriel.nome

print(nome)


#EXERCÍCIO crie classe carro com propriedades e crie objetos preenchendo os valores das propriedades:

class Carro:
    def __init__(self, portas,motor,teto_solar,marca,preço):
        self.portas = portas
        self.motor = motor
        self.teto_solar = teto_solar
        self.marca = marca
        self.preço = preço

volks = Carro(4, 2.0, True, "Volkswagen", 150000)

print(type(volks))

print(volks.portas)
print(volks.motor)
print(volks.teto_solar)
print(volks.marca)
print(volks.preço)
