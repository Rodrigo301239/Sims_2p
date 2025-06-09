class Animal:
    def __init__ (self,nome_cientifico):
        self.__nome_cientifico = nome_cientifico
        
    @property
    def nome_cientifico(self):
        return self.__nome_cientifico
    
class Cachorro(Animal):
    def __init__(self,nome_cientifico,racao_favorita):
        super().__init__(nome_cientifico)
        self.racao_favorita = racao_favorita
        
    def falar(self):
        print("sou um cachorro au au")

class Gato(Animal):
    def __init__(self,nome_cientifico,tamanho_bigode):
        super().__init__(self,nome_cientifico,tamanho_bigode)
    
    def falar (self):
        print("eu sou um gato miau miau")
        
if __name__ == "__main__":
    objeto_cachorro = Cachorro("Canino","Pedigree")
    objeto_cachorro.falar()
    print("quem leu é gay")
    
    objeto_Gato = Gato ("Miau miau miau miau","whiskas")
    
    objeto_Gato.falar()        
