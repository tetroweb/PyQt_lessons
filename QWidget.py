#-------------------------QWIDGET---------------------------- 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWidget(QWidget):
    def init(self):
        super().init() # Inherited from QWidget
        self.move(100, 100)  # Defines where the window will appear on the screen (origin: top-left corner) (x, y)
        print(self.pos())  # To confirm the window position

    #-------------------SIZE-------------------------
        self.setMinimumSize(1000, 800)  # Sets the minimum dimensions of the window
    #   self.setMinimumHeight() - for setting the minimum height
    #   self.setMinimumWidth()  - for setting the minimum width

        self.setMaximumSize(400, 400)  # Sets the maximum height and width of the window
    #   self.setMaximumHeight() - for setting the maximum height
    #   self.setMaximumWidth()  - for setting the maximum width

        self.setFixedSize(300, 300)  # Disables resizing; window size remains fixed

        self.resize(800, 500)  # Sets the initial size of the window
        print(self.size())  # To confirm the window size

    #------------------------------------------------

        self.setGeometry(150, 150, 300, 150)  # Performs move and resize operations at the same time
        print(self.geometry())  # Prints the properties of the window

    #----------------button--------------------------
        self.button = QPushButton("Click", self)  # Adds a button labeled "Click" to the window
        self.setDisabled(True)  # Disables the button
        self.setEnabled(True)  # Enables the button

    #-----------------WindowTitle-WindowIcon---------------
        self.setWindowTitle("Demo")  # Sets the title of the window
    #   self.setWindowIcon(QIcon("png")) - Add the name of the folder containing your desired icon image

    #-----------show (used to display the window on the screen)-----------
        self.show()
        self.showMinimized()  # Minimizes the window to the taskbar
        self.showMaximized()  # Maximizes the window to cover the entire screen
        self.showFullScreen()  # Shows the window in fullscreen mode
        self.showNormal()  # Restores the window to its normal size
    #---------------------------------------------------------------------
    
app = QApplication([])
window = main()
window.show()
app.exec()