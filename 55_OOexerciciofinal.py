class Mamifero:
    def __init__(self, patas, orelhas):
        self.patas = patas
        self.orelhas = orelhas
    
    def andar(self):
        print("O mamífero andou")

class Cachorro(Mamifero):
    def __init__(self, patas, orelhas, cor_do_pelo):
        super().__init__(patas,orelhas)
        self.cor_do_pelo = cor_do_pelo

    def latir(self):
        print("Au au!")


class Gato(Mamifero):
    def __init__(self, patas, orelhas, listras):
        super().__init__(patas, orelhas)
        self.listras = listras

    def miar(self):
        print("Miauuu")


ghost = Cachorro(4,2,"Branco")

ghost.andar()
ghost.latir()
print(ghost.patas)

babi = Gato(4,2,True)

babi.andar()
babi.miar()
print(babi.listras)