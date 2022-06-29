from class_estoque import*
from class_compras import*

class Menu():
    def __init__(self):
        estoque = Estoque()
        compra = Compras()
        compra.entrada = estoque
        while True:
            entrada=input(('1 - Novo Cadastro\n2 - Listar Produto\n3 - Alterar Prod..: \n4 - Comprar: \n0 - Sair\n: '))
            if entrada == '1':
                estoque.salvar_produtos()
                pass
            elif entrada == '2':
                estoque.listar_produtos()
                pass
            elif entrada == '3':
                estoque.alterar_produtos()
                pass
            elif entrada == '0':
                print('Obrigado por acessar. Volte Sempre.')
                break
            elif entrada == '4':
                compra.comprar()
            else:
                print('Opção Invalida!!!')