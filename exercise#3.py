from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.QtGui import *


class Main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.label_name = QLabel("Name :",self)
        self.label_name.move(20,20)
        
        self.label_surname = QLabel("Surname :",self)
        self.label_surname.move(180,20)
        
        self.label_age = QLabel("Age :",self)
        self.label_age.move(20,100)
        
        self.label_gender = QLabel("Gender :",self)
        self.label_gender.move(20,180)
        
        self.label_mail = QLabel("Email :",self)
        self.label_mail.move(20,260)
        
        self.label_phone = QLabel("Phone Number :",self)
        self.label_phone.move(20,340)
        
        self.label_length = QLabel("Length :",self)
        self.label_length.move(20,420)
        
        self.label_weight = QLabel("Weight :",self)
        self.label_weight.move(180,420)
        
        self.label_blood = QLabel("Blood Type :",self)
        self.label_blood.move(20,500)
        
        self.line_name = QLineEdit(self)
        self.line_surname = QLineEdit(self)
        self.line_age = QLineEdit(self)
        # self.line_gender = QLineEdit(self)
        self.line_mail  = QLineEdit(self)
        self.line_phone= QLineEdit(self)
        self.line_length= QLineEdit(self)
        self.line_weight= QLineEdit(self)
        # self.line_blood= QLineEdit(self)       
               
                
        self.line_name.move(20,40)
        self.line_surname.move(180,40)
        self.line_age.move(20,120)
        # self.line_gender.move(20,200)
        self.line_mail.move(20,280)
        self.line_phone.move(20,360)
        self.line_length.move(20,440)
        self.line_weight.move(180,440)
        # self.line_blood.move(20,520)
        
        self.radio1 = QRadioButton("Man",self)
        self.radio2 = QRadioButton("Woman",self)
        
        self.radio1.move(20,200)
        self.radio2.move(100,200)
        
        self.radio3 = QRadioButton("",self)
        self.radio3.setVisible(False)
        
        self.combo = QComboBox(self)
        self.combo.addItems(["A+","A-","B+","B-","0+","0-","AB+","AB-"])
        self.combo.move(20,520)
        
        self.button_1 = QPushButton("Save",self)
        self.button_2 = QPushButton("Delete",self)
        self.button_3 = QPushButton("Exit",self)
        
        self.button_1.move(100,600)
        self.button_2.move(210,600)    
        self.button_3.move(320,600)    
        
        self.frame = QFrame(self)
        self.frame.setFrameShape(QFrame.VLine)
        self.frame.move(350,50)
        self.frame.setLineWidth(5)
        self.frame.resize(3,550)
         
        self.button_3.clicked.connect(self.close) 
        self.button_2.clicked.connect(self.reset)
        
        self.resize(800,650)
        self.show()
        
    def reset(self):
        self.line_name.setText("")
        self.line_surname.setText("")
        self.line_age.setText("")
        self.line_mail.setText("")
        self.line_phone.setText("")
        self.line_length.setText("")
        self.line_weight.setText("")
        
        self.radio3.setChecked(True)
        self.combo.setCurrentIndex(-1)#use for reset comboBox
        
    
        
app = QApplication([])
window = Main()
app.exec()