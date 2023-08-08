#------------------QTextEdit-QPlainTextEdit------------
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import * 

#QTextEdit'in QLineEdit'ten farkı birden çok satır içermesi
class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.tex_edit = QTextEdit(self)
        self.tex_edit.setText("this is the sample write")
        
        
        #html kodlarını olduğu gibi gösterir
        self.plain_text = QPlainTextEdit(self)
        self.plain_text.setPlainText("this is the sample write")
        self.plain_text.move(400,0)
        
        self.button = QPushButton("Insert",self)
        self.button.clicked.connect(self.insert)
        self.button.move(0,400)
        self.resize(800,500)
        self.show()
        
    def insert(self):
        # self.tex_edit.insertHtml("<b>bold write</b>")
        self.tex_edit.setFontFamily("Verdana")#seçilmiş metinler için geçerli
        self.tex_edit.setFontPointSize(10)#seçilmiş metinler için geçerlidir


app = QApplication([])
window = Main()
app.exec()