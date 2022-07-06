#controller.py
from PyQt5 import QtWidgets
from UI import Ui_MainWindow
from model import factorial_sum

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        self.ui.Button.clicked.connect(self.buttomClicked)

    def buttomClicked(self):
        sum = str(factorial_sum())
        self.ui.ans.setText(sum)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) 