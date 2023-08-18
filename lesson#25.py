#------------------------------------------QAbstarctItemView-------------------------
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.hbox = QHBoxLayout(self)
        self.list = QListWidget()
        self.tree = QTreeWidget()
        self.table = QTableWidget(3,3)
        
        self.tree.setColumnCount(3)
        
        self.hbox.addWidget(self.list)
        self.hbox.addWidget(self.tree)
        self.hbox.addWidget(self.table)
        
        self.list.addItems(["Pen","Book","Ruler","Eraser","Notebook"])
        
        self.item = QTreeWidgetItem()
        self.item.setText(0,"item")
        self.tree.addTopLevelItems([self.item,self.item.clone(),self.item.clone(),self.item.clone(),self.item.clone(),self.item.clone()])
        
        self.list.setAlternatingRowColors(True)
        self.tree.setAlternatingRowColors(True)
        self.table.setAlternatingRowColors(True)
        
        self.list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tree.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        
        self.list.setSelectionMode(QAbstractItemView.MultiSelection)
        self.tree.setSelectionMode(QAbstractItemView.MultiSelection)
        self.table.setSelectionMode(QAbstractItemView.MultiSelection)
        
        self.list.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tree.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table.setSelectionMode(QAbstractItemView.ExtendedSelection)
        
        # self.tree.setSelectionBehavior(QAbstractItemView.SelectItems)
        
        # self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        
        # self.table.setSelectionBehavior(QAbstractItemView.SelectColumns)

        self.list.setDragEnabled(True)
        self.tree.setDragEnabled(True)
        self.table.setDragEnabled(True)
        
        
        self.list.setDragDropMode(QAbstractItemView.DragDrop)#Drag make a new clone
        self.tree.setDragDropMode(QAbstractItemView.InternalMove)#Move the real data
        self.table.setDragDropMode(QAbstractItemView.DragDrop)
        
        
        
        self.resize(1200,500)
        self.show()
        
        
app = QApplication([])
window = main()
app.exec()
    