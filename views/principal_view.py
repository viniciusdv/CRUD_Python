import tkinter as tk
import tkinter.messagebox
from tkinter.ttk import *

from views.cadastro_view import Cadastro_view

class Menu(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.criar_widgets()

    def criar_widgets(self):

        self.container_titulo = tk.Frame(self.master)
        self.container_titulo["pady"] = 10
        self.container_titulo["padx"] = 20
        self.container_titulo.pack()

        self.titulo_dados = tk.Label(self.container_titulo, text="SELECIONE A OPÇÃO DESEJADA:")
        self.titulo_dados.pack()
        self.container_usuario = tk.Frame(self.master)
        self.container_usuario["pady"] = 15
        self.container_usuario.pack()

        self.botao_usuario = tk.Button(self.container_usuario)
        self.botao_usuario["bg"] = "white"
        self.botao_usuario["text"] = "GESTÃO DE USUÁRIOS"
        self.botao_usuario["command"] = self.abrir_cadastro_usuarios
        self.botao_usuario["font"] = ("Arial", "8", "bold")
        self.botao_usuario.pack()

    def abrir_cadastro_usuarios(self):
        self.nova_tela = tk.Toplevel(self.master)
        self.cadastro_view = Cadastro_view(self.nova_tela)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Menu Principal ")
    root.geometry("400x400")
    Menu(master=root)
    root.mainloop()