# from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QMessageBox, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)

        # dentro da classe o window é self
        self.setCentralWidget(self.cw)

        # Título da Janela
        self.setWindowTitle('Calculadora Biridinha')

    def adjustFixedSize(self):
        # tenta ajustar o texto ao tamanho da janela
        # última coisa a ser feita.
        self.adjustSize()
        self.setFixedSize(self.width(), self. height())

        # função que diminui níveis de funções (boa prática.)
    def addWidgettoVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)
        # self.adjustFixedSize()

    def makeMsgBox(self):
        return QMessageBox(self)
