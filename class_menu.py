from class_estoque_db import*

class Menu(): 
    def __init__(self):
        estoque = Estoque()
        #compra = Compras()
        #compra.entrada = estoque
        #venda = Vendas()
        #venda.entrada = estoque
        while True:
            entrada=input(('1 - Cadastrar Fabriante\n2 - Listar Tabela\n3 - Cadastrar Produto\n0 - Sair\n: '))
            if entrada == '1':
                cod = None
                nome = input('Insira o nome do Fabricante\n : ') 
                estoque.salvar_fabricantes(cod, nome)
            elif entrada == '2':
                estoque.listar_tabelas()
                tabela=input('Insira o nome da Tabela\n : ')
                estoque.listar(tabela)
            elif entrada == '3':
                cod = None
                nome = input('Insira o nome do produto\n : ')
                estoque.listar('Fabricantes')
                fabricante = input('Insira o código do fabricante\n : ')
                quantidade = int(input('Qual a quantidade\n : '))
                estoque.salvar_produtos(cod, nome, fabricante, quantidade)
            #elif entrada == '4':
            #    estoque.listar_produtos()
            #elif entrada == '5':
            #    estoque.alterar_fabricantes()
            #elif entrada == '6':
            #    estoque.alterar_produtos()
            #elif entrada == '7':
            #    compra.comprar()
            #elif entrada == '8':
            #    venda.vender()
            #elif entrada == '9':
            #    estoque.excluir_fabricantes()
            #elif entrada == '10':
            #    estoque.excluir_produtos()
            #elif entrada == '11':
            #    compra.extrato()
            #elif entrada == '12':
            #    venda.extrato()
            elif entrada == '0':
                print('Obrigado por acessar. Volte Sempre.')
                break
            else:
                print('Opção Invalida!!!')