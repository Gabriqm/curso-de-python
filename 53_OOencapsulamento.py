class Aviao:
    __asas = 2

    def __init__(self,marca):
        self.marca = marca
    
    def mostrar_asas(self):
        print("O avião tem %d asas" %self.__asas)


aviao = Aviao("TAM")

print(aviao.marca)

aviao.mostrar_asas()