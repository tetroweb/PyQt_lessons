#------------------------QFrame----------------------
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.frame = QFrame(self)
        self.frame.setFrameShape(QFrame.VLine)
        self.frame.setFrameShape(QFrame.HLine)
        self.frame.setLineWidth(10)
        
        self.tbutton = QToolButton(self)
        self.tbutton.setGeometry(50,50,100,100)
        
        
        self.frame2 = QFrame(self.tbutton)#içine self.tbutton koyduğumuz için frame self.tbutton'un kenar çizgilerini sınır olarak bildi
        self.frame2.setFrameShape(QFrame.Box)
        self.frame2.setFrameShadow(QFrame.Raised)
        self.frame2.setLineWidth(10)
        self.frame2.setGeometry(0,0,100,100)
        
        self.tbutton.setToolTip("First row<br>Second row")#Html kodlarıyla çalışır
        
        self.resize(800,500)
        self.show()
        
        
app = QApplication([])
window = Main()
app.exec()