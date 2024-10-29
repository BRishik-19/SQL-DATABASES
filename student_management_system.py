from PyQt6.QtWidgets import QApplication,QTableWidgetItem,QTableWidget,QWidget,QMenuBar,QGridLayout,QLayout,QPushButton,QLineEdit,QLabel,QMainWindow
from PyQt6.QtGui import QAction
import sys
import sqlite3

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student management system")

        file_menu_bar = self.menuBar().addMenu("File")
        help_menu_bar = self.menuBar().addMenu("Help")

        add_student_action = QAction("Add student", self)
        file_menu_bar.addAction(add_student_action)

        about_action = QAction("About", self)
        help_menu_bar.addAction(about_action)

        #write the below line if about item is not shown in help menu bar,this occurs in mac os
        #]about_action.setMenuRole(QAction.MenuRole.NoRole)




        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("ID","Name","Course","Mobile"))
        #if we dont use the below 30th line ,app would display another column with default
        # serial numbers so we use this instance to over come it
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

    def load_data(self):
        connection = sqlite3.connect("database.db")
        result = connection.execute("SELECT * FROM students")
        print(result)

        self.table.setRowCount(0)
        for row,r_data in enumerate(result):
            self.table.insertRow(row)
            for col,data in enumerate(r_data):
                print(r_data)
                self.table.setItem(row, col, QTableWidgetItem(str(data)))

        connection.close()



app = QApplication(sys.argv)
win = Mainwindow()
win.show()
win.load_data()
sys.exit(app.exec())

