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
        mensagensFR.columnconfigure(0, weight=1)
        mensagensFR.columnconfigure(1, weight=1)
        mensagensFR.columnconfigure(2, weight=1)
        
        # COLUMN 0
        entradasFR = tb.Frame(mensagensFR)
        entradasFR.grid(row=0, column=1, sticky='NSEW')

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
        infoFR.grid(row=0, column=2, sticky='NSEW')
        
        agenteLB = tb.Label(infoFR, text='Agente trabalhando nesse chamado',
                            font=('Segoe UI', 12))
        agenteLB.grid(row=0, column=0, sticky='W', padx=10, pady=25)
        
        # Agente responsável
        imagem= Image.open("C:/Users/ferna/sistema_chamados/imgs/usuario.jpeg").resize((50,50))
        self.usuarioIM =ImageTk.PhotoImage(imagem)
        
        usuarioLB = tb.Label(infoFR, image=self.usuarioIM, text='   Fernando Sousa', compound='left')
        usuarioLB.grid(row=1, column=0, sticky='W', padx=7)
        
        separadorST = tb.Separator(infoFR, orient='horizontal')
        separadorST.grid(row=2, sticky='EW', pady=25)
        separadorST.config(bootstyle='success')
        
        
        # Detalhes do chamado
        detalhesCS = CaixaSelecao(infoFR, row=3, column=0, text='Detalhes do chamado')
        
        tipoLB = tb.Label(detalhesCS.frame, text='Tipo de chamado')
        tipoLB.grid(row=0, column=0, sticky='W', padx=10, pady=10)
        
        statusLB = tb.Label(detalhesCS.frame, text='Status')
        statusLB.grid(row=1, column=0, sticky='W', padx=10, pady=10)
        indo_statusLB = tb.Label(detalhesCS.frame, text='Pendente', bootstyle='secondary')
        indo_statusLB.grid(row=1, column=1, sticky='W', pady=10)
        
        priopridadeLB = tb.Label(detalhesCS.frame, text='Prioridade')
        priopridadeLB.grid(row=2, column=0, sticky='W', padx=10, pady=10)
        indo_prioridadeLB = tb.Label(detalhesCS.frame, text='Média', bootstyle='secondary')
        indo_prioridadeLB.grid(row=2, column=1, sticky='W', pady=10)
        
        data_criacaoLB = tb.Label(detalhesCS.frame, text='Data de criação')
        data_criacaoLB.grid(row=3, column=0, sticky='W', padx=10, pady=10)
        dataLB = tb.Label(detalhesCS.frame, text='10/05/2023', bootstyle='secondary')
        dataLB.grid(row=3, column=1, sticky='W', pady=10)
        
        data_finalizacaoLB = tb.Label(detalhesCS.frame, text='Data de finalização')
        data_finalizacaoLB.grid(row=4, column=0, sticky='W', padx=10, pady=10)
        data_finalDE = tb.DateEntry(detalhesCS.frame, dateformat="%d/%m/%Y", bootstyle='success')
        data_finalDE.grid(row=4, column=1)
        
        #menubutton
        self.item_var = tk.StringVar()
        self.item_var.set("tipo1")
        tempoMB = tb.Menubutton(detalhesCS.frame, bootstyle='success outline', textvariable=self.item_var)
        tempoMB.grid(row=0, column=1, sticky='W', pady=10)

                
        #menu
        menu = tb.Menu(tempoMB)
        self.lista = ['tipo1', 'tipo2', 'tipo3', 'tipo4']
        for indice, item in enumerate(self.lista):
            menu.add_radiobutton(label=item, variable=self.item_var, command=lambda i=item: self.mudar_nome(i))

        tempoMB['menu'] = menu
        
    def mudar_nome(self, novo_item):
        self.item_var.set(novo_item)

        
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
        

class CaixaSelecao(tb.Menubutton):
    def __init__(self, container, row, column, **kwargs):
        super().__init__(container, **kwargs, bootstyle='info', width=38)
        
        self.row = row
        self.column = column
        self.grid(row=row, column=column)


        self.frame_visivel = False
        self.frame = tb.Frame(container)

        self.bind('<Button-1>', lambda event: self.toggle_frame())
        
    def toggle_frame(self):
        # Inverte a visibilidade do Frame
        self.frame_visivel = not self.frame_visivel
        
        if self.frame_visivel == True:
            # Se visível, mostra o Frame
            self.frame.grid(row=(self.row + 1), column=self.column, padx=10, pady=10, sticky='NSEW')
        else:
            # Se não visível, esconde o Frame
            self.frame.grid_remove()
