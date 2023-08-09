#------------------QSlider---------------------
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setGeometry(20,20,200,25)
        
        self.slider.setRange(10,150)
        self.slider.setValue(25)
        self.slider.setSliderPosition(30)
        
        self.slider.setTickPosition(QSlider.TicksLeft)
        self.slider.setTickInterval(10)
        
        
        
        
        self.label = QLabel(self)
        self.label.setText(str(self.slider.value()))
        self.label.setGeometry(240,20,100,25)
        
        
        
        self.resize(800,500)
        self.show()
        
        
        
app = QApplication([])
window = main()
app.exec()