#-------------------------QGridLayout---------------------------- 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.grid = QGridLayout(self)
        
        # self.grid.addWidget(QPushButton("click1"),0,0,1,1)#(number of rows,number of columns,how many rows it will occupy,how many columns it will occupy)
        # self.grid.addWidget(QPushButton("click2"),0,1,1,1)
        # self.grid.addWidget(QPushButton("click3"),0,2,1,1)
        # self.grid.addWidget(QPushButton("click4"),1,0,1,2)
        
        self.grid.setSpacing(0)
        
        for i in range(3):
            for j in range(3):
                self.grid.addWidget(QPushButton("click"),i,j,1,1)
        
        
        
        self.resize(800,500)
        self.show()



app = QApplication([])
window = main()    
app.exec()