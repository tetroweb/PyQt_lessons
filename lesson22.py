#----------------------QTreeWidget#2---------------------------
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.tree = QTreeWidget(self)
        self.tree.setGeometry(20,20,450,450)
        
        self.tree.setHeaderLabels(["Header 1","Header 2","Header 3"])
        self.tree.setColumnCount(3)       
        
        for i in range(10):
            self.item1 = QTreeWidgetItem()
            self.item1.setText(0,"Item %d" %i)
            self.item1.addChildren([self.item1.clone(),self.item1.clone(),self.item1.clone()])
            self.tree.addTopLevelItem(self.item1)
        
        self.tree.setColumnWidth(0,90)
        self.tree.resizeColumnToContents(0)#resize column width according to content width
        
        # self.tree.setExpandsOnDoubleClick(False) top label open 2 click
        
        # self.tree.setIndentation(0)# edit all items length to the left
        
        self.tree.setSortingEnabled(True)
        self.tree.expandAll()
        
        
        self.resize(800,500)
        self.show()
        
        
app = QApplication([])
window = main()
app.exec()