#class Pessoa():
#    def falar(self):
#        print("Olá, pessoal!")

#class Gabriel(Pessoa):
#    def falar(self):
#        print("Olá pessoal, eu sou o Gabriel.")

#class Roberto(Pessoa):
#    pass  

#gabriel = Gabriel()

#gabriel.falar()

#roberto = Roberto()

#roberto.falar()

#EXERCÍCIO: crie classe pessoa com nome e idade, crie uma classe de super herói que herda pessoa, crie poderes especiais para o super herói e teste as duas classes criando dois novos objetos.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def falar(self):
        print("Olá, pessoal!")

class Superheroi(Pessoa):
    def __init__(self, nome, idade, superpoder):
        super().__init__(nome,idade)
        self.superpoder = superpoder

    def utilizar_super_poder(self):
        print("O herói utilizou o %s." %self.superpoder)


gabriel = Superheroi("Gabriel", 25, "Raio Laser")

gabriel.falar()
gabriel.utilizar_super_poder()

