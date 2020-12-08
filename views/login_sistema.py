from tkinter import *

import tkinter.messagebox

from views.principal_view import Principal_view


class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 40
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] = 0
        self.quintoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text=" ::: Entre no Sistema ::::")
        self.titulo["font"] = ("Arial", "12", "italic")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer,text="Usuario : ", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
        self.nomeLabel["pady"] = 15
        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 25
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.senhaLabel = Label(self.terceiroContainer, text="Senha : ", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)
        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 25
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["pady"] = 1
        self.autenticar["font"] = ("Arial","10","normal")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()

        self.sair = Button(self.quartoContainer)
        self.sair["text"] = "Sair"
        self.sair["pady"] = 1
        self.sair["font"] = ("Arial", "10", "normal")
        self.sair["width"] = 12
        self.sair["command"] = root.quit
        self.sair.pack(side=LEFT,pady=10);


    def verificaSenha(self):

        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "admin" and senha == "admin123@":

            tkinter.messagebox.showinfo(" Login Realizado com Sucesso! : ", "Seja Bem Vindo : " +usuario)
            self.Abrir_janela_Principal

        else:
             tkinter.messagebox.showinfo("Login Invalido! ", "Usuario ou Senha Incorretos!")

        self.LimpaTela()

        self.mensagem["text"] = ""


    def LimpaTela(self):

        self.nome.delete(0,tkinter.END)
        self.senha.delete(0,tkinter.END)
        self.mensagem["text"] = ""

    def Abrir_janela_Principal(self):

        self.nova_tela = tkinter.Toplevel(self.master)
        self.principal = Principal_view(self.nova_tela)



root = Tk()
root.title(" ::: SIGAPEV :::: ")
root.geometry("300x300")
Application(root)
root.mainloop()