#---------------------GooglWindow----------------------
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

#css codes---------------------------------------------
css = """
        QTabBar::tab{
            width: 100px;
            height: 35px;
            padding-right: 90px;
            border:none ;
        }
        QTabBar::tab::hover{
            background-color : whitesmoke;
        }
        QTabBar::tab::selected{
            background-color : white;
            border-top-left-radius: 8px;
            border-top-right-radius: 8px;
        }
        QTabBar::close-button{
            image: url(red_cross.png);
            padding: 2px;
            border-radius: 8px;
            
        }
        QTabBar::close-button::hover{
            
            background-color: #bbb;
            
        }
        QToolButton{
            padding:0 0 2px 2px; 
            border:none; 
            height:22px; 
            width:22px; 
            border-radius: 12px; 
            }
            QToolButton::hover{
            background-color: #bbb;
            }
            QToolButton::pressed{
            background-color:#ddd;
            }
        
"""

class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.hbox = QHBoxLayout(self)
        self.hbox.setContentsMargins(0,0,0,0)
        self.tab_widget = QTabWidget()
        self.hbox.addWidget(self.tab_widget)
        
        self.tab_widget.addTab(QWidget(),"Tab 1")
        self.tab_widget.addTab(QWidget(),"Tab 2")
        self.tab_widget.addTab(QWidget(),"Tab 3")
        
        self.tab_widget.setStyleSheet(css)
        self.tab_widget.setTabsClosable(True)
        
        self.tab_widget.tabCloseRequested.connect(self.tab_close)#some methods output is index and connect index with our function
        
        self.tbutton=QToolButton(self.tab_widget)
        
        self.tbutton.setText("+")
        
        w = self.tab_widget.tabBar().sizeHint().width()#width the tabbar
        self.tbutton.move(w+8,5)
        
        self.tbutton.setFont(QFont("Calibri",15))
        
        self.tbutton.clicked.connect(self.addTab)
        
        self.tbutton.setStyleSheet(css)
        
        
        self.resize(800,500)
        self.show()
    
    def tab_close(self,i):
        self.tab_widget.removeTab(i)
        w = self.tab_widget.tabBar().sizeHint().width()
        self.tbutton.move(w+8,5)
    
    def addTab(self):
        self.tab_widget.addTab(QWidget(),"New Tab")
        w = self.tab_widget.tabBar().sizeHint().width()
        self.tbutton.move(w+8,5)
    
    
     
app = QApplication([])
window = main()
app.exec()