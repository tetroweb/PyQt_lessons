from PyQt5.QtWidgets import* 
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.table = QTableWidget(5,5,self)
        self.table.setGeometry(20,20,600,450)
        
        # self.table.setColumnHidden(2,True)
        # self.table.setRowHidden(2,True)        
                
        self.table.setRowHeight(0,200)
        self.table.setColumnWidth(0,200)
        
        # self.table.setShowGrid(False)
        self.table.setGridStyle(Qt.DashLine)#Solidline dashline dotline
        
        self.table.setSortingEnabled(True)
        
        # self.table.setSpan(0,0,1,4) expand column or row
        
        self.item = QTableWidgetItem()
        self.item.setText("Pennnnnnn nnnnnnnnnnnnnnnnnnnnnn")
        self.table.setItem(0,0,self.item)
        self.table.setWordWrap(True)
        
        self.resize(800,500)
        self.show()
        
        
app = QApplication([])
window = main()
app.exec()