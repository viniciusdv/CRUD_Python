import sqlite3


class Banco:

    def __init__(self):
        self.conexao = sqlite3.connect('../model/database.db')
        self.createTables()

    def createTables(self):
        try:
            c = self.conexao.cursor()

            c.execute("""create table if not exists usuarios (
                                 id_usuario integer primary key autoincrement,
                                 nome_usuario text not null,
                                 sexo_usuario text not null ,
                                 data_nasc_usuario text not null ,
                                 estado_civil text not null,
                                 rg_usuario text not null ,
                                 dado_identificador_usuario text  not null, 
                                 email_usuario text not null,
                                 telefone_usuario text not null ,
                                 tipo_usuario text not null)""")
            self.conexao.commit()
            print("Banco de dados iniciado com Sucesso!")
            c.close()

        except sqlite3.Error as error:
            print("Falha ao Conectar ao Banco de Dados !", error)
