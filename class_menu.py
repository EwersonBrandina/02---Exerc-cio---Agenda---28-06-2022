from class_estoque import*
from class_compras import*
from class_vendas import*

class Menu():
    def __init__(self):
        estoque = Estoque()
        compra = Compras()
        compra.entrada = estoque
        venda = Vendas()
        venda.entrada = estoque
        while True:
            entrada=input(('1 - Cadastrar Fabriante\n'
                           '2 - Listar Fabricante\n'
                           '3 - Cadastrar Produto\n'
                           '4 - Listar Produto\n'
                           '5 - Alterar Fabricante\n'
                           '6 - Alterar Prod.:\n'
                           '7 - Comprar:\n'
                           '8 - Vender\n'
                           '9 - Excluir Fabricante\n'
                           '10 - Excluir Produto\n'
                           '11 - Ver Compras\n'
                           '12 - Ver Vendas\n'
                           '0 - Sair\n: '))
            if entrada == '1':
                estoque.salvar_fabricantes()
            elif entrada == '2':
                estoque.listar_fabricantes()
            elif entrada == '3':
                estoque.salvar_produtos()
            elif entrada == '4':
                estoque.listar_produtos()
            elif entrada == '5':
                estoque.alterar_fabricantes()
            elif entrada == '6':
                estoque.alterar_produtos()
            elif entrada == '7':
                compra.comprar()
            elif entrada == '8':
                venda.vender()
            elif entrada == '9':
                estoque.excluir_fabricantes()
            elif entrada == '10':
                estoque.excluir_produtos()
            elif entrada == '11':
                compra.extrato()
            elif entrada == '12':
                venda.extrato()
            elif entrada == '0':
                print('Obrigado por acessar. Volte Sempre.')
                break
            else:
                print('Opção Invalida!!!')