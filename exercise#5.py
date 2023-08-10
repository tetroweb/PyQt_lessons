from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import * 

class Main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.form = QFormLayout(self)
        self.form.setVerticalSpacing(30)
        
        self.form.addRow(QLabel("The path taken"),QLineEdit())
        self.form.addRow(QLabel("Average road"),QLineEdit())
        self.form.addRow(QLabel("Fuel consume"),QLineEdit())
        
        self.button = QPushButton("Calculate")
        self.label_res =  QLabel("Result :")
        
        self.hbox =QHBoxLayout()
        self.hbox.addWidget(self.button)
        self.hbox.addWidget(self.label_res)
        self.hbox.setSpacing(50)
        self.hbox.setAlignment(Qt.AlignRight)
        self.hbox.addSpacing(100)
        
        
        self.form.addRow(self.hbox)
        
       
        self.hbox2 = QHBoxLayout()
        self.label_error = QLabel("Error")
        self.hbox2.addWidget(self.label_error)
        self.form.addRow(self.hbox2)
        self.label_error.setAlignment(Qt.AlignCenter)
        
        
        
        
        self.resize(350,180)
        self.show()
        
        
app = QApplication([])
window = Main()
app.exec()