import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from PIL import Image, ImageTk
import ttkbootstrap as tb

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


class TelaChamado:
    def __init__(self, tela):
        self.tela = tela
        
        msg = 'Solicito dados do mês de Abril sobre diabetes no município de Codó.'
        # Criação de uma Entry desativada para a mensagem do chamado selecionado
        self.mensagem_entry = tk.Entry(self.tela, state='disabled')
        self.mensagem_entry.grid(row=1, column=0)
        self.mensagem_entry.insert(0, msg)
        