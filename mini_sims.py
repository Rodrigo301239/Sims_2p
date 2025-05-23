class Personagem:
    def __init__(self, nome):  # Adicionei o parâmetro nome aqui
        self.nome = nome
        self.energia = 100
        self.fome = 100
        self.higiene = 100
        self.dinheiro = 50
        self.skill = None
        self.HabSkill = 0
        self.trabalho = None
        self.mental = 100
    
    def comer(self):
        if self.dinheiro < 10:
            return f"{self.nome} não tem dinheiro para gomer"
        else:
            self.dinheiro -= 10
            self.fome = min(100, self.fome + 30)
    
    def dormir(self):
        if self.energia == 100:
            return f"{self.nome} voce não esta sonolento"
        else:
            self.energia = min (100,self.energia + 80)
            self.fome = max (0, self.fome -5)
            self.higiene = max (0, self.higiene - 30)
            self.mental = max (0, self.mental + 30)

    def trabalhar(self):
        if self.energia < 35:
            return f"{self.nome} esta sem energia para trabalhar"
        else:
            self.dinheiro += 40
            self.higiene = max (0,self.higiene - 30)

            
    def treinar(self):
        if self.HabSkill > 100:
            return f"{self.nome} já é mestre em {self.skill}"
        else:
            self.energia = max (100,self.energia - 35)
            self.fome = max (0,self.fome - 40)
            self.higiene = max (0,self.higiene - 30)
            self.mental = max (0, self.mental + 30)
    
    def mostrar_status(self):
        return f"{self.nome}\nfome: {self.fome}🍖\nEnergia: {self.energia}🔋\nmental:{self.mental}🧠\nHigiene: {self.higiene}🧻\nDinheiro: {self.dinheiro}💰"
    
    
    


    

    

if __name__ == "__main__":
    obj1 = Personagem("Salésio")
    print(obj1.nome)
    print(obj1.fome)

    obj2 = Personagem("Rodrigo")
    print(obj2.nome)
    obj2.fome = max(0, obj2.fome - 10)  
    print(obj2.fome)
    