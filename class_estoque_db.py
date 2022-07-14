import mysql.connector
from class_fabricante import Fabricante
from class_produto import Produto

class Estoque:
    def __init__(self, msg='Segue Lista Abaixo:'): 
        self.msg = msg
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='q1w2e3',
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
        self.conexao.commit()
    #Read
    def listar(self, tabela):
        self.msg = 'Segue Lista Abaixo:'
        if tabela != 'Produtos' and tabela != 'Fabricantes':
            self.msg += f'\nTabela Inexistente'
        else:
            comando_sql = f'select * from {tabela}'
            self.meu_cursor.execute(comando_sql)
            lista = self.meu_cursor.fetchall()
            if tabela == 'produtos' or tabela == 'Produtos':
                for i in lista:
                    self.msg += f'\nCod: {i[0]}, Nome: {i[1]}, Fabr.: {i[2]}, Quant.:{i[3]}'
            elif tabela == 'fabricantes' or tabela == 'Fabricantes':
                for i in lista:
                    self.msg += f'\nCod: {i[0]}, Fabr.: {i[1]}'
    #Read All Tables
    def listar_tabelas (self):
        self.msg = 'Segue Lista Abaixo:'
        comando_sql = f'show tables;'
        self.meu_cursor.execute(comando_sql)
        lista = self.meu_cursor.fetchall()
        for i in lista:
            self.msg += f'\n Tabela: {i[0].title()}'
    #Update
    def alterar_tabela(self, tabela, atributo, valor, cod):
        if tabela == 'Produtos':
            comando_sql = f'select * from {tabela}'
            self.meu_cursor.execute(comando_sql)
            lista = self.meu_cursor.fetchall()
            x=f'show columns from Produtos'
            self.meu_cursor.execute(x)
            x = self.meu_cursor.fetchall()
            for i in range(len(x)):
                if atributo in x[i]:
                    for i in range(len(lista)):
                        cod=int(cod)
                        if cod in lista[i]:
                            comando_sql = f'update {tabela} set {atributo} = "{valor}" where id = {cod}'
                            self.meu_cursor.execute(comando_sql)
                            self.conexao.commit()
                            self.msg=f'Alteração realizada com sucesso:'
                            break
                    self.msg=f'Cod Inexistente'
            self.msg=f'Coluna Inexistente'
        elif tabela == 'Fabricantes':
            comando_sql = f'select * from {tabela}'
            self.meu_cursor.execute(comando_sql)
            lista = self.meu_cursor.fetchall()
            if atributo in lista:
                if cod in lista:
                    comando_sql = f'update {tabela} set {atributo} = "{valor}" where id = {cod}'
                    self.meu_cursor.execute(comando_sql)
                    self.conexao.commit()
                    self.msg=f'Alteração realizada com sucesso:'
        else:
            self.msg=f'Tabela Inexistente'
                    
    #Delete
    def excluir(self, tabela, cod):
        if tabela == 'Produtos' or tabela == 'Fabricantes':
            for i in range(len(lista)):
                cod=int(cod)
                if cod in lista[i]:
                    comando_sql = f'delete from {tabela} where id = {cod}'
                    self.meu_cursor.execute(comando_sql)
                    self.conexao.commit()
                    self.msg+='Exclusão Realizada'