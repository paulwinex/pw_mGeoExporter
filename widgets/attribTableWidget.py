from imports import *
from .. import defaultSettings
defValues = dict(
                src='',
                rename='',
                # type=0,
                default=''
            )

class attribTableWidgetClass(QWidget):
    saveSignal = Signal(str)
    def __init__(self, parent, name):
        super(attribTableWidgetClass, self).__init__()
        self.setObjectName(name)
        self.ly = QHBoxLayout(self)
        self.ly.setContentsMargins(2,2,2,2)
        self.ly.setSpacing(2)
        #widgets
        self.table = QTableWidget(self)
        verticalHeader = self.table.verticalHeader()
        # verticalHeader.sectionResizeMode(QHeaderView.Fixed)
        verticalHeader.setDefaultSectionSize(24)
        verticalHeader.setCascadingSectionResizes(0)
        self.ly.addWidget(self.table)
        self.btn_ly = QVBoxLayout()
        self.btn_ly.setContentsMargins(2,2,2,2)
        self.btn_ly.setSpacing(2)

        self.ly.addLayout(self.btn_ly)
        self.setMinimumHeight(200)

        self.add_btn = QPushButton('+')
        self.del_btn = QPushButton('-')
        self.btn_ly.addWidget(self.add_btn)
        self.btn_ly.addWidget(self.del_btn)
        if name in defaultSettings.__dict__:
            self.check_btn = QPushButton('*')
            self.btn_ly.addWidget(self.check_btn)
            self.check_btn.clicked.connect(self.presetsMenu)

        self.btn_ly.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        #ui
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(('Name','Rename', 'Default value'))
        if qt == 'side2':
            self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch )
        else:
            self.table.horizontalHeader().setResizeMode(QHeaderView.Stretch )
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)

        #connect
        self.add_btn.clicked.connect(self.addAttr)
        self.del_btn.clicked.connect(self.removeAttr)


        self.table.itemChanged.connect(self.saveChanges)

    def addAttr(self, values=None):
        values = values or defValues
        self.table.blockSignals(True)
        row = self.table.rowCount()
        self.table.insertRow(row)
        i = self.table.rowCount()-1
        self.table.setItem(i, 0, QTableWidgetItem(values['src']))
        self.table.setItem(i, 1, QTableWidgetItem(values['rename']))
        self.table.setItem(i, 2, QTableWidgetItem(values['default']))
        self.table.blockSignals(False)

    def removeAttr(self):
        sel = self.table.selectedRanges()
        rows = []
        for s in reversed(sel):
            rows += list(reversed(range(s.topRow(), s.bottomRow()+1)))
        rows = list(reversed(sorted(rows)))
        for r in rows:
            self.table.removeRow(r)
        self.saveChanges()

    def getAllAttrs(self, i=0):
        attribs = []
        for i in range(self.table.rowCount()):
            srcName = self.table.item(i,0).text()
            if not srcName:
                continue
            rename = self.table.item(i,1).text()
            default = self.table.item(i,2).text()
            attr = dict(
                src=srcName,
                rename=rename,
                default=default
            )
            attribs.append(attr)
        return attribs

    def updateTable(self, attrs):
        self.table.setRowCount(0)
        for attr in attrs:
            self.addAttr(attr)

    def saveChanges(self, *args):
        self.saveSignal.emit(self.objectName())

    def presetsMenu(self):
        pr = defaultSettings.__dict__[self.objectName()]
        menu = QMenu(self)
        for title, preset in pr.items():
            a = QAction(title, self)
            presDict = {'src':preset[0], 'rename':preset[1], 'default':preset[2]}
            a.triggered.connect(lambda values=presDict:self.addAttr(values))
            menu.addAction(a)
        menu.exec_(QCursor.pos())
        self.saveChanges()