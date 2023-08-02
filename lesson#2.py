#-------------------Qlabel------------------------
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import * 



class Main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.label = QLabel("label", self)  # Used to create a label
        self.label.move(100, 100)  # Sets the position of the label
    
        self.label.setText("label 2" * 4)  # Allows us to change the text
        print(self.label.text())  # Returns the text as output
    
        self.label.setFont(QFont("Tahoma", 24, 100, True))  # Sets the text font (family, pointSize, bold, italic)
    
        self.label.setFrameShape(QFrame.Box)  # Adds a box frame shape around the label
        self.label.setLineWidth(10)  # Resizes the width of the label's frame
        self.label.setWordWrap(True)  # Wraps the text to the next line if it doesn't fit within the label's boundaries
    
    #-------------------------Alignment (aligns the text within the frame)-----------------------------
    
    #   self.label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
    
    #----------------------------------------------------------------------------------------
    
    #------------------------------------Clear-----------------------------------------------
    
    #   self.label.clear() -> Clears the text of the label
    
    #----------------------------------------------------------------------------------------
    
        self.label.resize(300, 300)
        self.label.adjustSize()  # Aligns and fits the text within the label
    
        self.resize(800, 500)
        self.show()
        
        
        
        
app = QApplication([])
window = Main()
app.exec()