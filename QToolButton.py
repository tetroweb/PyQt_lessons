#----------------------QToolButton------------------
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.tbutton = QToolButton(self)
        self.tbutton.setGeometry(50,50,80,80)
        
        self.tbutton.setText("Demo")
        
        # self.tbutton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon) -> Set this to display text beside the icon when there is an icon.

        self.tbutton.setToolTip("Ball")  # Set the tooltip text when the cursor hovers over the button
        self.tbutton.setToolTipDuration(2000)  # Set the duration of the tooltip display
        print(self.tbutton.toolTip())  # Print the tooltip text

        self.tbutton.setPopupMode(QToolButton.MenuButtonPopup)
        self.action = QAction("Action1")  # Create an action with the name "Action1"
        self.tbutton.addAction(self.action)  # Add the action to the button
        self.action.setShortcut("Ctrl+x")  # Set a shortcut for the added action (Ctrl + x)

        self.resize(800,500)
        self.show()
        
        
        
        
app = QApplication([])
window = Main()
app.exec()