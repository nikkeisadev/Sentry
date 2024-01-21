import os
import sys
import threading
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt, QTimer
from playsound import playsound

scriptDir = os.path.dirname(os.path.realpath(__file__))
gifFile = (scriptDir + os.path.sep + 'images/startup_logo.png')
soundFile = (scriptDir + os.path.sep + '/sounds/startup.wav')

class SoundThread(threading.Thread):
    def run(self):
        # Play the sound effect
        playsound(soundFile)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.resize(384, 242)
        self.MovieLabel = QtWidgets.QLabel(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.MovieLabel.setGeometry(QtCore.QRect(0, 0, 384, 242))
        self.movie = QMovie(gifFile)
        self.MovieLabel.setMovie(self.movie)
        self.movie.start()

        # Start a QTimer with a delay of 3 seconds (3000 milliseconds)
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.closeApplication)
        self.timer.start(6000)  # Delay of 3 seconds

        # Start the sound thread
        sound_thread = SoundThread()
        sound_thread.start()

    def closeApplication(self):
        # Perform any cleanup or additional actions before closing the application
        # Here, we simply exit the application
        QtWidgets.QApplication.quit()

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())