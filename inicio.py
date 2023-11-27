import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.style import Colors
from ttkbootstrap.scrolled import ScrolledFrame
from imagens import *
from interface import *




class TelaPadrao:
    def __init__(self):
        self.rootPadrao = tb.Window(themename='morph')
        self.rootPadrao.title('Sistema de Chamados')
        self.rootPadrao.state('zoomed')
        #self.rootPadrao.rowconfigure(0, weight=1)
        self.rootPadrao.columnconfigure(0, weight=1)
        
        #self.rootPadrao.rowconfigure(3, weight=1)
        
        
        
        # CABEÇALHO
        # Logo
        imagem1= Image.open("sis_logo.png").resize((45,35))
        logoIM =ImageTk.PhotoImage(imagem1)
        
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
        
        # COLUMN 0
        opcoesFR = tb.Labelframe(rootFR, text='Menu')
        opcoesFR.grid(column=0, row=2, sticky='NSEW', padx=20, pady=50)
        opcoesFR.columnconfigure(0, weight=1)
        #opcoesFR.rowconfigure(0, weight=1)
        #opcoesFR.columnconfigure(1, weight=1)
        chamadosLB = tb.Checkbutton(opcoesFR, bootstyle='default-toolbutton', text='Visualizar Chamados')
        chamadosLB.grid(row=0, column=0, sticky='NEW', pady=5)
        
        criarLB = tb.Checkbutton(opcoesFR, bootstyle='default-toolbutton', text='Criar Chamados')
        criarLB.grid(row=1, column=0, sticky='NEW')
        #criarLB.config(font=('Calibri', 12))
    


        # COLUMN 1
        # Imagens
        cameraIM = ImageTk.PhotoImage(imagem2)
        mapaIM = ImageTk.PhotoImage(imagem3)
        alarmeIM = ImageTk.PhotoImage(imagem4)
        remotoIM = ImageTk.PhotoImage(imagem5)
        cartaoIM = ImageTk.PhotoImage(imagem6)
        credencialIM = ImageTk.PhotoImage(imagem7)
        visitanteIM = ImageTk.PhotoImage(imagem8)
        pessoaIM = ImageTk.PhotoImage(imagem9)
        procuradoIM = ImageTk.PhotoImage(imagem10)
        repositorioIM = ImageTk.PhotoImage(imagem11)
        marcadorIM = ImageTk.PhotoImage(imagem12)
        movimentoIM = ImageTk.PhotoImage(imagem13)
        eventoIM = ImageTk.PhotoImage(imagem14)
        exploradorIM = ImageTk.PhotoImage(imagem15)
        buscaIM = ImageTk.PhotoImage(imagem16)
        areaIM = ImageTk.PhotoImage(imagem17)
        portaIM = ImageTk.PhotoImage(imagem18)
        titularIM = ImageTk.PhotoImage(imagem19)
        atVisitanteIM = ImageTk.PhotoImage(imagem20)
        presencaIM = ImageTk.PhotoImage(imagem21)
        horaIM = ImageTk.PhotoImage(imagem22)
        atCredencialIM = ImageTk.PhotoImage(imagem23)
        historicoIM = ImageTk.PhotoImage(imagem24)
        elevadorIM = ImageTk.PhotoImage(imagem25)
        visitaIM = ImageTk.PhotoImage(imagem26)
        alertaIM = ImageTk.PhotoImage(imagem27)
        alertaMultiIM = ImageTk.PhotoImage(imagem28)
        leituraIM = ImageTk.PhotoImage(imagem29)
        statusIM = ImageTk.PhotoImage(imagem30)
        auditoriaIM = ImageTk.PhotoImage(imagem31)
        estatisticaIM = ImageTk.PhotoImage(imagem32)


        # Frames
        telaFR = ScrolledFrame(rootFR)
        telaFR.grid(row=2, column=1, sticky='NSEW', padx=10, pady=10)
        
        #for child in telaFR.winfo_children():
            #child.configure(bg='#444444')

        #Operação
        operacaoFR = tb.Frame(telaFR)
        operacaoFR.grid(row=0, sticky='EW')
        operacaoFR.columnconfigure(0, weight=1)
        op_linha1FR = tb.Frame(operacaoFR)
        op_linha1FR.grid(row=4, sticky='EW')
        

        #Investigação
        investigacaoFR = tb.Frame(telaFR)
        investigacaoFR.grid(row=1, sticky='EW')
        investigacaoFR.columnconfigure(0, weight=1)
        in_linha1FR = tb.Frame(investigacaoFR)
        in_linha1FR.grid(row=4, sticky='EW')
        in_linha2FR = tb.Frame(investigacaoFR)
        in_linha2FR.grid(row=5, pady=20, sticky='EW')
        in_linha3FR = tb.Frame(investigacaoFR)
        in_linha3FR.grid(row=6, sticky='EW')

        #Manutenção
        mautencaoFR = tb.Frame(telaFR)
        mautencaoFR.grid(row=2, sticky='EW')
        mautencaoFR.columnconfigure(0, weight=1)
        mn_linha1FR = tb.Frame(mautencaoFR)
        mn_linha1FR.grid(row=4, sticky='EW')
        
        
        
        
        # Labels
        #Operação
        op_espaco1LB = tb.Label(operacaoFR)
        op_espaco1LB.grid(row=0, pady=2)
        subtitulo1LB = tb.Label(operacaoFR, text='xxxx', bootstyle='success')
        subtitulo1LB.config(font=('Calibri', 12))
        subtitulo1LB.grid(row=1)
        op_espaco2LB = tb.Label(operacaoFR)
        op_espaco2LB.grid(row=3, pady=3)
 
        linha3ST = tb.Separator(operacaoFR, orient='horizontal')
        linha3ST.grid(row=2, sticky='EW', pady=2)
        linha3ST.config(bootstyle='success')

        #Investigação
        in_espaco1LB = tb.Label(investigacaoFR)
        in_espaco1LB.grid(row=0)
        subtitulo2LB = tb.Label(investigacaoFR, text='xxxx', bootstyle='success')
        subtitulo2LB.config(font=('Calibri', 12))
        subtitulo2LB.grid(row=1)
        in_espaco2LB = tb.Label(investigacaoFR)
        in_espaco2LB.grid(row=3, pady=3)

        linha4ST = tb.Separator(investigacaoFR, orient='horizontal')
        linha4ST.grid(row=2, sticky='EW', pady=2)
        linha4ST.config(bootstyle='success')

        #Manutenção
        mn_espaco1LB = tb.Label(mautencaoFR)
        mn_espaco1LB.grid(row=0) 
        subtitulo3LB = tb.Label(mautencaoFR, text='xxxx', bootstyle='success')
        subtitulo3LB.config(font=('Calibri', 12))
        subtitulo3LB.grid(row=1)
        mn_espaco2LB = tb.Label(mautencaoFR)
        mn_espaco2LB.grid(row=3, pady=3)

        linha5ST = tb.Separator(mautencaoFR, orient='horizontal')
        linha5ST.grid(row=2, sticky='EW', pady=5)
        linha5ST.config(bootstyle='success')



        # Botões
        #Operação
        
        camerasBT = tb.Button(op_linha1FR, image=cameraIM, padding=(15,17), style=('light', OUTLINE), 
                              command=lambda: self.iniciar_telaCameras())
        camerasBT.grid(row=0, column=0)
        camerasLB = tb.Label(op_linha1FR, text='xxxx')
        camerasLB.grid(row=1,column=0)
        
        mapasBT = tb.Button(op_linha1FR, image=mapaIM, padding=(15,17), style=('light', OUTLINE))
        mapasBT.grid(row=0, column=1, padx=30)
        mapasLB = tb.Label(op_linha1FR, text='xxxx')
        mapasLB.grid(row=1, column=1)
        
        alarmesBT = tb.Button(op_linha1FR, image=alarmeIM, padding=(15,17), style=('light', OUTLINE))
        alarmesBT.grid(row=0, column=2, padx=10)
        alarmesLB = tb.Label(op_linha1FR, text='xxxx')
        alarmesLB.grid(row=1,column=2)

        remotoBT = tb.Button(op_linha1FR, image=remotoIM, padding=(15,17), style=('light', OUTLINE))
        remotoBT.grid(row=0, column=3, padx=30)
        remotoLB = tb.Label(op_linha1FR, text='xxxx')
        remotoLB.grid(row=1, column=3)

        cartaoBT = tb.Button(op_linha1FR, image=cartaoIM, padding=(15,17), style=('light', OUTLINE))
        cartaoBT.grid(row=0, column=4, padx=15)
        cartaoLB = tb.Label(op_linha1FR, text='xxxx')
        cartaoLB.grid(row=1, column=4)

        credenciaisBT = tb.Button(op_linha1FR, image=credencialIM, padding=(15,17), style=('light', OUTLINE))
        credenciaisBT.grid(row=0, column=5, padx=25)
        credenciaisLB = tb.Label(op_linha1FR, text='xxxx')
        credenciaisLB.grid(row=1, column=5)

        visitantesBT = tb.Button(op_linha1FR, image=visitanteIM, padding=(15,17), style=('light', OUTLINE))
        visitantesBT.grid(row=0, column=6, padx=10)
        visitantesLB = tb.Label(op_linha1FR, text='xxxx')
        visitantesLB.grid(row=1, column=6)

        pessoasBT = tb.Button(op_linha1FR, image=pessoaIM, padding=(15,17), style=('light', OUTLINE))
        pessoasBT.grid(row=0, column=7, padx=30)
        pessoasLB = tb.Label(op_linha1FR, text='xxxx')
        pessoasLB.grid(row=1, column=7)

        procuradosBT = tb.Button(op_linha1FR, image=procuradoIM, padding=(15,17),style=('light', OUTLINE))
        procuradosBT.grid(row=0, column=8)
        procuradosLB = tb.Label(op_linha1FR, text='xxxx')
        procuradosLB.grid(row=1, column=8)

        #Investigação
        repositoriosBT = tb.Button(in_linha1FR, image=repositorioIM, padding=(15,17), style=('light', OUTLINE))
        repositoriosBT.grid(row=0, column=0)
        repositoriosLB = tb.Label(in_linha1FR, text='xxxx')
        repositoriosLB.grid(row=1, column=0)
        
        eventosBT = tb.Button(in_linha1FR, image=eventoIM, padding=(15,17), style=('light', OUTLINE))
        eventosBT.grid(row=0, column=1, padx=30)
        eventosLB = tb.Label(in_linha1FR, text='xxxx')
        eventosLB.grid(row=1, column=1)

        exploradorBT = tb.Button(in_linha1FR, image=exploradorIM, padding=(15,17), style=('light', OUTLINE))
        exploradorBT.grid(row=0, column=2, padx=10)
        exploradorLB = tb.Label(in_linha1FR, text='xxxx')
        exploradorLB.grid(row=1, column=2)

        marcadoresBT = tb.Button(in_linha1FR, image=marcadorIM, padding=(15,17), style=('light', OUTLINE))
        marcadoresBT.grid(row=0, column=3, padx=30)
        marcadoresLB = tb.Label(in_linha1FR, text='xxxx')
        marcadoresLB.grid(row=1, column=3)

        movimentosBT = tb.Button(in_linha1FR, image=movimentoIM, padding=(15,17), style=('light', OUTLINE))
        movimentosBT.grid(row=0, column=4, padx=15)
        movimentosLB = tb.Label(in_linha1FR, text='xxxx')
        movimentosLB.grid(row=1, column=4)

        buscaBT = tb.Button(in_linha1FR, image=buscaIM, padding=(15,17), style=('light', OUTLINE))
        buscaBT.grid(row=0, column=5, padx=25)
        buscaLB = tb.Label(in_linha1FR, text='xxxx')
        buscaLB.grid(row=1, column=5)

        areaBT = tb.Button(in_linha1FR, image=areaIM, padding=(15,17), style=('light', OUTLINE))
        areaBT.grid(row=0, column=6, padx=12)
        areaLB = tb.Label(in_linha1FR, text='xxxx')
        areaLB.grid(row=1, column=6)

        portaBT = tb.Button(in_linha1FR, image=portaIM, padding=(15,17), style=('light', OUTLINE))
        portaBT.grid(row=0, column=7, padx=25)
        portaLB = tb.Label(in_linha1FR, text='xxxx')
        portaLB.grid(row=1, column=7)

        titularesBT = tb.Button(in_linha1FR, image=titularIM, padding=(15,17), style=('light', OUTLINE))
        titularesBT.grid(row=0, column=8, padx=5)
        titularesLB = tb.Label(in_linha1FR, text='xxxx')
        titularesLB.grid(row=1, column=8)

        atVisitantesBT = tb.Button(in_linha2FR, image=atVisitanteIM, padding=(15,17), style=('light', OUTLINE))
        atVisitantesBT.grid(row=0, column=0)
        atVisitantesLB = tb.Label(in_linha2FR, text='xxxx')
        atVisitantesLB.grid(row=1, column=1)

        presencaBT = tb.Button(in_linha2FR, image=presencaIM, padding=(15,17), style=('light', OUTLINE))
        presencaBT.grid(row=0, column=1, padx=30)
        presencaLB = tb.Label(in_linha2FR, text='xxxx')
        presencaLB.grid(row=1, column=0)

        horasBT = tb.Button(in_linha2FR, image=horaIM, padding=(15,17), style=('light', OUTLINE))
        horasBT.grid(row=0, column=2, padx=10)
        horasLB = tb.Label(in_linha2FR, text='xxxx')
        horasLB.grid(row=1, column=2)

        atCredenciaisBT = tb.Button(in_linha2FR, image=atCredencialIM, padding=(15,17), style=('light', OUTLINE))
        atCredenciaisBT.grid(row=0, column=3, padx=30)
        atCredenciaisLB = tb.Label(in_linha2FR, text='xxxx')
        atCredenciaisLB.grid(row=1, column=3)

        histoticoBT = tb.Button(in_linha2FR, image=historicoIM, padding=(15,17), style=('light', OUTLINE))
        histoticoBT.grid(row=0, column=4, padx=15)
        historicoLB = tb.Label(in_linha2FR, text='xxxx')
        historicoLB.grid(row=1, column=4)

        elevadorBT = tb.Button(in_linha2FR, image=elevadorIM, padding=(15,17), style=('light', OUTLINE))
        elevadorBT.grid(row=0, column=5, padx=25)
        elevadorLB = tb.Label(in_linha2FR, text='xxxx')
        elevadorLB.grid(row=1, column=5)

        visitaBT = tb.Button(in_linha2FR, image=visitaIM, padding=(15,17), style=('light', OUTLINE))
        visitaBT.grid(row=0, column=6, padx=10)
        visitaLB = tb.Label(in_linha2FR, text='xxxx')
        visitaLB.grid(row=1, column=6)

        alertasBT = tb.Button(in_linha2FR, image=alertaIM, padding=(15,17), style=('light', OUTLINE))
        alertasBT.grid(row=0, column=7, padx=30)
        alertasLB = tb.Label(in_linha2FR, text='xxxx')
        alertasLB.grid(row=1, column=7)
        
        alertasMultiBT = tb.Button(in_linha2FR, image=alertaMultiIM, padding=(15,17),style=('light', OUTLINE))
        alertasMultiBT.grid(row=0, column=8)
        alertasMultiLB = tb.Label(in_linha2FR, text='xxxx')
        alertasMultiLB.grid(row=1, column=8)

        leiturasBT = tb.Button(in_linha3FR, image=leituraIM, padding=(15,17), style=('light', OUTLINE))
        leiturasBT.grid(row=0, column=0)
        leiturasLB = tb.Label(in_linha3FR, text='xxxx')
        leiturasLB.grid(row=1, column=0)

        leiturasMultiBT = tb.Button(in_linha3FR, image=leituraIM, padding=(15,17), style=('light', OUTLINE))
        leiturasMultiBT.grid(row=0, column=1, padx=30)
        leiturasMultiLB = tb.Label(in_linha3FR, text='xxxx')
        leiturasMultiLB.grid(row=1, column=1)

        #Manutenção
        statusBT = tb.Button(mn_linha1FR, image=statusIM, padding=(15,17), style=('light', OUTLINE))
        statusBT.grid(row=0, column=0)
        statusLB = tb.Label(mn_linha1FR, text='xxxx')
        statusLB.grid(row=1, column=0)

        auditoriaBT = tb.Button(mn_linha1FR, image=auditoriaIM, padding=(15,17), style=('light', OUTLINE))
        auditoriaBT.grid(row=0, column=1, padx=30)
        auditoiaLB = tb.Label(mn_linha1FR, text='xxxx')
        auditoiaLB.grid(row=1, column=1)

        estatisticaBT = tb.Button(mn_linha1FR, image=estatisticaIM, padding=(15,17), style=('light', OUTLINE))
        estatisticaBT.grid(row=0, column=2, padx=10)
        estatisticaLB = tb.Label(mn_linha1FR, text='xxxx')
        estatisticaLB.grid(row=1, column=2)

        permissaoBT = tb.Button(mn_linha1FR, image=cartaoIM, padding=(15,17), style=('light', OUTLINE))
        permissaoBT.grid(row=0, column=3, padx=30)
        permissaoLB = tb.Label(mn_linha1FR, text='xxxx')
        permissaoLB.grid(row=1, column=3)

        diagnosticoBT = tb.Button(mn_linha1FR, image=portaIM, padding=(15,17), style=('light', OUTLINE))
        diagnosticoBT.grid(row=0, column=4, padx=15)
        diagnosticoLB = tb.Label(mn_linha1FR, text='xxxx')
        diagnosticoLB.grid(row=1, column=4)

        regraBT = tb.Button(mn_linha1FR, image=atCredencialIM, padding=(15,17), style=('light', OUTLINE))
        regraBT.grid(row=0, column=5, padx=30)
        regrasLB = tb.Label(mn_linha1FR, text='xxxx')
        regrasLB.grid(row=1, column=5)
        
        testeBT = Botao(mn_linha1FR, texto='Teste', row=0, column=6)
        testeBT.grid()
        
        self.aba_adicionada = False
        self.rootPadrao.mainloop()

    def iniciar_telaCameras(self):
        # Dicionário para mapear abas para seus botões de fechamento
        self.aba_botoes = {}
        
        if not self.aba_adicionada:
            self.aba_adicionada = True
            tela_cam = tb.Frame(self.notebook)
            tela_cam.grid(sticky='NSEW')
            tela_cam.columnconfigure(0, weight=1)   
            tela_cam.rowconfigure((1), weight=1)
            
            self.notebook.add(tela_cam, text='xxxx')
            fecharBT = ttk.Checkbutton(tela_cam, text="X", command=lambda tela_cam=tela_cam: self.fechar_aba(tela_cam), 
                                  bootstyle="light-toolbutton",
                                  padding=(5,2))
            fecharBT.grid(row=0, sticky="ne")

            self.aba_botoes[tela_cam] = fecharBT
            self.tela = TelaAdicional(tela_cam)

    def fechar_aba(self, aba):
        indice = self.notebook.index(aba)
        if indice != -1:
            self.notebook.hide(indice)
            self.aba_adicionada = False
        
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

teste = TelaPadrao()