#---------------QPushButton------------------------
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.button = QPushButton("Click",self)
        self.button.resize(150,50)
        self.button.setFont(QFont("Tahoma",24))
        
        self.button.setIcon(QIcon("DEMO1.png"))
        self.button.setIconSize(QSize(40,40))
        
        # self.button.setDisabled(True) -> disables the button
        # self.button.setEnabled(True) -> enables the button

        # setCursor -> sets the appropriate cursor symbol for the mouse
        self.button.setCursor(Qt.PointingHandCursor)

        # self.button.clicked.connect -> associates the desired command with the button
        # self.button.clicked.connect(self.close) -> a command to close the page
        self.button.clicked.connect(self.title)
        self.button.click() #-> presses the button automatically
        
        
        self.setGeometry(200,200,800,500)
        self.show()
        
    def title(self):
        self.setWindowTitle("Demo 1 ")
        
        
        
        
        
        
app = QApplication([])
window = Main()
app.exec()