from imports import *
import markerWidget
reload(markerWidget)

class activeButtonClass(QWidget):
    def __init__(self,  item, name, active, parent=None):
        QWidget.__init__(self)
        self.item = item
        self.par = parent
        self.text = name.replace(self.par.prefix, '')
        self.active = active
        self.color = (200, 150, 88)
        #UI
        ly = QHBoxLayout()
        #PyQt
        try:
            ly.setMargin(0)
        #PySide
        except:
            ly.setContentsMargins(0, 0, 0, 0)
        #BUTTON
        self.but1 = QPushButton()
        self.but1.setMaximumWidth(20)
        self.but1.setToolTip('Disable\Enable set')
        ly.addWidget(self.but1)
        #TEXT
        self.textLabel = QLabel()
        self.textLabel.setText(self.text)
        ly.addWidget(self.textLabel)
        #MARKERS
        if self.par.par.colorInd_act.isChecked():
            self.marker = markerWidget.markersClass()
            ly.addWidget(self.marker)
        else:
            self.marker = None

        self.setLayout(ly)
        #connect
        self.but1.clicked.connect(self.switsh)
        self.setColor()

    def switsh(self):
        self.par.setSetEnable(self.item)

    def setColor(self):
        if self.active:
            self.setStyleSheet('QPushButton{background-color: rgb'+str(self.color)+'; color: rgb(255, 255, 255)}QLabel{ font-size: 15px }')
        else:
            self.setStyleSheet('QPushButton{background-color: rgb(82,82,82); color: rgb(255, 255, 255)}QLabel{ font-size: 15px }')

    def state(self):
        return self.active

    def updateMarkers(self, opt):
        if self.marker:
            self.marker.updateColors(opt)


