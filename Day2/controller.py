#controller.py
from PyQt5 import QtWidgets
from UI import Ui_MainWindow
from PyQt5.QtGui import QImage, QPixmap
from model import *
import cv2

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        self.ui.Show_img.clicked.connect(self.buttomClicked)
        self.src_img = cv2.imread("frogg.jpg")
        self.src_img = cv2.resize(self.src_img, (220,220), interpolation=cv2.INTER_AREA)
        height, width, channel = self.src_img.shape
        bytesPerline = channel * width
        self.qimg = QImage(self.src_img, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.ui.img1.setPixmap(QPixmap.fromImage(self.qimg))

    def buttomClicked(self):
        src_img = get_gray(self.src_img)
        height, width = src_img.shape
        bytesPerline = width
        self.qimg2 = QImage(src_img, width, height, bytesPerline, QImage.Format_Grayscale8)
        self.ui.img2.setPixmap(QPixmap.fromImage(self.qimg2))

        spec = get_HSV(self.src_img)
        height, width, channel = spec.shape
        bytesPerline = channel * width
        self.qimg3 = QImage(spec, width, height, bytesPerline, QImage.Format_RGB888)
        self.ui.img3.setPixmap(QPixmap.fromImage(self.qimg3))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) 