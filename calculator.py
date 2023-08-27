from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

font1 = QFont("Tahoma",30)
font2 = QFont("Consolas",18)

class button(QPushButton):
    def __init__(self,text,line):
        super().__init__(text)
        
        self.line = line
        self.clicked.connect(self.control)
    def control(self):
        if self.text() =="←":
            self.line.backspace()
            if self.line.text() == "":
                self.line.setText("0") 
            
        if self.text() =="C":
            self.line.setText("0")    
        
        if self.line.text() == "0":
            if self.text().isnumeric():
                self.line.setText(self.text())
            else:
                if self.text() not in ["x^2","C","←","=",","]:
                    self.line.setText(self.line.text()+self.text())
        else:
            if self.text() not in ["x^2","C","←","=",","]:
                if self.line.text()[-1].isnumeric():
                    self.line.setText(self.line.text()+self.text())
                else:
                    if self.text().isnumeric():
                        self.line.setText(self.line.text()+self.text())
                    else:
                        # self.line.backspace()#delete last character in text
                        self.line.setText(self.line.text()[:-1]+self.text())   
        if self.text() == ",":
            c = self.line.text().count(",")
            if c == 0:
                if self.line.text()[-1].isnumeric():
                    self.line.setText(self.line.text()+",")
                else:
                    self.line.setText(self.line.text()[:-1]+",")
            if c >= 1:
                result = self.line.text().split(",")
                if result[-1].isnumeric():
                    pass
                else:
                    if result[-1][:-1].isnumeric():
                        pass
                    else:
                        self.line.setText(self.line.text()+",")
                    
                    
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
        self.line.setFocusPolicy(Qt.NoFocus)
        self.button_list = [
            button("x^2",self.line),
            button("C",self.line),
            button("←",self.line),
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
        self.key_list = [
            None,
            Qt.Key_Escape,
            Qt.Key_Backspace,
            Qt.Key_Slash,
            Qt.Key_7,
            Qt.Key_8,
            Qt.Key_9,
            Qt.Key_Asterisk,
            Qt.Key_4,
            Qt.Key_5,
            Qt.Key_6,
            Qt.Key_Plus,
            Qt.Key_1,
            Qt.Key_2,
            Qt.Key_3,
            Qt.Key_Minus,
            None,
            Qt.Key_0,
            Qt.Key_Comma,
            Qt.Key_Equal,
        ]
        
        self.list=["x","/","+","-"]
        
        self.grid = QGridLayout()
        self.vbox.addLayout(self.grid)
        self.grid.setSpacing(3)
        
        
        for i in range(4):
            self.grid.addWidget(self.button_list[i],1,i,1,1)
            self.button_list[i].setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
            self.button_list[i].setFont(font2)
            self.button_list[i].setStyleSheet("QPushButton{border:none ; background-color:#ddd;}QPushButton::hover{background-color:#bbb;}QPushButton::pressed{background-color:green;}")
            
            
        for i in range(4,len(self.button_list)):
            self.grid.addWidget(self.button_list[i])
            self.button_list[i].setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
            self.button_list[i].setFont(font2)
            self.button_list[i].setStyleSheet("QPushButton{border:none ; background-color:#ddd;}QPushButton::hover{background-color:#bbb;}")


            if self.button_list[i].text().isnumeric() or self.button_list[i].text() in [",", ""]:
                self.button_list[i].setStyleSheet("QPushButton{border:none; background-color: white;}QPushButton:hover{background-color:#bbb;}QPushButton::pressed{background-color:green;}")
            if self.button_list[i].text() == "=":
                self.button_list[i].setStyleSheet("QPushButton{border:none ; background-color : lightskyblue;}QPushButton:hover{background-color:#bbb;}QPushButton::pressed{background-color:green;}")   
            if self.button_list[i].text() in ["+","-","x"]:
                self.button_list[i].setStyleSheet("QPushButton{border:none ; background-color:#ddd;}QPushButton:hover{background-color:#bbb;}QPushButton::pressed{background-color:green;}")
                
        self.setStyleSheet("background-color:#ccc;")
        self.resize(310,450)
        self.show()
    
    def keyPressEvent(self,e):
        if e.key() in self.key_list:
            i =self.key_list.index(e.key())
            self.css = self.button_list[i].styleSheet()
            self.button_list[i].setStyleSheet("QPushButton{border:none;background-color:green;}")
            self.button_list[i].click()
    
    def keyReleaseEvent(self,e):
        if e.key() in self.key_list:
            i =self.key_list.index(e.key())
            self.button_list[i].setStyleSheet(self.css)
    
    def control(self,text):
        c = text.find("x")
        b = text.find("/")  
          
        if c != -1 and b !=-1:
            if c<b:
                pass
            elif b<c:
                result =text.split("/",1)
                self.slicing1(result[0])
                self.slicing2(result[1])
                count = float(self.num1)/float(self.num2)
                last_text = self.back1 + str(count) + self.back2
                print(last_text)
        elif c != -1 or b !=-1:
            pass
        else:
            pass  
    
    def slicing1(self,text):
        for i in range(len(text)-1,-1,-1):
            if text[i] in self.list:
                self.num1 = text[i+1:]
                self.back1 = text[:i+1]
                break
            if i ==0:
                self.num1 = text
                self.back1 = ""
            
    def slicing2(self,text):
        for i in range(0,len(text)):
            if text[i] in self.list:
                self.num2 = text[:i]
                self.back2 = text[i:]
                break
            if i ==len(text)[-1]:
                self.num2 = text
                self.back2 = ""
app = QApplication([])
window = main()    
app.exec()