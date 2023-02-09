class Carroexemplo:
    def __init__(self,marca,preco):
        self.marca = marca
        self.preco = preco

    def ligar(self):  #método/função
        print("Vrummmm")
    
    def mudar_preco(self, novo_preco):
        self.preco = novo_preco

    
polo = Carroexemplo("VW", 60000)

print(polo.marca)

polo.ligar()

polo.mudar_preco(90000)

print(polo.preco)

#Exercício crie classe carro com propriedades, crie um método que abasteça o tanque de gasolina e um método que remove gasolina por km rodado.

class Carro:
    def __init__(self, marca, valor, portas, tanque):
        self.marca = marca
        self.valor = valor
        self.portas = portas
        self.tanque = tanque

    def abastecer(self,litro):
        if self.tanque >= 100:
            print("O tanque está cheio")
        else:
            self.tanque += litro
            if self.tanque > 100:
                self.tanque = 100
        print("Você encheu o tanque com %d L de gasolina" %litro)
    
    def dirigir(self, km):
        km_por_litro = 10
        self.tanque -= (km/km_por_litro)




mobi = Carro("Fiat", 50000, 4, 50)

print(mobi.tanque)

mobi.abastecer(55)

print(mobi.tanque)

mobi.dirigir(100)

print(mobi.tanque)

mobi.abastecer(10)

print(mobi.tanque)

#EXERCÍCIO 2 criar um sistema de banco, classe deve ter método de saque, depósito e transferencia, propriedades nome, saldo e o que precisar
# realizar saques, depósitos e transferencia entre contas

class Banco:
    def __init__(self, nome_conta,saldo):
        self.nome_conta = nome_conta
        self.saldo = saldo
    
    def deposito(self, valor_deposito):
        self.saldo += valor_deposito
        print("Você depositou RS%.2f e agora seu saldo é de R$%.2f" %(valor_deposito, self.saldo))

    def saque(self, valor_saque):
        self.saldo -= valor_saque
        print("Você sacou R$%.2f e agora seu saldo é de R$%.2f" %(valor_saque, self.saldo))
    
    def transferencia(self, outra_conta, valor_transf):
        self.saldo -= valor_transf
        outra_conta.saldo += valor_transf
        print("Você transferiu R$%.2f para outra conta, agora seu saldo é R$%.2f" %(valor_transf, self.saldo))


gabriel = Banco("Gabriel Miranda", 700)

print(gabriel.saldo)

gabriel.deposito(850.24)

print(gabriel.saldo)

gabriel.saque(1000)

print(gabriel.saldo)

maria = Banco("Maria", 500)

gabriel.transferencia(maria,500)

print(maria.saldo)