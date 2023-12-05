import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

user = 'ferna'
x = (70,50)

imagem1 = Image.open(f'C:/Users/{user}/sistema_chamados/imgs/acesso.png').resize(x)
imagem2 = Image.open(f'C:/Users/{user}/sistema_chamados/imgs/solicitacao.png').resize(x)
imagem3 = Image.open(f'C:/Users/{user}/sistema_chamados/imgs/Titular.png').resize(x)
imagem4 = Image.open(f'C:/Users/{user}/sistema_chamados/imgs/relatorio.png').resize(x)
imagem5 = Image.open(f'C:/Users/{user}/sistema_chamados/imgs/dashboard.png').resize(x)