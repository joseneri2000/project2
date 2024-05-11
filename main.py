from PyQt6.QtWidgets import QApplication
from gui import CalculatorGUI
from logic import CalculatorModel

def run():
    app = QApplication([])
    calculator_model = CalculatorModel()
    calculator_view = CalculatorGUI(calculator_model)
    calculator_view.show()
    app.exec()

if __name__ == "__main__":
    run()