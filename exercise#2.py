#------------------------user authentication--------------------
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.login = login(self)
        
        
        
        

class login(QWidget):
    def __init__(self, parent = Main):
        super().__init__()
        
        self.label_username = QLabel("Username :",self)
        self.label_password = QLabel("Password :",self)
        
        self.label_username.move(20,20)
        self.label_password.move(20,60)

        self.line_user = QLineEdit(self)
        self.line_password = QLineEdit(self)
        
        self.line_user.move(120,20)
        self.line_password.move(120,60)
        
        self.button_login = QPushButton("Login",self)
        self.button_cancel = QPushButton("Cancel",self)
        
        self.button_login.move(100,100)
        self.button_cancel.move(200,100)
        
        self.resize(300,180)
        self.show()



app = QApplication([])
window = Main()
app.exec()