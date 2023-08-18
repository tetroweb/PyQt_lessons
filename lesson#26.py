#------------------------------------------QFontDialog-------------------------
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.button = QPushButton("Font settings",self)
        self.button.clicked.connect(self.font_change)
        
        self.label = QLabel("Label",self)
        self.label.move(25,100)        
        
        self.resize(1200,500)
        self.show()
        
    def font_change(self):
        self.dialog = QFontDialog()
        self.dialog.exec()
        
        font =self.dialog.selectedFont()
        self.label.setFont(font)
        self.label.adjustSize()
        
app = QApplication([])
window = main()
app.exec()