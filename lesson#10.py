#------------------QTextEdit-QPlainTextEdit------------
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import * 

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.tex_edit = QTextEdit(self)
        self.tex_edit.setText("this is the sample text")
        
        # Displays HTML code as is
        self.plain_text = QPlainTextEdit(self)
        self.plain_text.setPlainText("this is the sample text")
        self.plain_text.move(400, 0)
        
        self.button = QPushButton("Insert", self)
        self.button.clicked.connect(self.insert)
        self.button.move(0, 400)
        self.resize(800, 500)
        self.show()
        
    def insert(self):
        # self.tex_edit.insertHtml("<b>bold text</b>")
        self.tex_edit.setFontFamily("Verdana")  # Applies to selected text
        self.tex_edit.setFontPointSize(10)  # Applies to selected text


app = QApplication([])
window = Main()
app.exec()