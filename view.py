from PyQt6.QtWidgets import *
from PyQt6 import uic
from controller import Controller


class View(QMainWindow):

    # Klassenvariablen für die Autovervollständigung

    coB_operator: QComboBox
    pb_execute: QPushButton
    pb_reset: QPushButton
    spB_operand1: QSpinBox
    spB_operand2: QSpinBox
    l_act_result: QLabel
    statusbar: QStatusBar

    def __init__(self, c: Controller):
        # super const. immer aufrufen
        super().__init__()
        # GUI laden
        uic.loadUi("Grundrechenarten.ui", self)
        # ComboBox mit Operatoren füllen
        self.coB_operator.addItem("+")
        self.coB_operator.addItem("-")
        self.coB_operator.addItem("*")
        self.coB_operator.addItem("/")
        # Handler für die Buttons verbinden
        self.pb_execute.clicked.connect(c.execute)
        self.pb_reset.clicked.connect(c.reset)

    def reset(self) -> None:
        # oberstes Element der ComboBox auswählen
        self.coB_operator.setCurrentIndex(0)
        # Operanden auf 0 setzen
        self.spB_operand1.setValue(0)
        self.spB_operand2.setValue(0)
        self.l_act_result.setText("Noch kein Ergebnis")
        self.set_text_statusbar("Bitte zwei Werte für die Operanden eingeben. Einen Operator "
                                "auswählen und mit Ausführen berechnen lassen.")

    def set_ergebnis(self, t: str) -> None:
        self.l_act_result.setText(t)

    def set_text_statusbar(self, t: str) -> None:
        self.statusbar.showMessage(t)

    def get_op1(self) -> int:
        return self.spB_operand1.value()

    def get_op2(self) -> int:
        return self.spB_operand2.value()

    def get_operator(self) -> str:
        return self.coB_operator.currentText()
