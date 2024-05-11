from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QGridLayout, QFrame
from PyQt6.QtCore import Qt
from logic import CalculatorModel
import math

class CalculatorGUI(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        """
        Initialize the user interface for the calculator.
        """
        self.setWindowTitle("Calculator")
        self.setFixedSize(300, 300)

        layout = QVBoxLayout()

        label_frame = QFrame()
        label_frame.setFrameShape(QFrame.Shape.Box)
        label_frame.setFrameShadow(QFrame.Shadow.Raised)
        label_layout = QVBoxLayout()
        self.result_label = QLabel()
        label_layout.addWidget(self.result_label, alignment=Qt.AlignmentFlag.AlignCenter)
        label_frame.setLayout(label_layout)
        layout.addWidget(label_frame)

        buttons_layout = QGridLayout()

        # Row 1 Each row is similar, use this as example
        button_1 = QPushButton("1") # Creation of label
        button_1.clicked.connect(lambda: self.on_button_click("1")) # Connects the signal of button_1 to on_button_click
        buttons_layout.addWidget(button_1, 0, 0) # Adds button to layout at row 0, column 0

        # Button "2"
        button_2 = QPushButton("2")
        button_2.clicked.connect(lambda: self.on_button_click("2"))
        buttons_layout.addWidget(button_2, 0, 1)

        # Button "3"
        button_3 = QPushButton("3")
        button_3.clicked.connect(lambda: self.on_button_click("3"))
        buttons_layout.addWidget(button_3, 0, 2)

        # Button "+"
        button_plus = QPushButton("+")
        button_plus.clicked.connect(lambda: self.on_button_click("+"))
        buttons_layout.addWidget(button_plus, 0, 3)

        # ROW 2

        # Button "4"
        button_4 = QPushButton("4")
        button_4.clicked.connect(lambda: self.on_button_click("4"))
        buttons_layout.addWidget(button_4, 1, 0)

        # Button "5"
        button_5 = QPushButton("5")
        button_5.clicked.connect(lambda: self.on_button_click("5"))
        buttons_layout.addWidget(button_5, 1, 1)

        # Button "6"
        button_6 = QPushButton("6")
        button_6.clicked.connect(lambda: self.on_button_click("6"))
        buttons_layout.addWidget(button_6, 1, 2)

        # Button "-"
        button_minus = QPushButton("-")
        button_minus.clicked.connect(lambda: self.on_button_click("-"))
        buttons_layout.addWidget(button_minus, 1, 3)

        # ROW 3

        # Button "7"
        button_7 = QPushButton("7")
        button_7.clicked.connect(lambda: self.on_button_click("7"))
        buttons_layout.addWidget(button_7, 2, 0)

        # Button "8"
        button_8 = QPushButton("8")
        button_8.clicked.connect(lambda: self.on_button_click("8"))
        buttons_layout.addWidget(button_8, 2, 1)

        # Button "9"
        button_9 = QPushButton("9")
        button_9.clicked.connect(lambda: self.on_button_click("9"))
        buttons_layout.addWidget(button_9, 2, 2)

        # Button "*"
        button_multiply = QPushButton("*")
        button_multiply.clicked.connect(lambda: self.on_button_click("*"))
        buttons_layout.addWidget(button_multiply, 2, 3)

        # ROW 4

        # Button "e"
        button_e = QPushButton("e")
        button_e.clicked.connect(lambda: self.on_button_click("e"))
        buttons_layout.addWidget(button_e, 3, 4)

        # Button "π"
        button_pi = QPushButton("π")
        button_pi.clicked.connect(lambda: self.on_button_click("π"))
        buttons_layout.addWidget(button_pi, 2, 4)

        # Button "(-)"
        button_negative = QPushButton("(-)")
        button_negative.clicked.connect(lambda: self.on_button_click("-"))
        buttons_layout.addWidget(button_negative, 3, 0)

        # Button "0"
        button_0 = QPushButton("0")
        button_0.clicked.connect(lambda: self.on_button_click("0"))
        buttons_layout.addWidget(button_0, 3, 1)

        # Button "."
        button_decimal = QPushButton(".")
        button_decimal.clicked.connect(lambda: self.on_button_click("."))
        buttons_layout.addWidget(button_decimal, 3, 2)

        # Button "/"
        button_divide = QPushButton("/")
        button_divide.clicked.connect(lambda: self.on_button_click("//"))
        buttons_layout.addWidget(button_divide, 3, 3)

        # ROW 5

        # Clear Button
        button_clear = QPushButton("CLEAR")
        button_clear.clicked.connect(lambda: self.on_button_click("CLEAR"))
        buttons_layout.addWidget(button_clear, 4, 0)

        # Delete button
        button_delete = QPushButton("DEL")
        button_delete.clicked.connect(lambda: self.on_button_click("DEL"))
        buttons_layout.addWidget(button_delete, 4, 1)

        # Equal button
        button_equal = QPushButton("=")
        button_equal.clicked.connect(lambda: self.on_button_click("="))
        buttons_layout.addWidget(button_equal, 4, 2)

        # Square root button
        button_sqrt = QPushButton("√")
        button_sqrt.clicked.connect(lambda: self.on_button_click("√"))
        buttons_layout.addWidget(button_sqrt, 4, 3)

        # Square Button
        button_square = QPushButton("^2")
        button_square.clicked.connect(lambda: self.on_button_click("^2"))
        buttons_layout.addWidget(button_square, 4, 4)

        layout.addLayout(buttons_layout)
        self.setLayout(layout)

    def on_button_click(self, value):
        """
        Handles button clicks in the calculator GUI and performs appropriate actions based on the clicked button.
        value (str): The value associated with the clicked button.
        Returns:
            None
        """
        if value == '=':
            """
            If the value is = that means the equal sign button is clicked.
            """
            current_text = self.result_label.text()
            result = self.controller.evaluate_expression(current_text)
            self.result_label.setText(result)

        elif value == 'CLEAR':
            """
            If the value is CLEAR the clear button is clicked.
            """
            self.result_label.clear()

        elif value == 'DEL':
            """
            If the value is DEL the delete button is clicked.
            """
            current_text = self.result_label.text()
            self.result_label.setText(current_text[:-1])

        elif value == '√':
            """
            If the value is √ the square root button is clicked.
            """
            current_text = self.result_label.text()
            try:
                num = float(current_text)
                result = math.sqrt(num)
                self.result_label.setText(str(result))
            except ValueError:
                self.result_label.setText("Error")

        elif value == '^2':
            """
            If the value is ^2 the square button is clicked.
            """
            current_text = self.result_label.text()
            try:
                num = int(current_text)
                result = num ** 2
                self.result_label.setText(str(result))
            except ValueError:
                self.result_label.setText("Error")

        elif value == 'e':
            """
            If the value is e the 'e' button is clicked.
            """
            self.result_label.setText(self.result_label.text() + str(math.e))

        elif value == 'π':
            """
            If the value is π, it means the 'π' button is clicked.
            """
            self.result_label.setText(self.result_label.text() + str(math.pi))

        else:
            """
            For any other value (digits, decimal, operators), add it to the current text displayed in the result label
            """
            current_text = self.result_label.text() + str(value)
            self.result_label.setText(current_text)

