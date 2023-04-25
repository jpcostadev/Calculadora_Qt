from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from utils import isEmpty, isNumOrDot
from variables import BIG_FONT_SIZE, MINIMUM_WIDTH, TEXT_MARGIN


class Display(QLineEdit):
    eqRequested = Signal()
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()
    inputPressed = Signal(str)
    operatorPressed = Signal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        margins = [TEXT_MARGIN for _ in range(4)]
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')

        # define o tamanho minimo do espaço onde terá os números
        self.setMinimumHeight(BIG_FONT_SIZE * 2)

        # largura mínima
        self.setMinimumWidth(MINIMUM_WIDTH)

        # Alinha o texto a direita
        self.setAlignment(Qt.AlignmentFlag.AlignRight)

        # Define o tamanho da margin
        self.setTextMargins(*margins)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key.Key_Enter

        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return, KEYS.Key_Equal]
        isDelte = key in [KEYS.Key_Backspace, KEYS.Key_Delete, KEYS.Key_D]
        isEsc = key in [KEYS.Key_Escape, KEYS.Key_C]
        isOperator = key in [KEYS.Key_Plus,
                             KEYS.Key_Minus, KEYS.Key_Slash, KEYS.Key_Asterisk,
                             KEYS.Key_P]

        if isEnter:
            self.eqPressed.emit()
            return event.ignore()

        if isDelte:
            self.delPressed.emit()
            return event.ignore()

        if isEsc:
            self.clearPressed.emit()
            return event.ignore()

        if isOperator:
            if text.lower() == 'p':
                text = '^'
            self.operatorPressed.emit(text)
            return event.ignore()

        # return super().keyPressEvent(event)

    # Não passar daqui se não tiver texto
        if isEmpty(text):
            return event.ignore()

        if isNumOrDot(text):
            self.inputPressed.emit(text)
            return event.ignore()
