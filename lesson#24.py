#-------------------------QHeaderView-------------------
from PyQt5.QtWidgets import* 
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.hbox = QHBoxLayout(self)
        self.tree = QTreeWidget()
        self.table = QTableWidget(5,5)
        self.hbox.addWidget(self.tree)
        self.hbox.addWidget(self.table)
        
        self.tree.setColumnCount(3)
        self.tree.setHeaderLabels(["Header 1","Header 2","Header 3"])
        self.table.setHorizontalHeaderLabels(["Header 1","Header 2","Header 3"])
        
        print(self.tree.header().count())
        print(self.table.horizontalHeader().count())
        
        self.tree.header().hideSection(2)# showSection()
        self.table.horizontalHeader().hideSection(2)
        
        # self.tree.header().setMaximumSectionSize(50)
        self.tree.header().setDefaultSectionSize(100)
        self.tree.header().setStretchLastSection(False)
        
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)#ınteractive
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        self.tree.header().setSectionsClickable(True)
        self.table.horizontalHeader().setSectionsClickable(False)
        
        self.tree.header().setFirstSectionMovable(True)
        
        self.resize(800,500)
        self.show()
        
        
app = QApplication([])
window = main()
app.exec()