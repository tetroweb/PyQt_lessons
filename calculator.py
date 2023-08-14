from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

font1 = QFont("Tahoma",30)
font2 = QFont("Consolas",18)

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

        self.button_list = [
            QPushButton("x^2"),
            QPushButton("C"),
            QPushButton("<-"),
            QPushButton("/"),
            QPushButton("7"),
            QPushButton("8"),
            QPushButton("9"),
            QPushButton("x"),
            QPushButton("4"),
            QPushButton("5"),
            QPushButton("6"),
            QPushButton("+"),
            QPushButton("1"),
            QPushButton("2"),
            QPushButton("3"),
            QPushButton("-"),
            QPushButton(""),
            QPushButton("0"),
            QPushButton(","),
            QPushButton("=")
            
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