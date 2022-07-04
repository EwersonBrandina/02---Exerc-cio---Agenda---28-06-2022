from class_fabricante import *
from class_produto import *


class Estoque:

    def __init__(self):
        self.listaProdutos = []
        self.listaFabricantes = []

    def salvar_produtos(self):
        if len(self.listaFabricantes) > 0:
            self.mostrar_fabricantes()
            x = input('Insira o código do fabricante de seu produto.\n: ')
            print('Agora, insira os dados do produto.')
            for i in range(len(self.listaFabricantes)):
                if self.listaFabricantes[i].cod == x:
                    self.listaProdutos.append(Produto('0-' + str(len(self.listaProdutos) + 1), input('Nome: '),
                                                      self.listaFabricantes[i].nome_frabricante))
                    break
        else:
            print('Não há Fabricante cadastrado. Cadastre-o primeiro')

    def salvar_fabricantes(self):
        self.listaFabricantes.append(Fabricante('1-' + str(len(self.listaFabricantes) + 1), input('Nome: ')))

    def listar_fabricantes(self):
        self.mostrar_fabricantes()

    def listar_produtos(self):
        x = input('1 - Todos.\n2 - Por Cod.\n3 - Por Nome.\n')
        if x == '1':
            self.mostrar_produtos()
        if x == '2':
            in_cod = input('Insira o código do produto.\n: ')
            if in_cod == '':
                self.mostrar_produtos()
            contador = 0
            for i in range(len(self.listaProdutos)):
                contador += 1
                if self.listaProdutos[i].cod == in_cod:
                    print('Código: ', self.listaProdutos[i].cod,
                          'Nome: ', self.listaProdutos[i].nome,
                          'Fabricante: ', self.listaProdutos[i].fabricante,
                          'Quantidade: ', self.listaProdutos[i].quantidade)
                    break
                elif contador == len(self.listaProdutos):
                    print('Código Errado!')
        if x == '3':
            in_nome = input('Insira o nome do produto.\n: ')
            for i in range(len(self.listaProdutos)):
                if self.listaProdutos[i].nome == in_nome:
                    print('Código: ', self.listaProdutos[i].cod,
                          'Nome: ', self.listaProdutos[i].nome,
                          'Fabricante: ', self.listaProdutos[i].fabricante,
                          'Quantidade: ', self.listaProdutos[i].quantidade)

    def alterar_fabricantes(self):
        self.mostrar_fabricantes()
        in_cod = input('Insira o código do fabricante.\n: ')
        for i in range(len(self.listaFabricantes)):
            if self.listaFabricantes[i].cod == in_cod:
                self.listaFabricantes[i].nome_frabricante = input('Insira aqui o novo nome.\n: ')
                print(self.listaFabricantes[i].nome_frabricante)

    def alterar_produtos(self):
        self.mostrar_produtos()
        in_cod = input('Insira o código do produto.\n: ')
        for i in range(len(self.listaProdutos)):
            if self.listaProdutos[i].cod == in_cod:
                self.listaProdutos[i].nome = input('Insira aqui o novo nome.\n: ')
                print(self.listaProdutos[i].nome)

    def excluir_fabricantes(self):
        self.mostrar_fabricantes()
        in_cod = input('Insira o código do produto.\n: ')
        for i in range(len(self.listaFabricantes)):
            if self.listaFabricantes[i].cod == in_cod:
                self.listaFabricantes.pop(i)
                print('Fabricante excluído com sucesso!!!')
                self.mostrar_fabricantes()
                break
            else:
                pass

    def excluir_produtos(self):
        self.mostrar_produtos()
        in_cod = input('Insira o código do produto.\n: ')
        for i in range(len(self.listaProdutos)):
            if self.listaProdutos[i].cod == in_cod:
                self.listaProdutos.pop(i)
                print('Produto excluido com sucesso!!!')
                self.mostrar_produtos()
                break
            else:
                pass

    def mostrar_produtos(self):
        print('Produtos')
        for i in range(len(self.listaProdutos)):
            print('Código: ', self.listaProdutos[i].cod,
                  'Nome: ', self.listaProdutos[i].nome,
                  'Fabricante: ', self.listaProdutos[i].fabricante,
                  'Quantidade: ', self.listaProdutos[i].quantidade)

    def mostrar_fabricantes(self):
        print('Fabricantes')
        for i in range(len(self.listaFabricantes)):
            print('Código: ', self.listaFabricantes[i].cod,
                  'Nome: ', self.listaFabricantes[i].nome_frabricante)