import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from PIL import Image, ImageTk
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledFrame

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


class TelaChamado:
    def __init__(self, tela):
        self.tela = tela
        
        
        mensagensFR = tb.Frame(self.tela)
        mensagensFR.grid(row=1, sticky='NSEW')
        mensagensFR.rowconfigure(0, weight=1)
        mensagensFR.columnconfigure(0, weight=2)
        mensagensFR.columnconfigure(1, weight=1)
        
        # COLUMN 0
        entradasFR = tb.Frame(mensagensFR)
        entradasFR.grid(row=0, column=0, sticky='NSEW')

        tituloLB = tb.Label(entradasFR, 
                            text='#Solicitação de dados de pacientes com diabetes\nno Município de Codó',
                            font=('Segoe UI Semibold', 14))
        tituloLB.grid(row=0, column=0, pady=10, padx=10, sticky='W')
        espacoLB = tb.Label(entradasFR)
        espacoLB.grid(row=1, column=0)
        
        exemplo1CM = CaixaMensagem(entradasFR, row=2, column=0, height=3)
        exemplo1CM.mensagem_prefeitura(municipio='Codó', 
                                       mensagem='Solicito dados do mês de Abril sobre diabetes no município de Codó.')
        
        exemplo2CM = CaixaMensagem(entradasFR, row=4, column=0, height=7)
        exemplo2CM.mensagem_ses(mensagem='Olá,\n\nTudo bem?\n\nAté o momento, só temos os dados correspondentes até o mês de Março.\n\nPode ser ?')
        
        exemplo3CM = CaixaMensagem(entradasFR, row=6, column=0, height=3)
        exemplo3CM.mensagem_prefeitura(municipio='Codó', 
                                       mensagem='Então, possuem os dados correspondentes a...\n\n')
        
        # COLUMN 1
        infoFR = tb.Frame(mensagensFR)
        infoFR.grid(row=0, column=1, sticky='NSEW')
        
        agenteLB = tb.Label(infoFR, text='Agente trabalhando nesse chamado',
                            font=('Segoe UI', 12))
        agenteLB.grid(row=0, column=0, sticky='W', padx=10, pady=25)
        
        # Agente responsável
        imagem= Image.open("C:/Users/ferna/sistema_chamados/imgs/usuario.jpeg").resize((50,50))
        self.usuarioIM =ImageTk.PhotoImage(imagem)
        
        usuarioFR = tb.Frame(infoFR)
        usuarioFR.grid(row=1, column=0, sticky='W')
        
        usuarioLB = tb.Label(usuarioFR, image=self.usuarioIM, text='   Fernando Sousa', compound='left')
        usuarioLB.grid(row=0, column=0, sticky='W', padx=7)
        
        #nome_agenteLB = tb.Label(usuarioFR, text='Fernando Sousa',
                            #font=('Segoe UI', 10))
        #nome_agenteLB.grid(row=0, column=1, sticky='W', padx=10)
        
        separadorST = tb.Separator(infoFR, orient='horizontal')
        separadorST.grid(row=2, sticky='EW', pady=50)
        separadorST.config(bootstyle='success')
        
        
class CaixaMensagem():
    def __init__(self, container, row, column, height):
        self.container = container
        self.row = row
        self.column = column
        self.height = height
        
    def mensagem_prefeitura(self, municipio, mensagem):
        self.municipio = municipio
        self.mensagem = mensagem
            
        prefeituraLB = tb.Label(self.container, text=f'Prefeitura de {self.municipio}',
                                font=('Segoe UI', 10),
                                bootstyle='dark')
        prefeituraLB.grid(row=self.row, column=self.column, sticky='W', padx=11)
            
        msg = mensagem
        
        text = tk.Text(self.container, wrap='word', height=self.height)
        text.grid(row=(self.row + 1), column=self.column, sticky='W', padx=10, pady=10)
        text.insert('1.0', msg)
            
    def mensagem_ses(self, mensagem):
        self.mensagem = mensagem
            
        sesLB = tb.Label(self.container, text='Secretaria de Saúde',
                                font=('Segoe UI', 10),
                                bootstyle='dark')
        sesLB.grid(row=self.row, column=self.column, sticky='W', padx=11)
            
        msg = mensagem
        
        text = tk.Text(self.container, wrap='word', height=self.height)
        text.grid(row=(self.row + 1), column=self.column, sticky='W', padx=10, pady=10)
        text.insert('1.0', msg)
        

        