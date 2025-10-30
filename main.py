from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QComboBox,
    QPushButton, QVBoxLayout, QMessageBox
)
import sys

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Calculator - PyQt6")
        self.setFixedSize(300, 250)
        self.init_ui()

    def init_ui(self):
        # Widgets
        self.label1 = QLabel("Enter your first number:")
        self.num1 = QLineEdit()

        self.label2 = QLabel("Enter your second number:")
        self.num2 = QLineEdit()

        self.label3 = QLabel("Choose an operation:")
        self.operation = QComboBox()
        self.operation.addItems(["Add", "Subtract", "Multiply"])

        self.result_label = QLabel("Result: ")
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.num1)
        layout.addWidget(self.label2)
        layout.addWidget(self.num2)
        layout.addWidget(self.label3)
        layout.addWidget(self.operation)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate(self):
        try:
            a = float(self.num1.text())
            b = float(self.num2.text())
            op = self.operation.currentText()

            if op == "Add":
                result = a + b
            elif op == "Subtract":
                result = a - b
            elif op == "Multiply":
                result = a * b

            self.result_label.setText(f"Result: {result}")
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter valid numbers!")

# Run the app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
