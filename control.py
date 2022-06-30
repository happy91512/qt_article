from PyQt5 import QtWidgets
from UI import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        self.ui.Button.clicked.connect(self.buttomClicked)

    def buttomClicked(self):
        self.ui.txt.setText("hello")