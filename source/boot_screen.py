from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QLabel, QMainWindow, QApplication, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap
import sys 
  
  
class Window(QMainWindow): 
    def __init__(self): 
        super().__init__() 
        self.setWindowFlag(Qt.FramelessWindowHint) 
        
        self.central_widget = QWidget()               
        self.setCentralWidget(self.central_widget)    
        lay = QVBoxLayout(self.central_widget)
        
        label = QLabel(self)
        pixmap = QPixmap('images/startup_logo.png')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())
        
        lay.addWidget(label)
        self.show()
  
  
# create pyqt5 app 
App = QApplication(sys.argv) 
  
# create the instance of our Window 
window = Window() 
# start the app 
sys.exit(App.exec()) 