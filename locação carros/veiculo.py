
class Carro:
    def inicio (self,marca,modelo,kms,placa,cor):
        self.__marca = marca
        self.__modelo = modelo
        self.__kms = kms
        self.__placa = placa
        self.__cor = cor
        self.__esta_alugado = False

    @property
    def marca (self):
        return self.__marca
    
    @property
    def alugado(self):
        return self.__esta_alugado
    
    def exibir (self):
        print(f"carro = {self.__marca}")
        print(f"modelo = {self.__modelo}")
        print(f"kms rodados= {self.__kms}")
        print(f"placa = {self.__placa}")
        print(f"cor = {self.__cor}")

class Cliente:
    def cliente (self,nome,cpf,telefone,renda):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.renda = renda

    def exibir2(self):
        print(f"cliente = {self.nome}")
        print(f"cpf = {self.cpf}")
        print(f"telefone = {self.telefone}")
        print(f"renda = {self.renda}")

class Locacao:
    def locacao(self,nome,carro,valor,pagamento,data,quantidade):
        self.cliente = nome
        self.carro = carro
        self.valor = valor
        self.forma_pagamento = pagamento
        self.data = data
        self.quantidade = quantidade

    def exibir(self):
        print(f"cliente = {self.cliente}")
        print(f"carro = {self.carro}")
        print(f"valor = {self.valor}")
        print(f"forma de pagamento = {self.forma_pagamento}")

        if self.valor < 1200:
            print ("\n\nvoce esta pobre e nao consegue alugar")
        
        if self.carro == Carro.alugado:
            print ("o carro já esta alugado")


