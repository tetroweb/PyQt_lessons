#--------------------QHBoxLayout-QVBoxLayout--------
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import * 

class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.hbox = QHBoxLayout(self)
        
        self.button =QPushButton("Click")
        self.hbox.addWidget(self.button)
        
        self.hbox.addSpacing(100)
        
        self.hbox.addWidget(QPushButton("click2"))
        
        self.vbox = QVBoxLayout()
        self.hbox.addLayout(self.vbox)
        
        self.vbox.addWidget(QPushButton("click3"))
        self.vbox.addWidget(QPushButton("click4"))
        self.vbox.addWidget(QPushButton("click5"))

        self.hbox.setContentsMargins(100,0,0,0)

        self.hbox.setSpacing(50)
        
        self.hbox.setDirection(QBoxLayout.RightToLeft)
        
        self.resize(800,500)
        self.show()
        
        
        
        
app = QApplication([])
window = main()
app.exec()