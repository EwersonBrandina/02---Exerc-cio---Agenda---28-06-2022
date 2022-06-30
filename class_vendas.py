from class_estoque import* 

class Vendas:
    def __init__(self):
        self.entrada = Estoque()
    def vender(self):
        entrada = input('Cod do Produto:  ')
        for i in range(len(self.entrada.listaProdutos)):
            if entrada == self.entrada.listaProdutos[i].cod:
                self.entrada.listaProdutos[i].quantidade -= int(input('Quantidade vendida:  '))
