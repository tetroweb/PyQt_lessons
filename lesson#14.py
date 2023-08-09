#--------------------------QFormLayout----------------
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import * 


class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.form = QFormLayout(self)
        
        self.form.addWidget(QPushButton("click form"))
        self.form.addRow(QPushButton("name"),QLineEdit())
        self.form.addRow(QPushButton("surname"),QLineEdit())
        
        self.form.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        
        self.form.setFormAlignment(Qt.AlignBottom)
        
        self.form.removeRow(1)
        
        self.resize(800,500)
        self.show()
        
        
app = QApplication([])
window = main()
app.exec()