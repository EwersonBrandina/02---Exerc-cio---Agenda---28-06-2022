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
            entrada=input(('1 - Cadastrar Fabriante\n 2 - Listar Fabricante\n3 - Cadastrar Produto\n4 - Listar Produto\n5 - Alterar Prod..: \n6 - Comprar: \n7 - Vender\n8 - Excluir Produto\n9 - Ver Movimentações\n0 - Sair\n: '))
            if entrada == '1':
                estoque.salvar_fabricantes()
            elif entrada == '2':
                estoque.listar_fabricantes()
            elif entrada == '3':
                estoque.salvar_produtos()
            elif entrada == '4':
                estoque.listar_produtos()
            elif entrada == '5':
                estoque.alterar_produtos()
            elif entrada == '6':
                compra.comprar()
            elif entrada == '7':
                venda.vender()
            elif entrada == '8':
                estoque.excluir_produtos()
            elif entrada == '9':
                compra.extrato()
            elif entrada == '0':
                print('Obrigado por acessar. Volte Sempre.')
                break
            else:
                print('Opção Invalida!!!')