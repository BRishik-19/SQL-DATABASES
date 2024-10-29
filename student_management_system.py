from PyQt6.QtWidgets import (QApplication,QTableWidgetItem,QTableWidget,QWidget,QMenuBar,QGridLayout,QLayout,QPushButton,
                             QLineEdit,QVBoxLayout,QComboBox,QLabel,QMainWindow,QDialog)
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
        add_student_action.triggered.connect(self.insert)
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

    def insert(self):
        dialog = InsertDialog()
        dialog.exec()



class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert new data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Name")
        layout.addWidget(self.name_edit)

        self.course_name = QComboBox()
        courses = ["Biology","Math","Astronomy","Physics"]
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)

        self.ph_num = QLineEdit()
        self.ph_num.setPlaceholderText("Mobile")
        layout.addWidget(self.ph_num)

        button = QPushButton("Register")
        button.clicked.connect(self.add_student)
        layout.addWidget(button)

        self.setLayout(layout)


    def add_student(self):
        name = self.name_edit.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.ph_num.text()
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)",
                       (name, course, mobile))
        connection.commit()
        cursor.close()
        connection.close()
        win.load_data()




app = QApplication(sys.argv)
win = Mainwindow()
win.show()
win.load_data()
sys.exit(app.exec())

