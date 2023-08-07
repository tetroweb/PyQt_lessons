#-----------------QComboBox(Açılır Liste)--------------------------
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 


d_city = {"İstanbul" : ["Adalar","Arnavutköy","Ataşehir","Avcilar","Bagcilar"],
"Antalya": ["Kaş","Kemer","Kepez","Konyaalti"]}

class Main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.combo = QComboBox(self)
        self.combo.setGeometry(20,20,120,25)
        
        self.combo.addItem("Book")#[0]
        self.combo.addItem("Pencil")#[1]
        self.combo.addItem("Notebook")#[2]
        
        #self.combo.removeItem(1)
        self.combo.setItemText(2,"Pencilcase")
        
        print(self.combo.currentIndex())
        print(self.combo.currentText())
        
        self.combo.setCurrentIndex(2)
        # self.combo.setCurrentText("Pencilcase")
        
        self.combo.insertItem(1,"İnput")
        self.combo.insertSeparator(2)
        self.combo.clear()
        
        self.radio1 = QRadioButton("İstanbul",self)
        self.radio2 = QRadioButton("Antalya",self)
        
        self.radio2.move(80,0)
        
        self.radio1.clicked.connect(self.listing)
        self.radio2.clicked.connect(self.listing)
        
        
        
        self.resize(800,500)
        self.show()
        
    def listing(self):
        if self.radio1.isChecked():
            self.combo.clear()
            self.combo.addItems(d_city["İstanbul"])
        if self.radio2.isChecked():
            self.combo.addItems(d_city["Antalya"])
            
        
        
        
app = QApplication([])
window = Main()
app.exec()