from class_produto import *
class Estoque:
    
    def __init__(self):
        self.listaProdutos = []
    
    def salvar_produtos(self):
<<<<<<< HEAD
        self.listaProdutos.append(Produto('00'+str(len(self.listaProdutos)+1),input('Nome: '),input('Fabricante: '),input('Quantidade: ')))
=======
        self.listaProdutos.append(Produto(input('Código: '),input('Nome: '),input('Fabricante: '),input('Quantidade: ')))
        if len(self.listaProdutos) > 1:
            for i in range(len(self.listaProdutos)):
                for a in range(1,len(self.listaProdutos)):
                    print(self.listaProdutos[i].cod)
                    print(self.listaProdutos[a].cod)
                    if self.listaProdutos[i].cod == self.listaProdutos[a].cod:
                        self.in_cod=input('Código já cadastrado, insira outro, por favor.\n:')
                        self.listaProdutos[a].cod=self.in_cod
                        break
                    else:
                        pass
        else:
            pass



    
>>>>>>> 139c67a479f087196bed2a44924bbcc9465fcaad
    def listar_produtos(self):
        x=input('1 - Todos.\n2 - Por Cod.\n3 - Por Nome.\n')
        if x == '1':
            self.mostrar_estoque()
        if x == '2':
            in_cod=input('Insira o código do produto.\n: ')
            for i in range(len(self.listaProdutos)):
                if self.listaProdutos[i].cod == in_cod:
                    print('Código: ', self.listaProdutos[i].cod,
                    'Nome: ', self.listaProdutos[i].nome,
                    'Fabricante: ', self.listaProdutos[i].fabricante,
                    'Quantidade: ', self.listaProdutos[i].quantidade)
                else:
                    self.mostrar_estoque()
        if x == '3':
            in_nome=input('Insira o nome do produto.\n: ')
            for i in range(len(self.listaProdutos)):
                if self.listaProdutos[i].nome == in_nome:
                    print('Código: ', self.listaProdutos[i].cod,
                    'Nome: ', self.listaProdutos[i].nome,
                    'Fabricante: ', self.listaProdutos[i].fabricante,
                    'Quantidade: ', self.listaProdutos[i].quantidade)
    def alterar_produtos(self):
        self.mostrar_estoque()
        in_cod=input('Insira o código do produto.\n: ')
        for i in range(len(self.listaProdutos)):
            if self.listaProdutos[i].cod == in_cod:
                self.listaProdutos[i].nome=input('Insira aqui o novo nome.\n: ')
    def mostrar_estoque(self):
        for i in range(len(self.listaProdutos)):
            print('Código: ', self.listaProdutos[i].cod,
            'Nome: ', self.listaProdutos[i].nome,
            'Fabricante: ', self.listaProdutos[i].fabricante,
<<<<<<< HEAD
            'Quantidade: ', self.listaProdutos[i].quantidade)
=======
            'Quantidade: ', self.listaProdutos[i].quantidade)
>>>>>>> 139c67a479f087196bed2a44924bbcc9465fcaad
