#---------------------QTreeWidget-----------------------
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.tree = QTreeWidget(self)
        self.tree.setGeometry(20,20,300,400)
        self.tree.setHeaderLabel("Header")
        
        self.item1 = QTreeWidgetItem()
        self.item1.setText(0,"item 1")
        self.item1.setText(1,"./")
        
        self.item2 = QTreeWidgetItem()
        self.item2.setText(0,"item 2")
        
        self.item3 = QTreeWidgetItem()
        self.item3.setText(0,"item 3")
        
        self.tree.addTopLevelItem(self.item1)
        self.tree.addTopLevelItems([self.item2,self.item3])
        self.tree.insertTopLevelItem(2,self.item1.clone())
        
        self.tree.setHeaderItem(self.item3.clone())
        
        self.tree.setColumnCount(3)
        self.tree.setHeaderLabels(["Klasör","Yolu","Değiştirme tarihi"])
        
        
        print(self.tree.topLevelItemCount())
        print(self.tree.topLevelItem(0).text(1))
        print(self.tree.indexOfTopLevelItem(self.item3))
        
        self.tree.setCurrentItem(self.item3)
        
        self.item1.addChildren([self.item2.clone(),self.item2.clone(),self.item2.clone()])
        # self.tree.setItemsExpandable(False)
        self.tree.expandItem(self.item1)
        self.tree.collapseItem(self.item1)
        
        
        self.resize(800,500)
        self.show()
        
        
app = QApplication([])
window = main()
app.exec()