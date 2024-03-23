import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.style import Colors
from ttkbootstrap.scrolled import ScrolledFrame
from imagens import *
from dashboard import *
from chamados import *
import random




class TelaPadrao:
    def __init__(self):
        self.rootPadrao = tb.Window(themename='flatly')
        self.rootPadrao.title('Sistema de Chamados')
        self.rootPadrao.state('zoomed')
        self.rootPadrao.columnconfigure(0, weight=1)

        
        # CABEÇALHO
        # Logo
        imagem = Image.open("C:/Users/ferna/sistema_chamados/imgs/logo_maranhao.png").resize((130,40))
        logoIM =ImageTk.PhotoImage(imagem)
        
        # Frame Pirncipal
        self.notebook = tb.Notebook(self.rootPadrao)
        self.notebook.grid(sticky='NSEW', pady=10, padx=7, row=0)
        self.notebook.config(height=925)
        
        rootFR = tb.Frame(self.notebook)
        rootFR.columnconfigure(0, weight=1)
        rootFR.columnconfigure(1, weight=4)
        rootFR.rowconfigure(2, weight=1)
        rootFR.config(height=800)
        rootFR.grid(row=0, column=0, sticky='NSEW')
        
        self.notebook.add(rootFR, image=logoIM)
        
        # Abas
        self.dashboardAB = Aba(TelaDashboard, self.notebook)
        self.chamadosAB = Aba(TelaChamado, self.notebook)
        
        
        # COLUMN 0
        opcoesFR = tb.Labelframe(rootFR, text='Chamados', bootstyle='dark')
        opcoesFR.grid(column=0, row=2, sticky='NSEW', padx=20, pady=50)
        opcoesFR.columnconfigure(0, weight=1)
        opcoesFR.rowconfigure(0, weight=1)
        opcoesFR.rowconfigure(1, weight=4)
        
        treeviewFR = tb.Frame(opcoesFR)
        treeviewFR.grid(row=0)
        
        #Chamados
        colunas = ('numero', 'data_abertura', 'prioridade', 'status')
        self.chamadosTW = tb.Treeview(treeviewFR, bootstyle='success', columns=colunas, show='headings')
        self.chamadosTW.grid(sticky='EW')
        
        self.chamadosTW.heading('numero', text='Número')
        self.chamadosTW.heading('data_abertura', text='Data de Abertura')
        #chamadosTW.heading('responsavel', text='Responsável')
        self.chamadosTW.heading('prioridade', text='Prioridade')
        self.chamadosTW.heading('status', text='Status')
        

        numeros_chamados = [random.randint(1000000, 9999999) for _ in range(4)]
        
        self.chamadosTW.bind("<ButtonRelease-1>", self.numero_selecionado)
        
        for i, num in enumerate(numeros_chamados):
            self.chamadosTW.insert("", END, values=(f'{num}', f'1{i}/05/2023', 
                                               '     Média', '     Pendente'))
    
    


        # COLUMN 1
        # Imagens
        cartaoIM = ImageTk.PhotoImage(imagem1)
        movimentoIM = ImageTk.PhotoImage(imagem2)
        titularIM = ImageTk.PhotoImage(imagem3)
        historicoIM = ImageTk.PhotoImage(imagem4)
        dashboardIM = ImageTk.PhotoImage(imagem5)
        maisIM = ImageTk.PhotoImage(imagem6)


        # Frames
        telaFR = ScrolledFrame(rootFR)
        telaFR.grid(row=2, column=1, sticky='NSEW', padx=20, pady=10)
        telaFR.columnconfigure(0, weight=1)
        
        containerFR = tb.Frame(telaFR)
        containerFR.grid(row=0, column=0, sticky='EW')
        containerFR.columnconfigure(0, weight=1)
        botoesFR = tb.Frame(containerFR)
        botoesFR.grid(row=0, column=0, sticky='EW', padx=20)
        botoesFR.columnconfigure(0, weight=1)
        linha1FR = tb.Frame(botoesFR)
        linha1FR.grid(row=4)
        
        
        # Labels
        espaco1LB = tb.Label(botoesFR)
        espaco1LB.grid(row=0, pady=2)
        subtitulo1LB = tb.Label(botoesFR, text='Funcionalidades', bootstyle='success')
        subtitulo1LB.config(font=('Calibri', 12))
        subtitulo1LB.grid(row=1)
        espaco2LB = tb.Label(botoesFR)
        espaco2LB.grid(row=3, pady=3)
 
        linha3ST = tb.Separator(botoesFR, orient='horizontal')
        linha3ST.grid(row=2, column=0, sticky='EW', pady=2)
        linha3ST.config(bootstyle='success')


        # Botões
        criar_chmadoBT = Botao(linha1FR, image=maisIM, row=0, column=0, texto='Criar chamado')
        criar_chmadoBT.grid(padx=30)
        
        dashBT = Botao(linha1FR, image=dashboardIM, row=0, column=1, texto='Dashboards',
                       command=lambda: self.dashboardAB.abrir_aba('Dashboards'))
        dashBT.grid(padx=30)
        
        relatorioBT = Botao(linha1FR, image=historicoIM, row=0, column=2, 
                            texto='Solicitação de\n   Relatórios')
        relatorioBT.grid(padx=30)
        
        acessoFuncBT = Botao(linha1FR, image=cartaoIM, row=0, column=3, 
                            texto='  Acesso de\nFuncionários')
        acessoFuncBT.grid(padx=30)
        
        perfilBT = Botao(linha1FR, image=titularIM, row=0, column=4, 
                            texto='Configurações\n    de Perfil')
        perfilBT.grid(padx=30)
        
        dadosBT = Botao(linha1FR, image=movimentoIM, row=0, column=5, 
                            texto='Solicitação\n de Dados')
        dadosBT.grid(padx=30)

        
        self.aba_adicionada = False
        self.rootPadrao.mainloop()
        
    def numero_selecionado(self, event):
        selected_items = self.chamadosTW.selection()
        if selected_items:
            for item in selected_items:
                values = self.chamadosTW.item(item, 'values')
                numero = values[0]
            self.chamadosAB.abrir_aba(f'Chamado {numero}')
            
        
