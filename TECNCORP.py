import requests
from tkinter import *

janela = Tk()
janela.title("TECNCORP")
janela.geometry("800x600")

texto_orientacao = Label(janela, text ="Login")
texto_orientacao.grid(column=0, row=0, )

login_nome = Label(janela, text ="nome")
login_nome.grid(column=2, row=2 )

login_senha = Label(janela, text ="senha")
login_senha.grid(column=2, row=3,)

botao_login = Button(janela, text='Entrar', command = ())
botao_login.grid(column=3, row=4, )


janela.mainloop()