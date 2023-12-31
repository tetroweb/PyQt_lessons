#---------------QRadioButton,QCheckBox-----------------
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget

class Main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.gender_label = QLabel(self)
        self.gender_label.setFrameShape(QFrame.Box)
        self.gender_label.setGeometry(0,0,100,100)
        
        self.radio1 = QRadioButton("Male",self.gender_label)#-> if use radio button once check properties use same family for radio button members
        self.radio1.move(20,22)
        self.radio2 = QRadioButton("Female",self.gender_label)
        self.radio2.move(20,40)
        
        self.label = QLabel("Which  country have you been ?",self)
        self.check1 = QCheckBox("Denizli",self)#-> check box provide more than check for the questions
        self.check2 = QCheckBox("Adana",self)
        self.check3 = QCheckBox("İstanbul",self)
        
        self.label.move(20,80)
        self.check1.move(20,120)
        self.check2.move(90,120)
        self.check3.move(160,120)
        
        self.check3.setCheckable(False)# destroy the choose ability
        
        self.check2.toggled.connect(self.check)#When an option is selected, it returns True.
        
        self.check2.setChecked(True)
        
        boolean =self.check1.isChecked()#It checks whether the button is selected for conditional options
        print(boolean)
        
        self.resize(800,500)
        self.show()
        
    def check(self , par):
        print(par)

app = QApplication([])
window = Main()
app.exec()
