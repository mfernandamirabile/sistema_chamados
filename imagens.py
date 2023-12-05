import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

user = 'ferna'
x = (70,50)

imagem1 = Image.open(f'C:/Users/{user}/cameras/imgs/Cartao.png').resize(x)
imagem2 = Image.open(f'C:/Users/{user}/cameras/imgs/Movimento.png').resize(x)
imagem3 = Image.open(f'C:/Users/{user}/cameras/imgs/Titular.png').resize(x)
imagem4 = Image.open(f'C:/Users/{user}/cameras/imgs/Historico.png').resize(x)
imagem5 = Image.open(f'C:/Users/{user}/cameras/imgs/Estatistica.png').resize(x)