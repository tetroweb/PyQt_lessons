from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

font1 = QFont("Tahoma",30)
font2 = QFont("Consolas",18)

class button(QPushButton):
    def __init__(self,text,line):
        super().__init__(text,line)
        
        self.line = line
        self.clicked.connect(self.control)
    def control(self):
        if self.line.text() == "0":
            if self.text().isnumeric():
                self.line.setText(self.text())


class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.vbox =QVBoxLayout(self)
        self.vbox.setContentsMargins(4,4,4,4)
        self.vbox.setAlignment(Qt.AlignTop)
        
        self.vbox.setSpacing(1)
        
        self.line = QLineEdit("0")
        self.line.setFont(font1)
        self.line.setMinimumHeight(100)
        self.vbox.addWidget(self.line)
        self.line.setAlignment(Qt.AlignRight)
        self.line.setFrame(False)
        self.line.setReadOnly(True)
        self.button_list = [
            button("x^2",self.line),
            button("C",self.line),
            button("<-",self.line),
            button("/",self.line),
            button("7",self.line),
            button("8",self.line),
            button("9",self.line),
            button("x",self.line),
            button("4",self.line),
            button("5",self.line),
            button("6",self.line),
            button("+",self.line),
            button("1",self.line),
            button("2",self.line),
            button("3",self.line),
            button("-",self.line),
            button("",self.line),
            button("0",self.line),
            button(",",self.line),
            button("=",self.line)
            
        ]
        
        self.grid = QGridLayout()
        self.vbox.addLayout(self.grid)
        self.grid.setSpacing(3)
        
        
        for i in range(4):
            self.grid.addWidget(self.button_list[i],1,i,1,1)
            self.button_list[i].setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
            self.button_list[i].setFont(font2)
            self.button_list[i].setStyleSheet("QPushButton{border:none ; background-color:#ddd;}QPushButton:hover{background-color:#bbb;}")
            
            
        for i in range(4,len(self.button_list)):
            self.grid.addWidget(self.button_list[i])
            self.button_list[i].setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
            self.button_list[i].setFont(font2)
            self.button_list[i].setStyleSheet("QPushButton{border:none ; backgorund-color: #ddd;}QPushButton:hover{background-color:#bbb;}")

            if self.button_list[i].text().isnumeric() or self.button_list[i].text() in [",", ""]:
                self.button_list[i].setStyleSheet("QPushButton{border:none; background-color: white;}QPushButton:hover{background-color:#bbb;}")
            if self.button_list[i].text() == "=":
                self.button_list[i].setStyleSheet("QPushButton{border:none ; background-color : lightskyblue;}QPushButton:hover{background-color:#bbb;}")   
            if self.button_list[i].text() in ["+","-","x"]:
                self.button_list[i].setStyleSheet("QPushButton{border:none ; background-color:#ddd;}QPushButton:hover{background-color:#bbb;}")
                
        self.setStyleSheet("background-color:#ccc;")
        self.resize(310,450)
        self.show()



app = QApplication([])
window = main()    
app.exec()