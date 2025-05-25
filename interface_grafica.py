import tkinter as tk
from mini_sims import Personagem

class SimsApp:
    def __init__(self, root):
        self.personagem = Personagem("Salésio")
        root.title("mini sims")
        root.geometry("500x600")

      
        self.label_status = tk.Label(root, text=self.personagem.mostrar_status(), font=("Arial", 15), pady=10, bg='white')
        self.label_status.pack(pady=20)

        self.botao_comer = tk.Button(
            root,
            text="Comer (Custa $10)",
            command=self.acao_botao_comer,
            font=("Arial", 12),
            padx=10,
            pady=5
        )
        self.botao_comer.pack(pady=10)

        self.botao_dormir = tk.Button(
            root,
            text="Dormir",
            command=self.acao_botao_dormir,
            font=("Arial", 12),
            padx=10,
            pady=5
        )
        self.botao_dormir.pack(pady=10)

        self.botao_trabalhar = tk.Button(
            root,
            text="Trabalhar",
            command=self.acao_botao_trabalhar,
            font=("Arial", 12),
            padx=10,
            pady=5
        )
        self.botao_trabalhar.pack(pady=10)

        self.label_mensagem = tk.Label(root, text="", font=("Arial", 12), bg='white')
        self.label_mensagem.pack(pady=10)


    def acao_botao_comer(self):
        mensagem = self.personagem.comer()
        self.label_mensagem.config(text=mensagem)
        self.atualizar_status()

    def acao_botao_dormir(self):
        mensagem = self.personagem.dormir()
        self.label_mensagem.config(text=mensagem)
        self.atualizar_status()

    def acao_botao_trabalhar(self):
        mensagem = self.personagem.trabalhar()
        self.label_mensagem.config(text=mensagem)
        self.atualizar_status()
    
    #def acao_botao_artes_marciais(self):


    def atualizar_status(self):
        if self.personagem.dia == 555:
            self.label_status.config(text=self.personagem.escolher_profissao())

            self.botao_comer.pack_forget()
            self.botao_dormir.pack_forget()
            self.botao_trabalhar.pack_forget()

            self.botao_continuar = tk.Button(
            root,
            text="Treinar artes marciais",
            command=self.acao_botao_artes_marciais,
            font=("Arial", 12),
            padx=10,
            pady=5
            )
            self.botao_continuar.pack(pady=10)

        else:
            self.label_status.config(text=self.personagem.mostrar_status())
        

if __name__ == "__main__":
    root = tk.Tk()
    app = SimsApp(root)
    root.mainloop()
