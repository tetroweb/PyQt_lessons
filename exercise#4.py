#---------------------ColorSettings----------------
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import * 

class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.widget = QWidget(self)
        self.widget.setGeometry(20,20,300,250)
        
        self.widget.setStyleSheet("border : 2px solid black ; background-color : red ;")
        
        self.red = QLabel("red",self)
        self.green = QLabel("green",self)
        self.blue = QLabel("blue",self)
        
        self.red.move(20,280)
        self.green.move(20,310)
        self.blue.move(20,340)
        
        self.red_slider = QSlider(Qt.Horizontal,self)
        self.green_slider = QSlider(Qt.Horizontal,self)
        self.blue_slider = QSlider(Qt.Horizontal,self)
        
        self.red_slider.setGeometry(90,280,180,25)
        self.green_slider.setGeometry(90,310,180,25)
        self.blue_slider.setGeometry(90,340,180,25)
        
        self.red_value = QLabel("0",self)
        self.green_value = QLabel("0",self)
        self.blue_value = QLabel("0",self)
        
        self.red_value.move(305,280)
        self.green_value.move(305,310)
        self.blue_value.move(305,340)
        
        self.red_slider.setRange(0,255)
        self.green_slider.setRange(0,255)
        self.blue_slider.setRange(0,255)
        
        self.red_slider.valueChanged.connect(self.red_change)
        self.green_slider.valueChanged.connect(self.green_change)
        self.blue_slider.valueChanged.connect(self.blue_change)
        
        
        self.resize(800,500)
        self.show()
    
    def red_change(self,v):
        self.red_value.setText(str(v))
        self.red_value.adjustSize()
        self.widget.setStyleSheet("border : 2px solid black ; background-color : rgb(%d,%d,%d) ;" %(v,self.green_slider.value(),self.blue_slider.value()))
    
    def green_change(self,v):
        self.green_value.setText(str(v))
        self.green_value.adjustSize() 
        self.widget.setStyleSheet("border : 2px solid black ; background-color : rgb(%d,%d,%d) ;" %(self.red_slider.value(),v,self.blue_slider.value()))

    
    def blue_change(self,v):
        self.blue_value.setText(str(v))
        self.blue_value.adjustSize()    
        self.widget.setStyleSheet("border : 2px solid black ; background-color : rgb(%d,%d,%d) ;" %(self.red_slider.value(),self.green_slider.value(),v))



app = QApplication([])
window = main()
app.exec()