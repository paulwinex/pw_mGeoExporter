from imports import *

class warningDialogClass(QDialog):
    def __init__(self, method=1, parent = None):
        super(warningDialogClass, self).__init__(parent=None)
        titles = {1:'Warning!', 0:'Error!'}
        icons = {1:":/warning.png", 0:":/error.png"}
        self.setWindowTitle(titles[method])
        mainLy = QVBoxLayout()
        self.setLayout(mainLy)

        LY_up = QHBoxLayout()
        LY_up.setSpacing(15)
        ico = QLabel()
        ico.setPixmap(QPixmap(icons[method]))
        ico.setMaximumSize(64, 64)
        LY_up.addWidget(ico)

        self.text = QLabel()
        LY_up.addWidget(self.text)

        mainLy.addLayout(LY_up)

        LY_dwn = QHBoxLayout()
        #warning
        if method == 1:
            BTN_ok = QPushButton('Continue')
            LY_dwn.addWidget(BTN_ok)
            BTN_cncl = QPushButton('Cancel')
            LY_dwn.addWidget(BTN_cncl)
            BTN_ok.clicked.connect(self.accept)
            BTN_cncl.clicked.connect(self.reject)
        #error
        else:
            LY_dwn = QHBoxLayout()
            BTN_ok = QPushButton('OK')
            LY_dwn.addWidget(BTN_ok)
            BTN_ok.clicked.connect(self.reject)

        mainLy.addLayout(LY_dwn)

    def showWarning(self, text):
        self.text.setText(text)
        return self.exec_()
