from tkinter import *

import tkinter.messagebox


class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")

        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["pady"] = 15
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["pady"] = 15
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 15
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text=" ::: Exclusão de Usuarios :::")
        self.titulo["font"] = ("Arial", "12", "italic")
        self.titulo.pack()

        self.senhaLabel = Label(self.segundoContainer, text="ID ", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)
        self.senha = Entry(self.segundoContainer)
        self.senha["width"] = 20
        self.senha["font"] = self.fontePadrao
        self.senha.pack(side=LEFT)

        self.deletar = Button(self.segundoContainer)
        self.deletar["text"] = "Validar"
        self.deletar["pady"] = 1
        self.deletar["font"] = ("Arial", "10", "normal")
        self.deletar["width"] = 12
        self.deletar.pack(side=LEFT, pady=10);

        self.senhaLabel = Label(self.terceiroContainer, text="Senha : ", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)
        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 20
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.deletar = Button(self.quartoContainer)
        self.deletar["text"] = "Deletar Usuario"
        self.deletar["pady"] = 5
        self.deletar["font"] = ("Arial", "10", "normal")
        self.deletar["width"] = 12
        self.deletar.pack(side=LEFT, pady=5);
        self.deletar["command"] = self.verificaSenha

    def verificaSenha(self):


            senha = self.senha.get()

            if senha=="admin123@":

                tkinter.messagebox.showinfo(" Login Realizado com Sucesso! : ", "Seja Bem Vindo : ")

            else:
                tkinter.messagebox.showinfo("Login Invalido! ", "Usuario ou Senha Incorretos!")



root = Tk()
root.title(" ::: SIGAPEV :::: ")
root.geometry("400x300")
Application(root)
root.mainloop()