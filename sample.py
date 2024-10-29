from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout,\
    QPushButton ,QLineEdit
import sys
from datetime import datetime

class Age_calculator(QWidget):
    def __init__(self):
        super().__init__()
        grid = QGridLayout()

        name_label = QLabel("Name:")
        self.name_input = QLineEdit()

        age_label = QLabel("Your Date of birth MM/DD/YY:")
        self.age_input = QLineEdit()



        calculate_button = QPushButton("Calculate age")
        calculate_button.clicked.connect(self.calculation)
        self.outputlabel = QLabel("")





        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_input, 0, 1)
        grid.addWidget(age_label, 1, 0)
        grid.addWidget(self.age_input, 1, 1)
        grid.addWidget(calculate_button , 2, 0, 1, 2 )
        grid.addWidget(self.outputlabel , 3, 0, 1, 2)

        self.setLayout(grid)



    def calculation(self):
        present_yr = datetime.now().year
        born_yr = self.age_input.text()
        dob = datetime.strptime(born_yr,"%m/%d/%Y").date().year
        age = present_yr-dob
        self.outputlabel.setText(f"{self.name_input} is {age} years old")






app = QApplication(sys.argv)
age_calculator = Age_calculator()
age_calculator.show()
sys.exit(app.exec())
