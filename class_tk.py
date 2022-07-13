from importlib.metadata import entry_points
from tkinter import *

from mysqlx import Row
from class_estoque_db import *

estoque = Estoque()
opcoes = [
'Listar Todas as Tabelas',
'Listar Tabelas Por Nomes',
'Cadastrar Fabriante',
'Cadastrar Produto',
'Alterar Atributo da Tabela',
'Comprar Produto',
'Vender Produto',
'Excluir',
'Sair'
]

root = Tk()
altura = root.winfo_screenheight()
largura = root.winfo_screenwidth()
root.geometry('750x470')
root.config(background='#b05193')
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
#Funções
#Escolha de Opção no Menu
def escolha():
    if variable.get() == opcoes[0]: #Listar Todas as Tabelas
        fr0.grid_remove(), fr1.grid(row=0, column=0)
        lb1['text']=estoque.listar_tabelas()
    elif variable.get() == opcoes[1]: #Listar Tabelas Por Nomes
        fr0.grid_remove(), fr2.grid(row=0, column=0)
        lb2_0['text']=estoque.listar_tabelas()
    elif variable.get() == opcoes[2]: #Cadastrar Fabriante
        fr0.grid_remove(), fr3.grid(row=0, column=0)
    elif variable.get() == opcoes[3]:
        fr0.grid_remove(), fr4.grid(row=0, column=0)
    elif variable.get() == opcoes[4]:
        fr0.grid_remove(), fr5.grid(row=0, column=0)
    elif variable.get() == opcoes[5]:
        fr0.grid_remove(), fr6.grid(row=0, column=0)
    elif variable.get() == opcoes[6]:
        fr0.grid_remove(), fr7.grid(row=0, column=0)
    elif variable.get() == opcoes[7]:
        fr0.grid_remove(), fr8.grid(row=0, column=0)
    elif variable.get() == opcoes[8]:
        fr0.grid_remove(), fr9.grid(row=0, column=0)
#Escolha de Qual Tabela Olhar:
def escolha1():
    lb2_1_0['text']=estoque.listar(in2_1.get())
#Cadastro do Fabricante:
def cadastro1():
    cod=None
    nome=in3_0.get()
    estoque.salvar_fabricantes(cod,nome)
#Cadastro dos Produtos:
def cadastro2():
    cod=None
    nome=in4_0.get()
    fabricante=in4_1.get()
    quantidade=0
    estoque.salvar_produtos(cod, nome, fabricante, quantidade)
def alterar1():
    tabela=in5_0.get()
    atributo=in5_1.get()
    valor=in5_2.get()
    cod=in5_3.get()
    estoque.alterar_tabela(tabela, atributo, valor, cod)
def excluir1():
    tabela=in8_0.get()
    cod=in8_1.get()
    estoque.excluir(tabela,cod)
