#-------------------------QScroolArea---------------------------- 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *




class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.area = QScrollArea(self)
        self.area.setGeometry(10,10,250,200)
        
        self.widget = QWidget()
        
        self.vbox = QVBoxLayout(self.widget)
        
        for i in range(15):
            self.vbox.addWidget(QPushButton("click"))
        
        self.area.setWidget(self.widget)
        self.area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.area.setWidgetResizable(True)
        
        self.resize(300,250)
        self.show()



app = QApplication([])
window = main()    
app.exec()