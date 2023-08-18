#----------------------------QTableWidget----------------------------
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.table = QTableWidget(5,5,self)
        self.table.setGeometry(20,20,700,450)
        
        print(self.table.columnCount())
        print(self.table.rowCount())
        
        self.table.setColumnCount(10)
        self.table.setRowCount(10)
        
        self.item1 = QTableWidgetItem()
        self.item1.setText("item 1")
        
        self.table.setItem(2,2,self.item1)
        
        self.table.setHorizontalHeaderItem(2,self.item1.clone())
        self.table.setHorizontalHeaderLabels(["Title 1","Title 2","Title 3"])
        
        self.table.setVerticalHeaderItem(3,self.item1.clone())
        
        self.table.setCurrentCell(4,4)
        self.table.setCurrentItem(self.item1)
        print(self.table.currentItem().text())
        
        self.resize(800,500)
        self.show()
        
        
app = QApplication([])
window = main()
app.exec()
