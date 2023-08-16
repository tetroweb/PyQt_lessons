#----------------------------QListWidget--------------------
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.list_widget = QListWidget(self)
        self.list_widget.setGeometry(20,20,300,450)
        
        self.list_widget.addItem("Item 1")
        self.list_widget.addItems(["Pen","Pencil","Book"])
        
        self.item = QListWidgetItem("Ruler",self.list_widget)
        self.item2 = QListWidgetItem()
        self.item2.setText("Eraser")
        self.list_widget.addItem(self.item2)
        
        self.list_widget.insertItem(3,"note")
        
        print(self.list_widget.count())
        
        for i in range(120):
            self.list_widget.addItem(self.item.clone())
        
        self.list_widget.setCurrentItem(self.item)
        self.list_widget.setCurrentRow(3)
        
        print(self.list_widget.currentItem().text())
        print(self.list_widget.currentRow())
        
        self.list_widget.sortItems(Qt.AscendingOrder)
        
        item = self.list_widget.takeItem(1)
        print(item.text())
        item.setText("book 2")
        self.list_widget.insertItem(1,item)
        
        # self.list_widget.setFlow(QListView.LeftToRight)
        self.list_widget.setRowHidden(3,True)
        
        # self.list_widget.setViewMode(QListView.IconMode)
        self.list_widget.setWrapping(True)
        
        
        self.resize(800,500)
        self.show()
        
        
app = QApplication([])
window = main()
app.exec()