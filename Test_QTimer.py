import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800,200,300,300)

        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

    def statusmessage(self):
        self.statusBar.showMessage("Status Message") # statusBar에 massage 띄움
        time.sleep(2) # 2초 대기
        self.statusBar.showMessage("") # statusBar에 공백 띄움

    def set_timer(self):
        self.timer1 = QTimer(self) # timer1 선언
        self.timer1.timeout.connect(self.statusmessage) # timer1에 stausmessage 연결
        self.timer1.start(5000) # timer1 인터벌 5초

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()

    # 프로그램 실행 3초 후 set_timer 함수 실행하여 timer1 작동 시작
    QTimer().singleShot(3, mywindow.set_timer)

    app.exec_()