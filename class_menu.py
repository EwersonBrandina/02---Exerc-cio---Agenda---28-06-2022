from class_estoque_db import*

class Menu(): 
    def __init__(self):
        estoque = Estoque()
        while True:
            entrada=input(('1 - Listar Todas as Tabelas\n'
                        f'2 - Listar Tabelas Por Nomes\n'
                        f'3 - Cadastrar Fabriante\n'
                        f'4 - Cadastrar Produto\n'
                        f'5 - Alterar Atributo da Tabela\n'
                        f'6 - Comprar Produto\n'
                        f'7 - Vender Produto\n'
                        f'8 - Excluir\n'
                        f'0 - Sair\n: '))
            if entrada == '1':
                estoque.listar_tabelas()
            elif entrada == '2':
                estoque.listar_tabelas()
                tabela = input('Insira o nome da Tabela\n : ')
                estoque.listar(tabela)
            elif entrada == '3':
                cod = None
                nome = input('Insira o nome do Fabricante\n : ') 
                estoque.salvar_fabricantes(cod, nome)
            elif entrada == '4':
                cod = None
                nome = input('Insira o nome do produto\n : ')
                estoque.listar('Fabricantes')
                fabricante = input('Insira o código do fabricante\n : ')
                quantidade = 0
                estoque.salvar_produtos(cod, nome, fabricante, quantidade)
            elif entrada == '5':
                tabela=input('Insira o nome da Tabela\n : ')
                atributo=input('Insira o nome da coluna\n : ')
                valor=input('Insira a mudança\n : ')
                cod=input('Insira o id a ser alterado\n : ')
                estoque.alterar_tabela(tabela, atributo, valor, cod)
            elif entrada == '8':
                estoque.listar_tabelas()
                tabela = input('Insira o nome da Tabela\n : ')
                estoque.listar(tabela)
                cod=input('Insira o código a ser excluído\n : ')
                estoque.excluir(tabela,cod)
            elif entrada == '0':
                print('Obrigado por acessar. Volte Sempre.')
                break
            else:
                print('Opção Invalida!!!')