import sys

from buttons import ButtonsGrid
from display import Display
from info import Info
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from styles import setupTheme 
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    # snake_case
    # PascalCase
    # camelCase

    # cria a aplicação
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # info
    info = Info('sua conta')
    window.addWidgettoVLayout(info)

    # Display
    display = Display()
    # cria um texto tranparente no display que some quando é digitado algo
    display.setPlaceholderText('Digite')
    window.addWidgettoVLayout(display)
    # window.addToVLayout(Display('Olá Mundo'))  # display 2

    # Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # Button

    # Executa tudo
    window.adjustFixedSize()  # tira o Maximizar
    window.show()
    app.exec()
