from class_estoque import*
from class_historico import*

class Compras:
    def __init__(self):
        self.entrada = Estoque()
        self.historico = Historico()
    def comprar(self):
        entrada = input('Cod do Produto:  ')
        for i in range(len(self.entrada.listaProdutos)):
            if entrada == self.entrada.listaProdutos[i].cod:
                x=int(input('Quantidade comprada:  '))
                self.entrada.listaProdutos[i].quantidade += int(x)
                self.historico.transacoes.append(f'Compra de {x} unidades do produto:', self.entrada.listaProdutos[i].nome)
    def extrato(self):
        print(self.historico.compras_vendas())