class Botao(tb.Button):
    def __init__(self, container, texto, row, column, **kwargs):
        super().__init__(container, **kwargs, style=('light', OUTLINE), padding=(15,17))

        self.row = row
        self.column = column
        self.grid(row=row, column=column)
        self.texto = texto
        self.texto = tk.StringVar
        
        botaoLB = tb.Label(container, text=texto)
        botaoLB.grid(row=(self.row + 1), column=self.column)
        

        
class Aba:
    def __init__(self, funcionalidade, notebook):
        self.aba_botoes = {}
        #self.aba_adicionada = False
        self.funcionalidade = funcionalidade
        self.notebook = notebook
        
    def abrir_aba(self, nome_aba):
        #if not self.aba_adicionada:
            #self.aba_adicionada = True
        frame = tb.Frame(self.notebook)
        frame.grid(sticky='NSEW')
        frame.columnconfigure(0, weight=1)   
        frame.rowconfigure((1), weight=1)
            
        self.notebook.add(frame, text=nome_aba)
            
        # botão de fechar aba
        fecharBT = ttk.Checkbutton(frame, text="X", command=lambda tela_cam=frame: self.fechar_aba(tela_cam), 
                                  bootstyle="light-toolbutton",
                                  padding=(5,2))
        fecharBT.grid(row=0, sticky="ne")

        self.aba_botoes[frame] = fecharBT
            
        
        # adiciona tela de funcionalidade
        self.tela = self.funcionalidade(frame)
            
    def fechar_aba(self, aba):
        indice = self.notebook.index(aba)
        if indice != -1:
            self.notebook.hide(indice)
            #self.aba_adicionada = False 


teste = TelaPadrao()