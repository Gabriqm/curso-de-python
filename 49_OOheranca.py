class Veiculo:
    def __init__(self,rodas, marca):
        self.rodas = rodas
        self.marca = marca

    def ligar(self):
        print("Vrummm!")

class carro(Veiculo):
    def __init__(self, rodas, marca, teto_solar):
        super().__init__(rodas,marca)  #mostrando que a rodas e marca são herdadas da classe pai.
        self.teto_solar = teto_solar

ferrari = carro(4, "Ferrari", True)

print(ferrari.marca)

ferrari.ligar()

print(ferrari.teto_solar)

class Moto(Veiculo):
    def __init__(self,rodas,marca,protecao_lateral):
        super().__init__(rodas,marca)
        self.protecao_lateral = protecao_lateral

    def empinar(self):
        print("Empinou a moto!")

moto = Moto(2, "Honda", False)

print(moto.rodas)

moto.empinar()