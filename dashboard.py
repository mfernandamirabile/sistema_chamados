import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from PIL import Image, ImageTk
import cv2
import threading
import ttkbootstrap as tb

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


class TelaDashboard:
    def __init__(self, tela):
        self.tela = tela
        
        # Frame
        telaFR = tb.Frame(self.tela)
        telaFR.grid(row=1, sticky='NSEW')
        telaFR.columnconfigure(0, weight=1)
        telaFR.columnconfigure(1, weight=4)
        telaFR.rowconfigure(0, weight=1)


        # ELEMENTO DA TELA
        
        botoesFR = tb.Labelframe(telaFR, text='xxxx')
        botoesFR.grid(row=0, column=0, sticky='NSW', padx=20, pady=10)


        self.videoFR = tk.Frame(telaFR)
        self.videoFR.grid(row=0, column=1, sticky='NSEW', padx=10)
