import random

class Personagem:
    numero = random.randint(1, 10)

    def __init__(self, nome):  
        self.nome = nome
        self.energia = 100
        self.fome = 100
        self.higiene = 100
        self.dinheiro = 50
        self.skill = None
        self.HabSkill = 0
        self.trabalho = None
        self.mental = 100
        self.dia = 0
    
    def comer(self):
        if self.dinheiro < 10:
            return f"{self.nome} não tem dinheiro para gomer"
        else:
            self.dinheiro -= 10
            self.fome = min(100, self.fome + 30)
            self.mental = min (100, self.mental + 20)
    
    def dormir(self):
        if self.energia == 100:
            return f"{self.nome} voce não esta sonolento"
        else:
            self.energia = min (100,self.energia + 80)
            self.fome = max (0, self.fome - 15)
            self.higiene = min (100, self.higiene + 20)
            self.mental = min (100, self.mental + 30)
            self.dia += 1

    def trabalhar(self):
        if self.energia < 35:
            return f"{self.nome} esta sem energia para trabalhar"

        else:
            self.dinheiro += 40
            self.higiene = max (0,self.higiene - 15)
            self.energia = max (0,self.energia - 30)
            self.mental = max (0,self.mental - 30)
            self.fome = max (0,self.fome - 40)


            
    def treinar(self,treino):
        self.skill = treino
        self.HabSkill += 1
        
        if self.HabSkill > 100:
            return f"{self.nome} já é mestre em {self.skill}"
        else:
            self.energia = max (100,self.energia - 35)
            self.fome = max (0,self.fome - 40)
            self.higiene = max (0,self.higiene - 30)
            self.mental = max (0, self.mental + 30)
    
    def mostrar_status(self):
        return f"Dia: {self.dia}\n{self.nome}\n\nfome: {self.fome}🍖\nEnergia: {self.energia}🔋\nmental:{self.mental}🧠\nHigiene: {self.higiene}🧻\nDinheiro: {self.dinheiro}💰"
    
    def escolher_profissao(self):

        return f"{self.nome} esta cansado de apenas trabalhar e dormir, escolha uma das opções: "

class Trabalho:

    def __init__(self,carreira,cargo,salarios,energia,fome,higiene,mental,saude):
        self.__carreira = carreira
        self.__cargo = cargo
        self.__salarios = salarios
        self.__energia = energia
        self.__fome = fome
        self.__higiene = higiene
        self.__mental = mental
        self.__saude = saude
    
    @property
    def informacoes (self):
        return f"Carreira: {self.__carreira}\nCargo : {self.__cargo}\nSalario : {self.__salarios}\nEnergia : {self.__energia}\nFome : {self.__fome}\nHigiene : {self.__higiene}\nMental : {self.__mental}\nSaude : {self.__saude}"
    
    @property
    def carreira (self):
        return self.__carreira
    
    def ver_cargo (self,nivel):
        return self.__cargo[nivel-1]
        
    
    
if __name__ == "__main__":
    obj1 = Personagem("Salésio")
    print(obj1.nome)
    print(obj1.fome)

    obj2 = Personagem("Rodrigo")
    print(obj2.nome)
    obj2.fome = max(0, obj2.fome - 10)  
    print(obj2.fome)
    