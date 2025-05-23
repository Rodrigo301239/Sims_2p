import tkinter as tk
from mini_sims import Personagem

class SimsApp:
    def __init__ (self,root):
        self.personagem = Personagem ("Salésio")
        root.title ("mini sims")
        root.geometry ("500x500")

        self.label_status = tk.Label (root, text = self.personagem.mostrar_status(), font = ("Arial", 15), pady = 10)
        self.label_status.pack()
    
    def acao_botao_comer(self):
        mensagem = self.personagem.comer()
        self.label_mensagem.config (text = mensagem)
        self.atualizar_status()

    def atualizar_status(self):
        self.label_status.config (text = self.personagem.mostrar_status())

if __name__ == "__main__":
    root = tk.Tk()
    app = SimsApp (root)
    root.mainloop()