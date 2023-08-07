#---------------------QFontComboBox-----------------
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.QtGui import * 


class Main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.combo = QFontComboBox(self)
        self.combo.currentFontChanged.connect(self.label_font)
        
        self.label = QLabel("label",self)
        self.label.move(100,50)
        
        self.resize(800,500)
        self.show()
    
    def label_font(self,f):
        self.label.setFont(f)
        
            
app = QApplication([])
window = Main()
app.exec()