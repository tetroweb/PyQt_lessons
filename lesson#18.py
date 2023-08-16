#----------------QTabWidget-------------------
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class main(QWidget):
    def __init__(self):
        super().__init__()
        
        
        self.tab = QTabWidget(self)
        self.tab.setGeometry(10,10,300,300)
        
        self.widget1 =QWidget()
        self.button1 = QPushButton("click1",self.widget1)
        
        self.widget2 =QWidget()
        self.button2 = QPushButton("click2",self.widget2)
        
        self.widget3 =QWidget()
        self.button3 = QPushButton("click3",self.widget3)
        
        self.widget4 =QWidget()
        
        self.tab.addTab(self.widget1,QIcon("rock.png"),"Tab 1")
        self.tab.addTab(self.widget2,QIcon("rock.png"),"Tab 2")
        self.tab.addTab(self.widget3,QIcon("rock.png"),"Tab 3")
        
        # self.tab.removeTab(0)
        self.tab.insertTab(2,self.widget4,"Tab 4")        
        
        print(self.tab.indexOf(self.widget3))#write index which has belong
        
        print(self.tab.count())# write the tab count
        
        self.tab.setTabEnabled(2,False)# make the tab disable
        self.tab.setTabVisible(2,False)#make tab nonvisible not destroy
        
        self.tab.setTabToolTip(0,"show the tab 1 content ")
        
        self.tab.setMovable(True)
        self.tab.setTabsClosable(True)
        
        self.tab.setCurrentIndex(1)
        self.tab.setCurrentWidget(self.widget4)
        
        self.resize(800,500)
        self.show()
        
        
app = QApplication([])
window = main()
app.exec()

        