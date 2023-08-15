#----------------------QGroupBox-----------------
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.group = QGroupBox(self)
        self.group.setTitle("Softwork Controller")
        self.group.setGeometry(0,0,400,250)
        self.group.setAlignment(Qt.AlignCenter)
        self.group.setCheckable(True)
        self.group.setChecked(False)
        
        self.vbox = QVBoxLayout()
        self.check1 = QCheckBox("Check1")
        self.check2 = QCheckBox("Check2")
        
        self.vbox.addWidget(self.check1)
        self.vbox.addWidget(self.check2)
        
        
        self.group.setLayout(self.vbox)
        
        self.resize(800,500)
        self.show()
        
        
app = QApplication([])
window = main()
app.exec()