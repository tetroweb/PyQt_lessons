#--------------QlineEdit-----------------
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Main(QTabWidget):
    def __init__(self):
        super().__init__()
        
        self.line = QLineEdit(self)
        self.line.setGeometry(40,40,150,40)
        
        self.line.setText("LineEdit")
        
        self.line.setPlaceholderText("Enter your name ...")  # Creates a transparent text.
        
        self.line.setMaxLength(5)  # Maximum number of characters allowed.
        
        # self.line.setReadOnly(True)  # Creates a read-only line, meaning you cannot type in it.
        
        self.line.setFrame(True)  # Shows a frame while inputting text.
        
        self.line.setClearButtonEnabled(True)  # Adds a clear button to erase the input.
        
        
        
        self.resize(800,500)
        self.show()
        
        
        
app = QApplication([])
window = Main()
app.exec()
