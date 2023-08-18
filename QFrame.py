#------------------------QFrame----------------------
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.frame = QFrame(self)
        self.frame.setFrameShape(QFrame.VLine)# -> draw vertical line 
        self.frame.setFrameShape(QFrame.HLine)# -> draw horizontal line
        self.frame.setLineWidth(10)
        
        self.tbutton = QToolButton(self)
        self.tbutton.setGeometry(50,50,100,100)
        
        
        self.frame2 = QFrame(self.tbutton)# -> frame2 is resize for the self.button because his family is tbutton
        self.frame2.setFrameShape(QFrame.Box)
        self.frame2.setFrameShadow(QFrame.Raised)
        self.frame2.setLineWidth(10)
        self.frame2.setGeometry(0,0,100,100)
        
        self.tbutton.setToolTip("First row<br>Second row")#Work css codes
        
        self.resize(800,500)
        self.show()
        
        
app = QApplication([])
window = Main()
app.exec()