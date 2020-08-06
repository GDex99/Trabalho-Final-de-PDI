# IMPORTACOES
import sys
import subprocess
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QGridLayout, QWidget, QMessageBox
from PyQt5.QtCore import QSize
import shutil


# VARIAVEIS
janelaTitulo_ = "Trabalho Final(Aplicativo) - PDI"
arquivos_ = "&File"
filtros_ = "&Filtros"
sobre_ = "&Sobre"
abrir_ = "Abrir"
salvarComo_ = "Salvar Como..."
fechar_ = "Fechar"
filtro_negativo_ = "Negativo"
filtro_gamma_ = "Correcao Gamma..."
filtro_transformacao_logaritmica_ = "Transformacao Logaritmica"
filtro_shapen_ = "Shapen"
filtro_da_mediana_ = "Mediana"
filtro_gaussiano_ = "Gaussiano"
filtro_gaussiano_3x3_ = "3 x 3"
filtro_gaussiano_5x5_ = "5 x 5"
filtro_gaussiano_7x7_ = "7 x 7"
filtro_deteccao_de_borda_com_sobel_ = "Deteccao de Borda com Sobel..."
filtro_deteccao_de_borda_com_filtro_da_lista4_ = "Deteccao de Borda Especial"
filtro_deteccao_especial_1_ = "?"
filtro_deteccao_especial_2_ = "?"
filtro_deteccao_especial_3_ = "?"
filtro_colorida_para_escala_de_cinza_ = "Colorida para Escala de Cinza"
filtro_colorida_para_preto_e_branco_ = "Colorida para Preto e Branco..."
filtro_separacao_de_camadas_ = "Separacao das Camadas"
filtro_camada_R_ = "Camada R"
filtro_camada_G_ = "Camada G"
filtro_camada_B_ = "Camada B"
filtro_de_erosao_ = "Erosao..."
filtro_de_dilatacao_ = "Dilatacao..."
filtro_de_abertura_ = "Abertura..."
filtro_de_fechamento_ = "Fechamento..."
filtro_deteccao_de_borda_de_imagem_binaria_ = "Deteccao de Borda de Imagem Binaria"
sobre_aplicativo_ = "Aplicativo"
sobre_imagem_ = "Imagem"
sobre_ideias_para_o_projeto_ = "As ideias para esse projeto "
mensagem_inicial = "12.0.3.4.6.8.11.3.14: Seja Bem-Vindo ao meu trabalho final"
imagem_de_fundo = "capa.png"
abrir_arquivo = "Open File"
salvar_arquivo = "Save as..."


atalho0_ = "Alt+1" # Abrir
atalho1_ = "Alt+S" # Salvar como...
atalho2_ = "Alt+0" # Fechar
atalho3_ = "Ctrl+N" # Negativo
atalho4_ = "Ctrl+G" # Gamma
atalho5_ = "Ctrl+L" # Transformacao Logaritmica
atalho6_ = "Ctrl+S" # Shapen
atalho7_ = "Ctrl+M" # Mediana
atalho8_ = "Ctrl+3" #  Gaussiano 3x3
atalho9_ = "Ctrl+5" #  Gaussiano 5x5
atalho10_ = "Ctrl+7" #  Gaussiano 7x7
atalho11_ = "Ctrl+B+S" # Deteccao de borda com filtro Sobel
atalho12_ = "Ctrl+Shift+/" # sem nome
atalho13_ = "Ctrl+Shift+1" # sem nome
atalho14_ = "Ctrl+Shift+8" # sem nome
atalho15_ = "Ctrl+E" # Colorida para escala de cinza
atalho16_ = "Ctrl+P+B" # Colorida para preto e branco
atalho17_ = "Ctrl+R" # Camada R
atalho18_ = "Ctrl+G" # Camada G
atalho19_ = "Ctrl+B" # Camada B
atalho20_ = "Ctrl+E" # Erosao
atalho21_ = "Ctrl+D" # Dilatacao
atalho22_ = "Ctrl+A" # Abertura
atalho23_ = "Ctrl+F" # Fechamento
atalho24_ = "Ctrl+D+B" # Detecccao de borda de imagem binaria
atalho25_ = "Shift+A" # Aplicativo
atalho26_ = "Shift+I" # Imagens
atalho27_ = "Shift+8" # Ideias
atalho28_ = ""
atalho29_ = ""
atalho30_ = ""


