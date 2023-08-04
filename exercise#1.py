from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import * 

class Main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.label_km = QLabel("the path taken",self)
        self.label_avr = QLabel("average fuel consume",self)
        self.label_price = QLabel("Price",self)
        self.label_res =QLabel("Result",self)
        
        self.label_res.setFont(QFont("Tahoma",12))
        
        self.line_km = QLineEdit(self)
        self.line_avr = QLineEdit(self)
        self.line_price = QLineEdit(self)
        
        
        self.line_km.move(150,20)
        self.line_avr.move(150,60)
        self.line_price.move(150,100)
        
        self.button = QPushButton("click me ",self)
        self.button.setFont(QFont("Tahoma",12))
        self.button.move(120,140)
        
        self.label_km.move(20,20)
        self.label_avr.move(20,60)
        self.label_price.move(20,100)
        self.label_res.move(240,140)
        
        self.label_error = QLabel("Error",self)
        self.label_error.move(50,180)
        self.label_error.resize(250,50)
        self.label_error.setAlignment(Qt.AlignCenter)
        
        self.button.clicked.connect(self.count)
        self.setWindowTitle("fuel price")
        self.resize(350,250)
        self.show()
        
    def count(self):
        #does all datas entered
        #does all datas number
        #does all datas positive
        
        self.line_list = [self.line_km,self.line_avr,self.line_price]
        
        for i in self.line_list:
            if i.text().strip() != "":
                if i.text().replace(".","").isnumeric() or i.text().replace(",","").isnumeric():
                    pass
                else:
                    self.label_error.setText("Please only enter number")
                    break
            else:
                self.label_error.setText("Please fill the blank")
                break
        else:
            result = float(self.line_km.text().replace(",","."))*float(self.line_avr.text().replace(",","."))*float(self.line_price.text().replace(",","."))/100
            self.label_res.setText("%0.2f" %result)#The expression "%0.2f" % result formats the floating-point number "result" with two decimal places.
            self.label_error.setText("Error")
app = QApplication([])
window = Main()
app.exec()



