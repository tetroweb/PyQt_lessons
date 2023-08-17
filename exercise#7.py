from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

font1 = QFont("Tahoma",18)
font2 = QFont("Tahoma",12)


class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.hbox = QHBoxLayout(self)
        self.vbox_left = QVBoxLayout()
        self.vbox_right = QVBoxLayout()
        self.hbox.addLayout(self.vbox_left)
        self.hbox.addLayout(self.vbox_right)
        
        self.vbox_right_setup()
        self.vbox_left_setup()
        
        
        
        self.resize(500,500)
        self.show()
    
    def get_info(self,c):
        for i in range(5):
            self.label_list[i].setText(self.dict_item[c.text()][i])
    
        
    def vbox_left_setup(self):
        self.list = QListWidget()
        self.list.setFont(font2)
        self.list.setViewMode(QListView.IconMode)
        self.item1 = QListWidgetItem("Acer",self.list)
        self.item2 = QListWidgetItem("Monster",self.list)
        self.item3 = QListWidgetItem("Asus",self.list)
        self.list.setFlow(QListView.TopToBottom)
        
        self.list.currentItemChanged.connect(self.get_info)
        
        self.dict_item = {
            "Acer" : ["1 TB","4 GB","2 GB","Yes","3500 TL"],
            "Monster" : ["2 TB","16 GB","8 GB","Yes","35000 TL"],
            "Asus" : ["1 TB","16 GB","12 GB","Yes","25000 TL"]
            
        }
        
        self.vbox_left.addWidget(self.list)
        
    def vbox_right_setup(self):
        self.label = QLabel("Product Properties")
        self.label.setFrameShape(QFrame.Panel)
        self.label.setFont(font1)
        self.vbox_right.addWidget(self.label)
        self.vbox_right.setAlignment(Qt.AlignTop)
        
        self.form=QFormLayout()
        self.vbox_right.addLayout(self.form)
        
        self.label1 = QLabel("Properties")
        self.label2 = QLabel("Properties")
        self.label3 = QLabel("Properties")
        self.label4 = QLabel("Properties")
        self.label5 = QLabel("Properties")
        self.label6 = QLabel("Memory :")
        self.label7 = QLabel("Ram Memory :")
        self.label8 =QLabel("VRam :")
        self.label9 = QLabel("Avaliable :")
        self.label10 = QLabel("Price :")
        
        self.form.addRow(self.label6,self.label1)
        self.form.addRow(self.label7,self.label2)
        self.form.addRow(self.label8,self.label3)
        self.form.addRow(self.label9,self.label4)
        self.form.addRow(self.label10,self.label5)

        self.label_list = [self.label1,self.label2,self.label3,self.label4,self.label5,self.label6,self.label7,self.label8,self.label9,self.label10 ]
        for i in self.label_list:
            i.setFont(font2)
app = QApplication([])
window = main()
app.exec()