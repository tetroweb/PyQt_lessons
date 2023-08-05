#------------------------user authentication--------------------
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.label_username = QLabel("User name :",self)
        # self.label_username.setFrameShape(QFrame.Box)
        
        self.label_username.move(200,150)
        self.label_username.setFont(QFont("Tahoma",10))
        
        self.line_enter = QLineEdit(self)
        self.line_enter.setPlaceholderText("Enter the name")
        self.line_enter.move(300,150)
        
        self.button_search = QPushButton("Search",self)
        self.button_search
        self.button_search.move(260,180)
        
        
        self.resize(700,500)
        self.show()
        
        
app = QApplication([])
window = Main()
app.exec()