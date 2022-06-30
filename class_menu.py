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
            entrada=input(('1 - Novo Cadastro\n2 - Listar Produto\n3 - Alterar Prod..: \n4 - Comprar: \n5 - Vender\n0 - Sair\n: '))
            if entrada == '1':
                estoque.salvar_produtos()
                pass
            elif entrada == '2':
                estoque.listar_produtos()
                pass
            elif entrada == '3':
                estoque.alterar_produtos()
                pass
            elif entrada == '4':
                compra.comprar()
            elif entrada == '5':
                venda.vender()
            elif entrada == '6':
                estoque.excluir_produtos()
            elif entrada == '0':
                print('Obrigado por acessar. Volte Sempre.')
                break
            else:
                print('Opção Invalida!!!')