from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.hbox = QHBoxLayout(self)
        self.vbox_left = QVBoxLayout()
        self.vbox_right = QVBoxLayout()
        self.hbox.addLayout(self.vbox_left)
        self.hbox.addLayout(self.vbox_right)
        
        self.vbox_left_setup()
        self.vbox_right_setup()
        
        
        self.resize(400,500)
        self.show()
        
    def vbox_left_setup(self):
        self.list = QListWidget()
        self.vbox_left.addWidget(self.list)
        
    def vbox_right_setup(self):
        self.label = QLabel("Product Properties")
        self.vbox_right.addWidget(self.label)
        self.vbox_right.setAlignment(Qt.AlignVCenter)

app = QApplication([])
window = main()
app.exec()