import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *


class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super(JanelaPrincipal, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com/'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navbar = QToolBar()
        self.addToolBar(navbar)
        navbar.setFont(QFont('Fira Code', 12))

        voltar_btn = QAction('←', self)
        voltar_btn.triggered.connect(self.browser.back)
        navbar.addAction(voltar_btn)
        voltar_btn.setFont(QFont('Fira Code', 15))

        avancar_btn = QAction('→', self)
        avancar_btn.triggered.connect(self.browser.forward)
        navbar.addAction(avancar_btn)
        avancar_btn.setFont(QFont('Fira Code', 15))

        recarregar_btn = QAction('⟲', self)
        recarregar_btn.triggered.connect(self.browser.reload)
        navbar.addAction(recarregar_btn)
        recarregar_btn.setFont(QFont('Fira Code', 15))

        home_btn = QAction('⃤', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)
        home_btn.setFont(QFont('Fira Code', 15))

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://google.com/'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('Navegador Matheus')
Janela = JanelaPrincipal()
app.exec_()
