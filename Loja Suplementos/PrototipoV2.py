#Importações
from tkinter import *

produtos = ["Whey Protein","BCAA","Creatina","Multivitaminico","Cafeina"]
precoProdutos = ["R$100,00","R$50,00","R$5,00","R$50,00","R$150,00"]

#configurações da janela
janela = Tk()
janela.title("Loja de Suplementos")
janela.geometry("750x510+230+70")

titulo = Label(
    janela,
    text="Loja suplementos",
    font=("arial", 40),
    fg="black",
    relief="solid"
)

#carrinho
def carrinhoCompras():
    carrinhoJanela = Toplevel(janela)
    carrinhoJanela.title("Carrinho de compras")
    carrinhoJanela.geometry("500x350+430+250")
    carrinhoJanela.resizable(False, False)

    carrinhoItens = Text(carrinhoJanela,font="arial, 13",width=59,height=14)
    carrinhovalor = 0

    carrinhoItens.insert(INSERT,"Itens do Carrinho: \n")
    Label(carrinhoJanela,text="Valor Total: ",font="Arial, 12").place(x=25,y=300)
    valorTotal = Label(carrinhoJanela,text="R$00,00",font="arial,12",bg="green")

    valorTotal.place(x=110,y=300)
    carrinhoItens.place(x=10,y=10)

carrinhoImg = PhotoImage(file="Loja Suplementos/Imagens/carrinho.png")
carrinho = Button(janela,image=carrinhoImg,command=carrinhoCompras)

#produtos
whey = Label(janela,text="Whey Protein", font="arial, 20")
wheyPreco = Label(
    janela,
    text=precoProdutos[0],
    font=("arial", 20),
    bg="green",
    width=8
)
wheyComprar = Button(janela,text="COMPRAR")

#local dos objetos
titulo.place(x=165, y=0)
whey.place(x=50,y=120)
wheyPreco.place(x=50,y=230)
wheyComprar.place(x=80,y=270)
carrinho.place(x=650,y=1)

#mantem a janela aberta
janela.mainloop()
