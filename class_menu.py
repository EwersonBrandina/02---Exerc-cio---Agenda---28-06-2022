from class_estoque import *

class Menu():
    def __init__(self):
        estoque = Estoque()
        while True:
            entrada=input(('1 - Novo Cadastro\n2 - Listar Produto\n3 - Alterar Prod..: \n0 - Sair\n: '))
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
            else:
                print('Opção Invalida!!!')