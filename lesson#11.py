#----------------------QSpinBox-QDoubleSpinBox------
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import *


class Main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.spin = QSpinBox(self)
        self.spin.setRange(1,100)
        self.spin.setGeometry(10,10,100,30)
        self.spin.setMinimum(10)
        self.spin.setMaximum(100)
        self.spin.setAlignment(Qt.AlignRight)
        
        print(self.spin.value())
        self.spin.setValue(20)
        
        #tuşa bastığımızda sayının kaçar kaçar değişeceğini belirler
        self.spin.setSingleStep(5)
        
        self.spin.setSuffix(" TL")
        self.spin.setPrefix(" % ")
        
        self.double_spin = QDoubleSpinBox(self)
        self.double_spin.setGeometry(10,30,100,25)
        self.double_spin.setSingleStep(0.1)
        self.double_spin.setDecimals(3)
        
        
        self.resize(800,500)
        self.show()
        
        
app = QApplication([])
window = Main()
app.exec()