#Frame0
fr0 = LabelFrame(root, bg= '#b05193')
fr0.grid(row=0,column=0)
lb0 = Label(fr0, text='Escolha Uma Opção Abaixo', font='Arial 25', fg='#18ab4e', bg='#2b2d94').grid(row=0, column=0, sticky=S)
variable = StringVar(fr0)
variable.set(opcoes[0])
opc0 = OptionMenu(fr0, variable, *opcoes).grid(row=1,column=0)
bt0 = Button(fr0, text='Confirmar', font='Arial 25', fg='#18ab4e', bg='#2b2d94', command= lambda: escolha()).grid(row=2,column=0, sticky=N)
#Frame1 - Listar Todas as Tabelas
fr1 = LabelFrame(root, bg= '#b05193')
lb1= Label(fr1, text='', font='Arial 25', fg='#18ab4e', bg='#2b2d94')
lb1.grid()
#Frame2 - Listar Tabelas Por Nomes
fr2 = LabelFrame(root, bg= '#b05193')
lb2_0=Label(fr2, text='', font='Arial 25', fg='#18ab4e', bg='#2b2d94')
lb2_0.grid(row=0, column=0, columnspan=2)
lb2_1= Label(fr2, text='Insira o Nome da Tabela: ', font='Arial 25', fg='#18ab4e', bg='#2b2d94')
lb2_1.grid(row=1, column=0)
in2_1 = Entry(fr2, font='Arial 25', fg='#18ab4e', bg='#2b2d94')
in2_1.grid(row=1, column=1)
bt2_3 = Button(fr2, text='Confirmar', font='Arial 25', fg='#18ab4e', bg='#2b2d94', command= lambda: [escolha1(), fr2.grid_remove(), fr2_1.grid()])
bt2_3.grid(row=2, column=0, columnspan=2)
#Frame2_1 - Nomes dos Atributos da Tabela Selecionada
fr2_1 = LabelFrame(root, bg='#b05193')
lb2_1_0=Label(fr2_1, text='', font='Arial 25', fg='#18ab4e', bg='#2b2d94')
lb2_1_0.grid()
#Frame3 - Cadastrar Fabriante
fr3 = LabelFrame(root, bg= '#b05193')
lb3_0 = Label(fr3, text='Insira o Nome do Fabricante:', font='Arial 25', fg='#18ab4e', bg='#2b2d94')
lb3_0.grid(row=0, column=0)
in3_0 = Entry(fr3, font='Arial 25', fg='#18ab4e', bg='#2b2d94')
in3_0.grid(row=0,column=1)
bt3_1 = Button(fr3, text='Confirmar', font='Arial 25', fg='#18ab4e', bg='#2b2d94', command= lambda: [cadastro1(), in3_0.delete(0,'end')])
bt3_1.grid(row=1, column=0, columnspan=2)
#Frame4 - Cadastrar Produto
fr4 = LabelFrame(root, bg= '#b05193')
lb4_0= Label(fr4, text='Insira o Nome do Produto:', font='Arial 25', fg='#18ab4e', bg='#2b2d94')
lb4_0.grid(row=0, column=0)
in4_0 = Entry(fr4, font='Arial 25', fg='#18ab4e', bg='#2b2d94')
in4_0.grid(row=0, column=1)
lb4_1= Label(fr4, text='Insira o Cod. do Fabricante:', font='Arial 25', fg='#18ab4e', bg='#2b2d94')
lb4_1.grid(row=1, column=0)
in4_1 = Entry(fr4, font='Arial 25', fg='#18ab4e', bg='#2b2d94')
in4_1.grid(row=1,column=1)
bt4_2 = Button(fr4, text='Confirmar', font='Arial 25', fg='#18ab4e', bg='#2b2d94', command= lambda: [cadastro2(), in4_0.delete(0,'end'), in4_1.delete(0,'end')])
bt4_2.grid(row=2, column=0, columnspan=2) 
#Frame5 - Alterar Atributo da Tabela
fr5 = LabelFrame(root, bg= '#b05193')
lb5_0 = Label(fr5, text='Nome da Tabela: ', font='Arial 25', fg='#18ab4e', bg='#2b2d94')
lb5_0.grid(row=0, column=0)
in5_0 = Entry(fr5, font='Arial 25', fg='#18ab4e', bg='#2b2d94')
in5_0.grid(row=0, column=1)
lb5_1 = Label(fr5, text='Nome do Atributo: ', font='Arial 25', fg='#18ab4e', bg='#2b2d94')
lb5_1.grid(row=1, column=0)
in5_1 = Entry(fr5, font='Arial 25', fg='#18ab4e', bg='#2b2d94')
in5_1.grid(row=1, column=1)
lb5_2 = Label(fr5, text='Valor a substituir: ', font='Arial 25', fg='#18ab4e', bg='#2b2d94')
lb5_2.grid(row=2, column=0)
in5_2 = Entry(fr5, font='Arial 25', fg='#18ab4e', bg='#2b2d94')
in5_2.grid(row=2, column=1)
lb5_3 = Label(fr5, text='Cod. da Linha a Substituir: ', font='Arial 25', fg='#18ab4e', bg='#2b2d94')
lb5_3.grid(row=3, column=0)
in5_3 = Entry(fr5, font='Arial 25', fg='#18ab4e', bg='#2b2d94')
in5_3.grid(row=3, column=1)
bt5_4 = Button(fr5, text='Confirmar', font='Arial 25', fg='#18ab4e', bg='#2b2d94', command= lambda: [alterar1(),in5_0.delete(0,'end'),in5_1.delete(0,'end'),in5_2.delete(0,'end'),in5_3.delete(0,'end'),in5_4.delete(0,'end')])
bt5_4.grid(row=4, column=0, columnspan=2)
#Frame6 - Comprar Produto
fr6 = LabelFrame(root, bg= '#b05193')
lb6= Label(fr6, text='Teste6', font='Arial 25', fg='#18ab4e', bg='#2b2d94')
lb6.grid()
#Frame7 - Vender Produto
fr7 = LabelFrame(root, bg= '#b05193')
lb7= Label(fr7, text='Teste7', font='Arial 25', fg='#18ab4e', bg='#2b2d94')
lb7.grid()
#Frame8 - Excluir
fr8 = LabelFrame(root, bg= '#b05193')
lb8_0 = Label(fr8, text='Insira o Nome da Tabela:', font='Arial 25', fg='#18ab4e', bg='#2b2d94')
lb8_0.grid(row=0, column=0)
in8_0 = Entry(fr8, font='Arial 25', fg='#18ab4e', bg='#2b2d94')
in8_0.grid(row=0, column=1)
lb8_1 = Label(fr8, text='Insira o Cod a Excluir:', font='Arial 25', fg='#18ab4e', bg='#2b2d94')
lb8_1.grid(row=1, column=0)
in8_1 = Entry(fr8, font='Arial 25', fg='#18ab4e', bg='#2b2d94')
in8_1.grid(row=1, column=1)
bt8_2 = Button(fr8, text='Confirmar', font='Arial 25', fg='#18ab4e', bg='#2b2d94', command= lambda: [excluir1(), in8_0.delete(0,'end'),in8_1.delete(0,'end'), alterar1()])
bt8_2.grid(row=2, column=0, columnspan=2)
#Frame9 - Sair
fr9 = LabelFrame(root, bg= '#b05193')
lb9= Label(fr9, text='Teste9', font='Arial 25', fg='#18ab4e', bg='#2b2d94')
lb9.grid()









root.mainloop()
