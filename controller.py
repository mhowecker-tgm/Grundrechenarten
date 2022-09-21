import sys
from PyQt6.QtWidgets import QApplication
import model
import view


class Controller:
    def __init__(self):
        # Model und View als Variablen anlegen
        self.model = model.Grundrechnung()
        self.view = view.View(self)

    def reset(self) -> None:
        # Model und View zurücksetzen
        self.model.reset()
        self.view.reset()

    def execute(self) -> None:
        # Eingaben lesen
        op1 = self.view.get_op1()
        op2 = self.view.get_op2()
        operator = self.view.get_operator()
        # Ergebnis berechnen und ausgeben
        error = self.model.berechnen(op1, op2, operator)
        t = "Die Berechnung war erfolgreich!"
        if error is None:
            self.view.set_ergebnis(self.model.erg)
            self.view.set_text_statusbar(t)
        else:
            self.view.set_ergebnis("Fehler")
            self.view.set_text_statusbar(error)


if __name__ == '__main__':
    app = QApplication([])
    c = Controller()
    c.view.show()
    sys.exit(app.exec())
