from PyQt6.QtWidgets import QApplication,QWidget,QGridLayout,QLayout,QLabel,QPushButton,QLineEdit,QComboBox
import sys

class Speed_Calculator(QWidget):
    def __init__(self):
        super().__init__()
        grid = QGridLayout()

        distance_label = QLabel("Distance:")
        self.distance_input = QLineEdit()

        time_label = QLabel("Time in sec:")
        self.time_input = QLineEdit()

        units_of_distance = QComboBox()
        units_of_distance.addItems(["KM","Miles"])

        calcute_button = QPushButton("Calculate")
        calcute_button.clicked.connect()

        if units_of_distance.currentText() == "KM":
            calcute_button.clicked.connect(self.Km())
        elif units_of_distance.currentText() == "Miles":
            calcute_button.clicked.connect(self.Miles())


        self.output_label = QLabel()




        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_input, 0, 1)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_input, 1, 1)
        grid.addWidget(units_of_distance, 0, 2)
        grid.addWidget(self.output_label , 2, 0, 1, 2)

        self.setLayout(grid)


    def Km(self):
        distance = self.distance_input.text()
        time = self.time_input.text()
        velocity = distance/time
        self.output_label.setText(f"Speed is {velocity}")

    def Miles(self):
        distance = self.distance_input.text()
        time = self.time_input.text()
        velocity = distance/time
        self.output_label.setText(f"Speed is {velocity}")



app = QApplication(sys.argv)
speed_calculator = Speed_Calculator()
speed_calculator.show()
sys.exit(app.exec())


