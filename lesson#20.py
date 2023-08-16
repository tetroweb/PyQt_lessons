#--------------------------------------------QListWidgetItem--------------------------
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.list = QListWidget(self)
        self.list.setGeometry(20,20,300,400)
        
        self.item1 = QListWidgetItem("Item 1",self.list)
        self.item2 = QListWidgetItem("Item 2",self.list)
        self.item3 = QListWidgetItem("Item 3",self.list)
        
        self.item1.setFont(QFont("Calibri",24))
        self.item2.setFont(QFont("Calibri",24))
        self.item3.setFont(QFont("Calibri",24))
        
        self.item1.setTextAlignment(Qt.AlignRight)
        self.item2.setTextAlignment(Qt.AlignHCenter)
        
        self.item1.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable  | Qt.ItemIsEditable)
        self.item2.setSelected(True)
        self.item3.setHidden(True)
        
        self.item1.setToolTip("Show the content")
        self.resize(800,500)
        self.show()
        
        
app = QApplication([])
window = main()
app.exec()