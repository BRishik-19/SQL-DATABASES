from PyQt6.QtWidgets import  QLabel ,QWidget ,QLineEdit ,QPushButton, QApplication,QGridLayout,QLayout
import sys

class Exa(QWidget):
    def __init__(self):
        super().__init__()
        grid = QGridLayout()

        number = QLabel("Number:")
        self.line = QLineEdit()

        grid.addWidget(number,0,0)
        grid.addWidget(self.line,0,1)

        self.setLayout(grid)





app = QApplication(sys.argv)
ex = Exa()
ex.show()
sys.exit(app.exec())