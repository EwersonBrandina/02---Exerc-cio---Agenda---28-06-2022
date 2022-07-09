import mysql.connector
from class_fabricante import Fabricante
from class_produto import Produto


class Estoque:

    def __init__(self): 
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='92337155Thule03@1',
            database='estoque'
        )
        self.meu_cursor = self.conexao.cursor()
        
    #Create
    def salvar_fabricantes(self, cod, nome):
        obj_fabricante = Fabricante(cod, nome)
        comando_sql = f'insert into Fabricantes (nome) value ("{obj_fabricante.nome}")'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()
    def salvar_produtos(self, cod, nome, fabricante, quantidade):
        obj_produto = Produto(cod, nome, fabricante, quantidade)    
        comando_sql = f'insert into Produtos (nome, fabricante, quantidade) value ("{obj_produto.nome}", (select nome from Fabricantes where id = {obj_produto.fabricante}), {obj_produto.quantidade});'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()
    #Read
    def listar(self, tabela):
        comando_sql = f'select * from {tabela}'
        self.meu_cursor.execute(comando_sql)
        lista = self.meu_cursor.fetchall()
        for i in lista:
            print(i)
    #Read All Tables
    def listar_tabelas (self):
        comando_sql = f'show tables;'
        self.meu_cursor.execute(comando_sql)
        lista = self.meu_cursor.fetchall()
        for i in lista:
            print(i)
    #Update
    def alterar_tabela(self, tabela, atributo, valor, cod):
        comando_sql = f'update {tabela} set {atributo} = "{valor}" where id = {cod}'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()
    #Delete
    def excluir(self, tabela, cod):
        comando_sql = f'delete from {tabela} where id = {cod}'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()