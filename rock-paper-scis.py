from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import random as r 


font = QFont("Comic Sans MS",18)

winner = [("Rock","Scissor"),("Paper","Rock"),("Scissor","Paper")]
loser= [("Rock","Paper"),("Paper","Scissor"),("Scissor","Rock")]

class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.vbox = QVBoxLayout(self)
        
        self.hbox = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        
        self.rock_button = QToolButton()
        self.rock_button.setText("Rock")
        self.rock_button.setMinimumHeight(60)
        self.rock_button.setIcon(QIcon("rock.png"))
        self.rock_button.setIconSize(QSize(80,80))
        self.rock_button.setFont(QFont(font))
        
        self.paper_button = QToolButton()
        self.paper_button.setText("Paper")
        self.paper_button.setMinimumHeight(60)
        self.paper_button.setIcon(QIcon("paper.png"))
        self.paper_button.setIconSize(QSize(80,80))
        self.paper_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.paper_button.setFont(QFont(font))
        
        self.scissor_button = QToolButton()
        self.scissor_button.setText("Scissor")
        self.scissor_button.setMinimumHeight(60)
        self.scissor_button.setIcon(QIcon("scissor.png"))
        self.scissor_button.setIconSize(QSize(80,80))
        self.scissor_button.setFont(QFont(font))
        
        self.comp_label = QLabel("Computer")
        self.hbox2.addWidget(self.comp_label)
        self.comp_label.setFont(QFont(font))
        
        self.comp_choose = QLabel("Choose")
        self.hbox2.addWidget(self.comp_choose)
        self.comp_choose.setFont(QFont(font))
        
        self.res_label = QLabel("Result")
        self.res_label.setAlignment(Qt.AlignCenter)
        self.res_label.setMinimumHeight(80)
        self.res_label.setFont(QFont(font))
        
        
        self.score1 = QLabel("0")
        self.score1.setAlignment(Qt.AlignCenter)
        self.score1.setMaximumWidth(80)
        self.score1.setFrameShape(QFrame.Box)
        self.score1.setFont(QFont(font))
        self.hbox3.addWidget(self.score1)
        
        
        self.score2 = QLabel("0")
        self.score2.setAlignment(Qt.AlignCenter)
        self.score2.setMaximumWidth(80)
        self.score2.setFrameShape(QFrame.Box)
        self.score2.setFont(QFont(font))
        self.hbox3.addWidget(self.score2)
        self.hbox3.setSpacing(110)
        
        self.hbox.addWidget(self.rock_button)
        self.hbox.addWidget(self.paper_button)
        self.hbox.addWidget(self.scissor_button)
        
        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addWidget(self.res_label)
        self.vbox.addLayout(self.hbox3)
        
        self.resize(350,250)
        self.show()
        
        self.rock_button.clicked.connect(lambda :self.compare("Rock"))
        self.paper_button.clicked.connect(lambda :self.compare("Paper"))
        self.scissor_button.clicked.connect(lambda :self.compare("Scissor"))
        
    def compare(self,choose):
        random_pc = r.choice(["Rock","Paper","Scissor"])
        choose_tuple = (choose,random_pc)
        self.comp_choose.setText(random_pc)
        if choose_tuple in winner:
            self.res_label.setText("Win :)")
            self.score1.setText(str(int(self.score1.text())+1))
            self.res_label.setStyleSheet("color : blue;")
        elif choose_tuple in loser:
            self.res_label.setText("Lose :(")
            self.score2.setText(str(int(self.score2.text())+1))
            self.res_label.setStyleSheet("color : red;")
        else:
            self.res_label.setText("Draw")
            self.res_label.setStyleSheet("color : green;")
        
app = QApplication([])
window = main()
app.exec()