nomeCompleto = "Gildo Alves Monteiro Filho"
nomeCidade = "Ituiutaba-MG"
dataTermino = "5 de Agosto de 2020"
linkApresentacao = ""







class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setup_main_window()
        self.initUI()

    def setup_main_window(self):
        self.x = 640
        self.y = 480
        self.setMinimumSize(QSize(self.x, self.y))
        self.setWindowTitle(janelaTitulo_)
        self.wid = QWidget(self)
        self.setCentralWidget(self.wid)
        self.layout = QGridLayout()
        self.wid.setLayout(self.layout)

    def initUI(self):

        # Craindo barra de menu
        self.barraDeMenu = self.menuBar()

        # Criando os menus
        self.menuArquivo = self.barraDeMenu.addMenu(arquivos_)
        self.menuImagens = self.barraDeMenu.addMenu(filtros_)
        self.menuSobre = self.barraDeMenu.addMenu(sobre_)

        # ♦-♦-♦
        #
        # FILE Criando as actions - ABRIR
        self.opcaoAbrir = self.menuArquivo.addAction(abrir_)
        self.opcaoAbrir.triggered.connect(self.open_file)
        self.opcaoAbrir.setShortcut(atalho0_)
        self.opcaoAbrir.setCheckable(True)
        self.opcaoAbrir.setChecked(False)

        # FILE Criando SALVAR COMO... (submenu)
        self.opcaoSalvarComo = self.menuArquivo.addAction(salvarComo_)
        self.opcaoSalvarComo.triggered.connect(self._save_as)
        self.opcaoSalvarComo.setShortcut(atalho1_)
        self.opcaoSalvarComo.setCheckable(True)
        self.opcaoSalvarComo.setChecked(False)

        # FILE Criando uma separacao
        self.menuArquivo.addSeparator()

        # FILE Criando 'FECHAR'
        self.opcaoFechar = self.menuArquivo.addAction(fechar_)
        self.opcaoFechar.setShortcut(atalho2_)
        self.opcaoFechar.triggered.connect(self.close)
        #
        # ♦-♦-♦

        # ♠-♠-♠
        #
        # TRANFORMACOES
        self.negativo = self.menuImagens.addAction(filtro_negativo_)
        self.negativo.triggered.connect(self.filtro_negativo)
        self.negativo.setShortcut(atalho3_)
        self.negativo.setCheckable(True)
        self.negativo.setChecked(False)

        self.gamma = self.menuImagens.addAction(filtro_gamma_)
        self.gamma.triggered.connect(self.filtro_gamma)
        self.gamma.setShortcut(atalho4_)
        self.gamma.setCheckable(True)
        self.gamma.setChecked(False)

        self.transformacaoLogaritmica = self.menuImagens.addAction(filtro_transformacao_logaritmica_)
        self.transformacaoLogaritmica.triggered.connect(self.filtro_transformacaoLogaritmica)
        self.transformacaoLogaritmica.setShortcut(atalho5_)
        self.transformacaoLogaritmica.setCheckable(True)
        self.transformacaoLogaritmica.setChecked(False)

        self.shapen = self.menuImagens.addAction(filtro_shapen_)
        self.shapen.triggered.connect(self.filtro_shapen)
        self.shapen.setShortcut(atalho6_)
        self.shapen.setCheckable(True)
        self.shapen.setChecked(False)

        self.mediana = self.menuImagens.addAction(filtro_da_mediana_)
        self.mediana.triggered.connect(self.filtro_mediana)
        self.mediana.setShortcut(atalho7_)
        self.mediana.setCheckable(True)
        self.mediana.setChecked(False)

        # FILE Criando uma separacao
        self.menuImagens.addSeparator()

        self.gaussiano = self.menuImagens.addMenu(filtro_gaussiano_)
        self.tresPorTres = self.gaussiano.addAction(filtro_gaussiano_3x3_)
        self.tresPorTres.triggered.connect(self.filtro_gaussiano3x3)
        self.tresPorTres.setShortcut(atalho8_)
        self.tresPorTres.setCheckable(True)
        self.tresPorTres.setChecked(False)

        self.cincoPorCinco = self.gaussiano.addAction(filtro_gaussiano_5x5_)
        self.cincoPorCinco.triggered.connect(self.filtro_gaussiano5x5)
        self.cincoPorCinco.setShortcut(atalho9_)
        self.cincoPorCinco.setCheckable(True)
        self.cincoPorCinco.setChecked(False)

        self.setePorSete = self.gaussiano.addAction(filtro_gaussiano_7x7_)
        self.setePorSete.triggered.connect(self.filtro_gaussiano7x7)
        self.setePorSete.setShortcut(atalho10_)
        self.setePorSete.setCheckable(True)
        self.setePorSete.setChecked(False)

        # FILE Criando uma separacao
        self.menuImagens.addSeparator()

        self.sobel = self.menuImagens.addAction(filtro_deteccao_de_borda_com_sobel_)
        self.sobel.triggered.connect(self.filtro_sobel)
        self.sobel.setShortcut(atalho11_)
        self.sobel.setCheckable(True)
        self.sobel.setChecked(False)

        # FILE Criando uma separacao
        self.menuImagens.addSeparator()

        self.detecccaoDeBordaEspecial = self.menuImagens.addMenu(filtro_deteccao_de_borda_com_filtro_da_lista4_)
        self.detecccaoDeBordaEspecial1 = self.detecccaoDeBordaEspecial.addAction(filtro_deteccao_especial_1_)
        self.detecccaoDeBordaEspecial1.triggered.connect(self.filtro_deteccaoDeBordaEspecial1)
        self.detecccaoDeBordaEspecial1.setShortcut(atalho12_)
        self.detecccaoDeBordaEspecial1.setCheckable(True)
        self.detecccaoDeBordaEspecial1.setChecked(False)

        self.detecccaoDeBordaEspecial2 = self.detecccaoDeBordaEspecial.addAction(filtro_deteccao_especial_2_)
        self.detecccaoDeBordaEspecial2.triggered.connect(self.filtro_deteccaoDeBordaEspecial2)
        self.detecccaoDeBordaEspecial2.setShortcut(atalho13_)
        self.detecccaoDeBordaEspecial2.setCheckable(True)
        self.detecccaoDeBordaEspecial2.setChecked(False)

        self.detecccaoDeBordaEspecial3 = self.detecccaoDeBordaEspecial.addAction(filtro_deteccao_especial_3_)
        self.detecccaoDeBordaEspecial3.triggered.connect(self.filtro_deteccaoDeBordaEspecial3)
        self.detecccaoDeBordaEspecial3.setShortcut(atalho14_)
        self.detecccaoDeBordaEspecial3.setCheckable(True)
        self.detecccaoDeBordaEspecial3.setChecked(False)

        # FILE Criando uma separacao
        self.menuImagens.addSeparator()

        self.coloridaParaEscalaDeCinza = self.menuImagens.addAction(filtro_colorida_para_escala_de_cinza_)
        self.coloridaParaEscalaDeCinza.triggered.connect(self.filtro_coloridaParaEscalaDeCinza)
        self.coloridaParaEscalaDeCinza.setShortcut(atalho15_)
        self.coloridaParaEscalaDeCinza.setCheckable(True)
        self.coloridaParaEscalaDeCinza.setChecked(False)

        self.coloridaParaPretoAndBranco = self.menuImagens.addAction(filtro_colorida_para_preto_e_branco_)
        self.coloridaParaPretoAndBranco.triggered.connect(self.filtro_coloridaParaPretoAndBranco)
        self.coloridaParaPretoAndBranco.setShortcut(atalho16_)
        self.coloridaParaPretoAndBranco.setCheckable(True)
        self.coloridaParaPretoAndBranco.setChecked(False)

        # FILE Criando uma separacao
        self.menuImagens.addSeparator()

        self.separacaoDeCamadas = self.menuImagens.addMenu(filtro_separacao_de_camadas_)
        self.camadaR = self.separacaoDeCamadas.addAction(filtro_camada_R_)
        self.camadaR.triggered.connect(self.filtro_camadaR)
        self.camadaR.setShortcut(atalho17_)
        self.camadaR.setCheckable(True)
        self.camadaR.setChecked(False)

        self.camadaG = self.separacaoDeCamadas.addAction(filtro_camada_G_)
        self.camadaG.triggered.connect(self.filtro_camadaG)
        self.camadaG.setShortcut(atalho18_)
        self.camadaG.setCheckable(True)
        self.camadaG.setChecked(False)

        self.camadaB = self.separacaoDeCamadas.addAction(filtro_camada_B_)
        self.camadaB.triggered.connect(self.filtro_camadaB)
        self.camadaB.setShortcut(atalho19_)
        self.camadaB.setCheckable(True)
        self.camadaB.setChecked(False)

        # FILE Criando uma separacao
        self.menuImagens.addSeparator()

        self.erosao = self.menuImagens.addAction(filtro_de_erosao_)
        self.erosao.triggered.connect(self.filtro_erosao)
        self.erosao.setShortcut(atalho20_)
        self.erosao.setCheckable(True)
        self.erosao.setChecked(False)

        self.dilatacao = self.menuImagens.addAction(filtro_de_dilatacao_)
        self.dilatacao.triggered.connect(self.filtro_dilatacao)
        self.dilatacao.setShortcut(atalho21_)
        self.dilatacao.setCheckable(True)
        self.dilatacao.setChecked(False)

        self.abertura = self.menuImagens.addAction(filtro_de_abertura_)
        self.abertura.triggered.connect(self.filtro_abertura)
        self.abertura.setShortcut(atalho22_)
        self.abertura.setCheckable(True)
        self.abertura.setChecked(False)

        self.fechamento = self.menuImagens.addAction(filtro_de_fechamento_)
        self.fechamento.triggered.connect(self.filtro_fechamento)
        self.fechamento.setShortcut(atalho23_)
        self.fechamento.setCheckable(True)
        self.fechamento.setChecked(False)

        self.deteccaoDeBordaDeImagemBinaria = self.menuImagens.addAction(filtro_deteccao_de_borda_de_imagem_binaria_)
        self.deteccaoDeBordaDeImagemBinaria.triggered.connect(self.filtro_deteccaoDeBordaDeImagemBinaria)
        self.deteccaoDeBordaDeImagemBinaria.setShortcut(atalho24_)
        self.deteccaoDeBordaDeImagemBinaria.setCheckable(True)
        self.deteccaoDeBordaDeImagemBinaria.setChecked(False)



        
        #
        # ♠-♠-♠

        # ♣-♣-♣
        #
        # SOBRE Criando 'Sobre'
        self.opcaoSobre = self.menuSobre.addAction(sobre_aplicativo_)
        self.opcaoSobre.triggered.connect(self.exibe_mensagem)
        self.opcaoSobre.setShortcut(atalho25_)
        self.opcaoSobre.setCheckable(True)
        self.opcaoSobre.setChecked(False)
        
        self.infoImagem = self.menuSobre.addAction(sobre_imagem_)
        self.infoImagem.triggered.connect(self.exibe_info)
        self.infoImagem.setShortcut(atalho26_)
        self.infoImagem.setCheckable(True)
        self.infoImagem.setChecked(False)

        # FILE Criando uma separacao
        self.menuSobre.addSeparator()
        
        self.ideiasParaProjeto = self.menuSobre.addAction(sobre_ideias_para_o_projeto_)
        self.ideiasParaProjeto.triggered.connect(self.exibe_ideiasParaProjeto)
        self.ideiasParaProjeto.setShortcut(atalho27_)
        self.ideiasParaProjeto.setCheckable(True)
        self.ideiasParaProjeto.setChecked(False)
        
        
        #
        # ♣-♣-♣

        # Criando barra de status
        self.barraStatus = self.statusBar()
        self.barraStatus.showMessage(
            mensagem_inicial, 3000)

        # Criando os widgets (label, text, image)
        self.texto = QLabel(self)
        self.texto.adjustSize()
        self.largura = self.texto.frameGeometry().width()
        self.altura = self.texto.frameGeometry().height()
        self.texto.setAlignment(QtCore.Qt.AlignCenter)

       # Criando uma imagem
        self.imagem1 = QLabel(self)
        self.endereco1 = imagem_de_fundo
        self.pixmap1 = QtGui.QPixmap(self.endereco1)
        self.pixmap1 = self.pixmap1.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.imagem1.setPixmap(self.pixmap1)
        self.imagem1.setAlignment(QtCore.Qt.AlignCenter)

        # Segunda imagem
        self.imagem2 = QLabel(self)
        self.endereco2 = imagem_de_fundo
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap1.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

        # Organizando os widgets dentro do GridLayout
        self.layout.addWidget(self.texto, 0, 0, 1, 2)
        self.layout.addWidget(self.imagem1, 1, 0)
        self.layout.addWidget(self.imagem2, 1, 1)
        self.layout.setRowStretch(0, 0)
        self.layout.setRowStretch(1, 1)
        self.layout.setRowStretch(2, 0)

    

    # ♦-♦-♦
    #
    # function para 'abrir o arquivo'
    def open_file(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, caption=abrir_arquivo,
                                                            directory=QtCore.QDir.currentPath(),
                                                            filter='Images (*.ppm; *.pgm; *.pbm)',
                                                            initialFilter='Images (*.pgm)')

        print(fileName)
        if fileName != '':

            self.endereco1 = fileName
            self.pixmap1 = QtGui.QPixmap(self.endereco1)
            self.pixmap1 = self.pixmap1.scaled(
                300, 300, QtCore.Qt.KeepAspectRatio)
            self.imagem1.setPixmap(self.pixmap1)

    # function para 'salvar o arquivo'
    def _save_as(self):
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, caption=salvar_arquivo,
                                                            directory=QtCore.QDir.currentPath(),
                                                            filter='Images (*.ppm; *.pgm; *.pbm)',
                                                            initialFilter='Images (*.pgm)')

        print(fileName)

        if fileName != '':
            self.pixmap2 = QtGui.QPixmap(self.endereco2)
            self.pixmap2 = self.pixmap2.scaled(
                300, 300, QtCore.Qt.KeepAspectRatio)
            self.imagem2.setPixmap(self.pixmap2)

            shutil.copyfile(self.endereco2, fileName)
    #
    # ♦-♦-♦

    # ♠-♠-♠
    #
    def filtro_negativo(self):
        self.entrada = self.endereco1
        self.saida = 'new'
        self.script = 'filtro_negativo.py'
        self.program = 'python ' + self.script + \
            ' ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def filtro_gamma(self):
        self.entrada = self.endereco1
        self.saida = 'new'
        self.script = 'filtro_gamma.py'
        self.program = 'python ' + self.script + \
            ' ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def filtro_transformacaoLogaritmica(self):
        self.entrada = self.endereco1
        self.saida = 'new'
        self.script = 'filtro_transformacaoLogaritmica.py'
        self.program = 'python ' + self.script + \
            ' ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def filtro_shapen(self):
        self.entrada = self.endereco1
        self.saida = 'new'
        self.script = 'filtro_shapen.py'
        self.program = 'python ' + self.script + \
            ' ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def filtro_mediana(self):
        self.entrada = self.endereco1
        self.saida = 'new'
        self.script = 'filtro_mediana.py'
        self.program = 'python ' + self.script + \
            ' ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)
    
    def filtro_gaussiano3x3(self):
        self.entrada = self.endereco1
        self.saida = 'new'
        self.script = 'filtro_gaussiano3x3.py'
        self.program = 'python ' + self.script + \
            ' ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def filtro_gaussiano5x5(self):
        self.entrada = self.endereco1
        self.saida = 'new'
        self.script = 'filtro_gaussiano5x5.py'
        self.program = 'python ' + self.script + \
            ' ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def filtro_gaussiano7x7(self):
        self.entrada = self.endereco1
        self.saida = 'new'
        self.script = 'filtro_gaussiano7x7.py'
        self.program = 'python ' + self.script + \
            ' ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def filtro_deteccaoDeBorda(self):
        self.entrada = self.endereco1
        self.saida = 'new'
        self.script = 'filtro_deteccaoDeBorda.py'
        self.program = 'python ' + self.script + \
            ' ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def filtro_sobel(self):
        self.entrada = self.endereco1
        self.saida = 'new'
        self.script = 'filtro_sobel.py'
        self.program = 'python ' + self.script + \
            ' ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)
    

    def filtro_deteccaoDeBordaEspecial1(self):
        self.entrada = self.endereco1
        self.saida = 'new'
        self.script = 'filtro_deteccaoDeBordaEspecial1.py'
        self.program = 'python ' + self.script + \
            ' ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def filtro_deteccaoDeBordaEspecial2(self):
        self.entrada = self.endereco1
        self.saida = 'new'
        self.script = 'filtro_deteccaoDeBordaEspecial2.py'
        self.program = 'python ' + self.script + \
            ' ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def filtro_deteccaoDeBordaEspecial3(self):
        self.entrada = self.endereco1
        self.saida = 'new'
        self.script = 'filtro_deteccaoDeBordaEspecial3.py'
        self.program = 'python ' + self.script + \
            ' ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def filtro_coloridaParaEscalaDeCinza(self):
        self.entrada = self.endereco1
        self.saida = 'new'
        self.script = 'filtro_coloridaParaEscalaDeCinza.py'
        self.program = 'python ' + self.script + \
            ' ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def filtro_coloridaParaPretoAndBranco(self):
        self.entrada = self.endereco1
        self.saida = 'new'
        self.script = 'filtro_coloridaParaEscalaDeCinza.py'
        self.program = 'python ' + self.script + \
            ' ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def filtro_camadaR(self):
        self.entrada = self.endereco1
        self.saida = 'new'
        self.script = 'filtro_camadaR.py'
        self.program = 'python ' + self.script + \
            ' ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def filtro_camadaG(self):
        self.entrada = self.endereco1
        self.saida = 'new'
        self.script = 'filtro_camadaG.py'
        self.program = 'python ' + self.script + \
            ' ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def filtro_camadaB(self):
        self.entrada = self.endereco1
        self.saida = 'new'
        self.script = 'filtro_camadaB.py'
        self.program = 'python ' + self.script + \
            ' ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def filtro_erosao(self):
        self.entrada = self.endereco1
        self.saida = 'new'
        self.script = 'filtro_erosao.py'
        self.program = 'python ' + self.script + \
            ' ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def filtro_dilatacao(self):
        self.entrada = self.endereco1
        self.saida = 'new'
        self.script = 'filtro_dilatacao.py'
        self.program = 'python ' + self.script + \
            ' ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def filtro_abertura(self):
        self.entrada = self.endereco1
        self.saida = 'new'
        self.script = 'filtro_abertura.py'
        self.program = 'python ' + self.script + \
            ' ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def filtro_fechamento(self):
        self.entrada = self.endereco1
        self.saida = 'new'
        self.script = 'filtro_fechamento.py'
        self.program = 'python ' + self.script + \
            ' ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def filtro_deteccaoDeBordaDeImagemBinaria(self):
        self.entrada = self.endereco1
        self.saida = 'new'
        self.script = 'filtro_deteccaoDeBordaDeImagemBinaria.py'
        self.program = 'python ' + self.script + \
            ' ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)
    #
    # ♠-♠-♠

    # ♣-♣-♣
    #
    # function para 'SOBRE MIM'
    def exibe_mensagem(self):
        self.barraStatus.showMessage("Vc clicou no sobre mim, parabens", 5000)
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setText("Versao: BETA\n")
        self.msg.setWindowTitle("Sobre")
        self.msg.setInformativeText("Uma janela que tem alguns dos filtros que aprendemos na diciplina de Processamento Digital de Imagens. Nessa janela eu usei os filtros: Negativo, Conversao para cinza, Gama, Transformcao Logaritmica, Deteccao de borda, Separacao de camada")
        self.msg.setDetailedText(
            nomeCompleto + "\n" + nomeCidade + "\n" + dataTermino + "\n" + linkApresentacao)
        self.msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.msg.exec_()  # Exibe a caixa de mensagem, ou caixa de dialogo
    

    def exibe_info(self):
        #MODIFICACAO PARA A LISTA 01/07/20 #
        localizacao = self.endereco1
        arq = localizacao.rpartition('/')
        arq = (arq[2])
        count = 0
        with open(self.endereco1, 'rb') as f:
            for line in f:
                count += 1
                # print(line)
                if count == 1:
                    tipo = str(line)
                    tipo = (tipo[2:-3])
                if count == 2:
                    comentario = str(line)
                    comentario = (comentario[2:-3])
                if count == 3:
                    largura = str(line)
                    largura = (largura[2:-7])
                    altura = str(line)
                    altura = (altura[6:-3])
        self.barraStatus.showMessage("Informacoes sobre a imagem", 5000)
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setText(
            "Caminho: " + localizacao + "\nArquivo: " + arq + "\nTipo: " + tipo + "\nComentario: " + comentario + "\nLargura: " + largura + "\nAltura: " + altura)
        self.msg.setWindowTitle("Informacao sobre a imagem")
        self.msg.exec_()

    def exibe_ideiasParaProjeto(self):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Warning)
        self.msg.setText("uma barra de carregando sincronizada com as transformacoes")
        self.msg.setWindowTitle("Coisas para colocar")
        self.msg.setInformativeText("")
        self.msg.setDetailedText(
            "")
        self.msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.msg.exec_()

    
    #
    # ♣-♣-♣


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_()) 


window()
