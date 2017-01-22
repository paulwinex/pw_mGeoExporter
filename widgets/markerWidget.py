from imports import *

class markersClass(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.par = parent
        #Variables
        self.colors = dict(green='(45, 140, 28)',
                             red='(150, 40, 20)',
                          orange='(166, 121, 2)',
                            white='(150, 150, 150)',
                            blue='(25,100,150)',
                            gray='(50, 50, 50)'
                           )
        #UI
        self.buildUI()
        self.setMaximumWidth(30)
        self.setMaximumHeight(16)

    def buildUI(self):
        self.gridLayout = QGridLayout()
        #PyQt
        if qt == 'qt':
            self.gridLayout.setMargin(0)
        #PySide
        else:
            self.gridLayout.setContentsMargins(0,0,0,0)
        self.gridLayout.setSpacing(0)

        self.anim_lb = QLabel()
        self.anim_lb.setObjectName('expanim:green:1')
        self.gridLayout.addWidget(self.anim_lb, 0, 0, 1, 1)

        self.geo_lb = QLabel()
        self.geo_lb.setObjectName('fileformat:blue:0')
        self.gridLayout.addWidget(self.geo_lb, 0, 1, 1, 1)

        self.mdd_lb = QLabel()
        self.mdd_lb.setObjectName('animtype:white:0')
        self.gridLayout.addWidget(self.mdd_lb, 0, 2, 1, 1)

        self.gzip_lb = QLabel()
        self.gzip_lb.setObjectName('gzip:red:1')
        self.gridLayout.addWidget(self.gzip_lb, 0, 3, 1, 1)

        self.poly_lb = QLabel()
        self.poly_lb.setObjectName('exportgeo:orange:1')
        self.gridLayout.addWidget(self.poly_lb, 1, 0, 1, 1)


        self.curv_lb = QLabel()
        self.curv_lb.setObjectName('expcurve:orange:1')
        self.gridLayout.addWidget(self.curv_lb, 1, 1, 1, 1)

        self.part_lb = QLabel()
        self.part_lb.setObjectName('expparticle:orange:1')
        self.gridLayout.addWidget(self.part_lb, 1, 2, 1, 1)

        self.pivot_lb = QLabel()
        self.pivot_lb.setObjectName('exppiv:orange:1')
        self.gridLayout.addWidget(self.pivot_lb, 1, 3, 1, 1)

        self.setLayout(self.gridLayout)

    def colorizeLabels(self, data=None):
        self.anim_lb.setStyleSheet(self.getStyle('red'))
        self.poly_lb.setStyleSheet(self.getStyle('orange'))
        self.curv_lb.setStyleSheet(self.getStyle('gray'))
        self.part_lb.setStyleSheet(self.getStyle('blue'))
        self.pivot_lb.setStyleSheet(self.getStyle('green'))

    def getStyle(self, color):
        style = '''background-color: rgb{0};
                   border-color: rgb(49, 49, 49);
                   border-style: outset;
                   border-width: 0.5px;
                   border-radius: 1px;
                   '''.format(self.colors[color])
        return style

    def updateColors(self, op):
        for w in self.poly_lb, self.curv_lb, self.part_lb, self.pivot_lb, self.anim_lb, self.geo_lb, self.mdd_lb, self.gzip_lb:
            sp = str(w.objectName()).split(':')
            val = op[sp[0]]
            if not int(sp[2]):
                val = not val
            if val:
                color = sp[1]
            else:
                color = 'gray'
            w.setStyleSheet(self.getStyle(color))