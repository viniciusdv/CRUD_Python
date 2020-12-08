import sqlite3
from model.database import Banco


class Usuario():
    __id_usuario = None
    __nome_usuario = None
    __sexo_usuario = None
    __data_nasc_usuario = None
    __estado_civil = None
    __rg_usuario = None
    __dado_dentificador_usuario = None
    __email_usuario = None
    __telefone_usuario = None
    __tipo_usuario = None
    __banco = None

    def __init__(self,nome_usuario,sexo_usuario,data_nasc_usuario,estado_civil,rg_usuario,dado_identificador_usuario,email_usuario,telefone_usuario,tipo_usuario):

        self.set_nome(nome_usuario)
        self.set_sexo(sexo_usuario)
        self.set_data_nasc(data_nasc_usuario)
        self.set_estado_civil(estado_civil)
        self.set_rg_usuario(rg_usuario)
        self.set_dado_identificador(dado_identificador_usuario)
        self.set_email(email_usuario)
        self.set_telefone_usuario(telefone_usuario)
        self.set_tipo_usuario(tipo_usuario)
        self.__banco = Banco()

    def set_id(self, id_usuario):
        self.__id_usuario = id_usuario

    def get_id(self):
        return self.__id_usuario

    def set_nome(self,nome_usuario):
        self.__nome_usuario = nome_usuario

    def get_nome(self):
        return self.__nome_usuario

    def set_sexo(self,sexo_usuario):
         self.__sexo_usuario = sexo_usuario

    def get_sexo(self):
        return self.__sexo_usuario

    def set_estado_civil(self,estado_civil):
        self.__estado_civil = estado_civil

    def get_estado_civil(self):
        return self.__estado_civil

    def set_data_nasc(self, data_nasc_usuario):
        self.__data_nasc_usuario = data_nasc_usuario

    def get_data_nasc(self):
        return self.__data_nasc_usuario

    def set_rg_usuario(self,rg_usuario):
        self.__rg_usuario = rg_usuario

    def get_rg_usuario(self):
        return self.__rg_usuario

    def set_dado_identificador(self, dado_identificador):
        self.__dado_dentificador_usuario = dado_identificador

    def get_dado_identificador(self):
        return self.__dado_dentificador_usuario

    def set_email(self, email_usuario):
        self.__email_usuario = email_usuario

    def get_email(self):
        return self.__email_usuario

    def set_telefone_usuario(self, telefone_usuario):
        self.__telefone_usuario = telefone_usuario

    def get_telefone_usuario(self):
        return self.__telefone_usuario

    def set_tipo_usuario(self, tipo_usuario):
        self.__tipo_usuario = tipo_usuario

    def get_tipo_usuario(self):
        return self.__tipo_usuario

    def insert_usuario(self):
        try:

            c = self.__banco.conexao.cursor()

            c.execute("insert into usuarios(nome_usuario, sexo_usuario, data_nasc_usuario, estado_civil, rg_usuario, dado_identificador_usuario,email_usuario,telefone_usuario,tipo_usuario) values('" + self.get_nome() + "', '" + self.get_sexo() + "', '" + str(self.get_data_nasc()) + "', '" + self.get_estado_civil() + "', '" + str(self.get_rg_usuario()) + "','" + str(self.get_dado_identificador()) + "','" + self.get_email() + "','" + str(self.get_telefone_usuario()) + "','" + self.get_tipo_usuario() + "')")


            id_gerado = c.lastrowid

            self.__banco.conexao.commit()
            c.close()

            return True, id_gerado, "Usuario Cadastro com Sucesso!"
        except sqlite3.Error as er:
            return False, 0, "Erro ao inserir Usuario!"

    def update_usuario(self):
        try:

            c = self.__banco.conexao.cursor()

            c.execute(
                "update usuarios set nome_usuario = '" + self.get_nome() + "', sexo_usuario = '" + self.get_sexo() + "', data_nasc_usuario = '" + self.get_data_nasc() + "', estado_civil = '" + self.get_estado_civil() +
                "',estado_civil'" + self.get_estado_civil() + "', rg_usuario'" + self.get_rg_usuario() + "',dado_identificador_usuario'" + self.get_dado_identificador() +  "', email_usuario'" + self.get_email() +
                "', telefone_usuario'" + self.get_telefone_usuario() + "', tipo_usuario'" + self.get_tipo_usuario()+ "' where id_usuario = " + str(
                  self.get_id()) + " ")

            self.__banco.conexao.commit()
            c.close()

            return True, "Usuario atualizado com Sucesso!"
        except sqlite3.Error as er:
            return False, "Falha ao Alterar Usuario"

    def delete_usuario(self):
        try:

            c = self.__banco.conexao.cursor()

            c.execute("delete from usuarios where id_usuario = " + str(self.get_id()) + " ")

            self.__banco.conexao.commit()
            c.close()

            return True, "Usuario Deletado com Sucesso!"
        except sqlite3.Error as er:
            return False, "Falha ao Deletar Usuario"

    def select_usuario(self, id_usuario):
        try:

            c = self.__banco.conexao.cursor()
            print("Entrou")
            c.execute("select * from usuarios where id_usuario = " + id_usuario + "  ")

            linha = c.fetchone()

            if linha is None:
                return False, "Usuario não Encontrado"
            print(linha)
            self.set_id(linha[0])
            self.set_nome(linha[1])
            self.set_sexo(linha[2])
            self.set_data_nasc(linha[3])
            self.set_estado_civil(linha[4])
            self.set_rg_usuario(linha[5])
            self.set_dado_identificador(linha[6])
            self.set_email(linha[7])
            self.set_telefone_usuario(linha[8])
            self.set_tipo_usuario(linha[9])

            print("Entrou")
            c.close()

            return linha, "Busca feita com sucesso!"
        except sqlite3.Error as er:
            return False, "Ocorreu um erro na Busca de Usuarios!"
