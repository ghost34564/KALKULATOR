import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Калькулятор')
        self.create_ui()

    def create_ui(self):
        # Создаем сетку для размещения элементов
        layout = QGridLayout()

        # Поле для отображения выражения и результата
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setFixedHeight(80)
        layout.addWidget(self.display, 0, 0, 1, 4)

        # Создаем кнопки
        buttons = {
            '7': (1, 0),
            '8': (1, 1),
            '9': (1, 2),
            '/': (1, 3),
            '4': (2, 0),
            '5': (2, 1),
            '6': (2, 2),
            '*': (2, 3),
            '1': (3, 0),
            '2': (3, 1),
            '3': (3, 2),
            '-': (3, 3),
            '0': (4, 0),
            '.': (4, 1),
            '=': (4, 2),
            '+': (4, 3),
            'del': (5, 0)
        }

        # Создаем и добавляем кнопки на форму
        for btn_text, pos in buttons.items():
            button = QPushButton(btn_text)
            button.setFixedSize(90, 90)
            layout.addWidget(button, pos[0], pos[1])
            if btn_text not in ['=', 'del']:
                button.clicked.connect(self.num_click)
            elif btn_text == '=':
                button.clicked.connect(self.calculate)
            elif btn_text == 'del':
                button.clicked.connect(self.clear_display)

        self.setLayout(layout)

    def num_click(self):
        sender = self.sender()
        current_text = self.display.text()
        new_text = current_text + sender.text()
        self.display.setText(new_text)

    def clear_display(self):
        self.display.clear()

    def calculate(self):
        expression = self.display.text()
        try:
            result = eval(expression)
            self.display.setText(str(result))
        except Exception:
            self.display.setText('ОШИБКА!, ПРОВЕРТЕ ПРАВИЛЬНОСТЬ!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
    