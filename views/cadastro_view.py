import tkinter as tk

from tkcalendar import DateEntry

from model.usuario import Usuario

class Cadastro_view(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.Criar_widget_usuario()
        self.usuario = Usuario("","","","","","","","","")

    def Criar_widget_usuario(self):
        # Título
        self.container_titulo = tk.Frame(self.master)
        self.container_titulo["pady"] = 10
        self.container_titulo["padx"] = 20
        self.container_titulo.pack()

        self.titulo_dados = tk.Label(self.container_titulo, text="Cadastro de Usuario")
        self.titulo_dados.pack()

        # Campo id
        self.container_id = self.criar_container_padrao()

        self.id_label = tk.Label(self.container_id, text="ID")
        self.id_label["width"] = 20
        self.id_label["anchor"] = tk.NW
        self.id_label.pack(side=tk.LEFT)

        self.id = tk.Entry(self.container_id)
        self.id["width"] = 10
        self.id.pack(side=tk.LEFT)

        self.botao_buscar = tk.Button(self.container_id)
        self.botao_buscar["text"] = "Buscar"
        self.botao_buscar["command"] = self.buscar_usuario
        self.botao_buscar.pack(side=tk.LEFT)

        # Campo nome
        self.container_nome = self.criar_container_padrao()
        self.nome_label = tk.Label(self.container_nome, text=" Nome")
        self.nome_label["width"] = 20
        self.nome_label["anchor"] = tk.NW
        self.nome_label.pack(side=tk.LEFT)
        self.nome = tk.Entry(self.container_nome)
        self.nome["width"] = 20
        self.nome.pack(side=tk.LEFT)

        # Campo nascimento
        self.container_nascimento = self.criar_container_padrao()
        self.nascimento_label = tk.Label(self.container_nascimento, text="Data de nascimento")
        self.nascimento_label["width"] = 20
        self.nascimento_label["anchor"] = tk.NW
        self.nascimento_label.pack(side=tk.LEFT)
        self.nascimento = DateEntry(self.container_nascimento, width=18, background='darkblue', foreground='white',
                                    borderwidth=2)
        self.nascimento.pack(side=tk.LEFT)

        # Campo sexo
        self.container_sexo = self.criar_container_padrao()
        self.sexo_label = tk.Label(self.container_sexo, text="Sexo")
        self.sexo_label["width"] = 20
        self.sexo_label["anchor"] = tk.NW
        self.sexo_label.pack(side=tk.LEFT)
        self.sexo = tk.StringVar(self.container_sexo)
        self.sexo.set("")  # default value
        self.sexo_combo = tk.OptionMenu(self.container_sexo, self.sexo, "Masculino", "Feminino", "")
        self.sexo_combo["width"] = 15
        self.sexo_combo.pack(side=tk.LEFT)

        # Campo Estado Civil
        self.container_estado_civil = self.criar_container_padrao()
        self.estado_civil_label = tk.Label(self.container_estado_civil, text="Estado Civil")
        self.estado_civil_label["width"] = 20
        self.estado_civil_label["anchor"] = tk.NW
        self.estado_civil_label.pack(side=tk.LEFT)
        self.estado_civil = tk.Entry(self.container_estado_civil)
        self.estado_civil["width"] = 20
        self.estado_civil.pack(side=tk.LEFT)

        # Campo RG
        self.container_rg = self.criar_container_padrao()
        self.rg_label = tk.Label(self.container_rg, text="RG")
        self.rg_label["width"] = 20
        self.rg_label["anchor"] = tk.NW
        self.rg_label.pack(side=tk.LEFT)
        self.rg = tk.Entry(self.container_rg)
        self.rg["width"] = 20
        self.rg.pack(side=tk.LEFT)

        # Campo Dado Identificador
        self.container_dado_identificador = self.criar_container_padrao()
        self.dado_identificador_label = tk.Label(self.container_dado_identificador, text="CPF\CNPJ")
        self.dado_identificador_label["width"] = 20
        self.dado_identificador_label["anchor"] = tk.NW
        self.dado_identificador_label.pack(side=tk.LEFT)
        self.dado_identificador = tk.Entry(self.container_dado_identificador)
        self.dado_identificador["width"] = 20
        self.dado_identificador.pack(side=tk.LEFT)

        # Campo Email
        self.container_email = self.criar_container_padrao()
        self.email_label = tk.Label(self.container_email, text="E-mail")
        self.email_label["width"] = 20
        self.email_label["anchor"] = tk.NW
        self.email_label.pack(side=tk.LEFT)
        self.email = tk.Entry(self.container_email)
        self.email["width"] = 20
        self.email.pack(side=tk.LEFT)

        # Campo Telefone
        self.container_telefone = self.criar_container_padrao()
        self.telefone_label = tk.Label(self.container_telefone, text="Telefone")
        self.telefone_label["width"] = 20
        self.telefone_label["anchor"] = tk.NW
        self.telefone_label.pack(side=tk.LEFT)
        self.telefone = tk.Entry(self.container_telefone)
        self.telefone["width"] = 20
        self.telefone.pack(side=tk.LEFT)

        # Campo Tipo Usuario
        self.container_tipo_usuario = self.criar_container_padrao()
        self.tipo_usuario_label = tk.Label(self.container_tipo_usuario, text="Tipo Usuario")
        self.tipo_usuario_label["width"] = 20
        self.tipo_usuario_label["anchor"] = tk.NW
        self.tipo_usuario_label.pack(side=tk.LEFT)
        self.tipo_usuario = tk.Entry(self.container_tipo_usuario)
        self.tipo_usuario["width"] = 20
        self.tipo_usuario.pack(side=tk.LEFT)


        # Botões
        self.container_botoes = self.criar_container_padrao()
        self.botao_criar = tk.Button(self.container_botoes)
        self.botao_criar["text"] = "Criar"
        self.botao_criar["command"] = self.add_usuario
        self.botao_criar["bg"] = "blue"
        self.botao_criar["fg"] = "white"
        self.botao_criar.pack(side=tk.LEFT)

        self.botao_atualizar = tk.Button(self.container_botoes)
        self.botao_atualizar["text"] = "Atualizar"
        #self.botao_atualizar["command"] = self.atualizar_funcionario
        self.botao_atualizar["bg"] = "green"
        self.botao_atualizar["fg"] = "white"
        self.botao_atualizar["state"] = "disabled"
        self.botao_atualizar.pack(side=tk.LEFT)

        self.botao_excluir = tk.Button(self.container_botoes)
        self.botao_excluir["text"] = "Excluir"
        #self.botao_excluir["command"] = self.excluir_funcionario
        self.botao_excluir["bg"] = "red"
        self.botao_excluir["fg"] = "white"
        self.botao_excluir["state"] = "disabled"
        self.botao_excluir.pack(side=tk.LEFT)

        self.botao_limpar = tk.Button(self.container_botoes)
        self.botao_limpar["text"] = "Limpar"
        #self.botao_limpar["command"] = self.limpar_tela
        self.botao_limpar.pack()

        # Mensagem
        self.container_mensagem = self.criar_container_padrao()
        self.mensagem = tk.Label(self.container_mensagem, text="")
        self.mensagem.pack()

    def add_usuario(self):
        self.usuario.set_nome(self.nome.get())
        self.usuario.set_sexo(self.sexo.get())
        self.usuario.set_data_nasc(self.nascimento.get())
        self.usuario.set_estado_civil(self.estado_civil.get())
        self.usuario.set_rg_usuario(self.rg.get())
        self.usuario.set_dado_identificador(self.dado_identificador.get())
        self.usuario.set_email(self.email.get())
        self.usuario.set_telefone_usuario(self.telefone.get())
        self.usuario.set_tipo_usuario(self.tipo_usuario.get())

        status, id_gerado, mensagem = self.usuario.insert_usuario()
        if status:
            self.id.insert(0, id_gerado)
            self.botao_criar.config(state="disabled")
            self.botao_excluir.config(state="normal")
            self.botao_atualizar.config(state="normal")

        self.mensagem["text"] = mensagem

        self.mensagem["text"] = "Novo funcionário criado!"

    def buscar_usuario(self):
        data = self.usuario.select_usuario(self.id.get())

        self.nome.delete(0, 100)
        self.nome.insert(0, data[0][1])
        self.nascimento.delete(0, 100)
        self.nascimento.insert(0, data[0][3])
        self.sexo.set(data[0][2])
        self.estado_civil.delete(0, 100)
        self.estado_civil.insert(0, data[0][4])
        self.rg.delete(0, 100)
        self.rg.insert(0, data[0][5])
        self.dado_identificador.delete(0, 100)
        self.dado_identificador.insert(0, data[0][6])
        self.email.delete(0, 100)
        self.email.insert(0, data[0][7])
        self.telefone.insert(0, 100)
        self.telefone.insert(0, data[0][8])
        self.tipo_usuario.delete(0, 100)
        self.tipo_usuario.insert(0, data[0][9])

    def criar_container_padrao(self):
        container = tk.Frame(self.master)
        container["padx"] = 20
        container["pady"] = 5
        container.pack()

        return container

