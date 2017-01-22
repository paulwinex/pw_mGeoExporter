from widgets.imports import *
#reload(widgetsMap)
#reload(activeButton)
from widgets import widgetsMap, activeButton
reload(widgetsMap)
import json
import defaultSettings
reload(defaultSettings)
from widgets import pathLineEdit

class exportSetManager(QListWidget):
    def __init__(self,  parent = None):
        QListWidget.__init__(self)
        self.par = parent
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.prefix = 'mGeo_'
        self.settingsAttribName = 'mgeo'
        self.enableAttribName = 'mgeoEnable'

        self.bufer = None
        #connect
        self.itemDoubleClicked.connect(self.selectObjects)
        self.itemChanged.connect(self.setSetEnable)
        self.itemSelectionChanged.connect(self.par.enableUi)
        #style
        self.setStyleSheet("QListWidget::item{ height: 20px;}")
        palette  = self.palette()
        palette.setColor(QPalette.Highlight, QColor(70,80,88))
        self.setPalette(palette)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.itemAt(event.pos()):
                self.updateUi(self.itemAt(event.pos()))
                QListWidget.mousePressEvent(self, event)
            else:
                self.clearSelection()
                self.par.statusMsg('Create or select export set')
                self.refreshSets()
            self.par.enableUi()
            QListWidget.mousePressEvent(self, event)
        elif event.button() == Qt.RightButton:
            if len(self.selectedItems()) <= 1:
                QListWidget.mousePressEvent(self, event)
                self.par.enableUi()
            if self.itemAt(event.pos()):
                self.par.enableUi()
                self.openMenu(self.itemAt(event.pos()), event.globalPos())

################################################################

    def createSet(self):
        objs = self.getSelectedObjects()
        if objs:
            text, ok = QInputDialog.getText(self, 'Create export set', 'Enter name:', QLineEdit.Normal, objs[0])
            if ok:
                setNode = cmds.sets(objs, n=self.prefix+str(text))
                self.writeAttrib(setNode, self.getDeafults())
                self.writeEnable(setNode)
                self.refreshSets()
                msg = 'Set created: ' + setNode.replace(self.prefix, '')
                self.par.msg2(0, msg)
                self.par.statusMsg(msg)
        else:
            self.par.msg2(1, 'Selection is empty!!!')
            self.par.statusMsg('Selection is empty!!!')

    def removeSet(self):
        sel = self.selectedItems()
        names = []
        for s in sel:
            cmds.delete(self.getSetName(s))
            names.append(str(self.itemWidget(s).text))

        self.par.msg2(0,'Delete sets: ' + ' '.join([f+',' for f in names]))
        self.refreshSets()

    def addToSet(self):
        objs = self.getSelectedObjects()
        if objs:
            sets = self.selectedItems()
            if set:
                for s in sets:
                    for o in objs:
                        cmds.sets(o, add=self.getSetName(s))

    def removeFromSet(self):
        objs = self.getSelectedObjects()
        if objs:
            sets = self.selectedItems()
            if sets:
                for s in sets:
                    for o in objs:
                        cmds.sets(o, rm=self.getSetName(s))

    def replaceSetContent(self):
        objs = self.getSelectedObjects()
        if objs:
            items = self.selectedItems()
            if items:
                self.clearSet()
                self.addToSet()

    def clearSet(self):
        items = self.selectedItems()
        if items:
            for item in items:
                name = self.getSetName(item)
                objs = cmds.sets(name, q=True )
                if objs:
                    for o in objs:
                        cmds.sets(o, rm=name)

    def getDeafults(self):
        ui = defaultSettings.settings
        return ui

    def refreshSets(self):
        self.clear()
        defaults = ['initialShadingGroup', 'initialParticleSE', 'defaultCreaseDataSet']
        sets = ls(type='objectSet')
        mgeoSets = []
        for s in sets:
            if not s in defaults and objExists(s):
                if attributeQuery( self.settingsAttribName, node=s, exists=True ):
                    mgeoSets.append(s)
        if mgeoSets:
            mgeoSets = list(set([x.name() for x in mgeoSets]))
            for s in sorted(mgeoSets):
                # item = self.createItem(s)
                item = QListWidgetItem()
                item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
                item.setData(32, s)
                self.addItem(item)
                act = self.getSetEnable(s)
                wg = activeButton.activeButtonClass(item, s, act, self)
                self.setItemWidget(item, wg)
                self.updateMarkers(item)

        self.exportEnable() #check enable to export

    def selectObjects(self, item):
        self.par.selectSetObjects(self.getSetName(item), self.par.getVisFast())

    def getSelectedObjects(self):
        sel =  cmds.ls(sl=1, objectsOnly=1)
        return sel

    def getSetEnable(self, s):
        if cmds.attributeQuery( self.enableAttribName, node=s, exists=True ):
            if bool(cmds.getAttr(s+'.'+self.enableAttribName)):
                return True
            else:
                return False
        else:
            cmds.addAttr(s,ln=self.enableAttribName,at=bool )
            cmds.setAttr(s+'.'+self.enableAttribName, 1)
            return Qt.Checked

    def setNodeEnable(self, name, val):
        if cmds.objExists(name):
            if cmds.attributeQuery(self.enableAttribName, node=name, exists=True):
                cmds.setAttr(name+'.'+self.enableAttribName, val)
            else:
                cmds.addAttr(name, ln=self.enableAttribName, at=bool)
                cmds.setAttr(name+'.'+self.enableAttribName, val)

    def setSetEnable(self, item):
        name = self.getSetName(item)
        val = self.itemWidget(item).active
        sel = self.selectedItems()
        #PySide
        exists = False
        for i in sel:
            if i is item:
                exists = True
                break
        if exists:
            for i in sel:
                self.itemWidget(i).active = not val
                self.setNodeEnable(self.getSetName(i), not val)
                self.itemWidget(i).setColor()
        else:
            self.itemWidget(item).active = not val
            self.setNodeEnable(name, not val)
            self.itemWidget(item).setColor()

    def toDefault(self, dict):
        sel = self.selectedItems()
        for s in sel:
            self.writeAttrib(self.getSetName(s), dict)

    def writeAttrib(self, nset, dict=None):
        if not cmds.attributeQuery(self.settingsAttribName, node=nset, exists=True ):
            cmds.addAttr(nset, ln=self.settingsAttribName, sn='mg',  dt='string')#, h=True)
        if dict:
            ui = dict
        else:
            ui = self.getAttribString()
        data = json.dumps(ui)
        cmds.setAttr(nset+'.'+self.settingsAttribName, data, type="string" )

    def writeAttribByName(self, item, widget):
        opt = self.getOptionName(str(widget))
        if not cmds.objExists(item):
            print 'Node not found!!!', item
            return
        if opt:
            if not cmds.attributeQuery( self.settingsAttribName, node=item, exists=True ):
                cmds.addAttr(item, ln=self.settingsAttribName, sn='mg',  dt='string')#, h=True)
            attribStr = cmds.getAttr(item + '.' +  self.settingsAttribName)
            try:
                node = json.loads(attribStr)
            except:
                node = defaultSettings.settings
            ui = self.getAttribString()
            node[opt] = ui[opt]
            cmds.setAttr(item+'.'+self.settingsAttribName, json.dumps(node), type="string" )
        else:
            # import inspect
            # print inspect.stack()[1][3]
            print 'WIDGET NOT FOUND FOR SAVING', widget

    def getOptionName(self, widget):
        w = widgetsMap.widgets.get(widget)
        return w

    def writeEnable(self, n):
        if not cmds.attributeQuery(self.enableAttribName, node=n, exists=True ):
            cmds.addAttr(n, ln=self.enableAttribName, attributeType='bool' )
            cmds.setAttr(n+'.'+self.enableAttribName, 1)

    def readAttrib(self, item):
        name = self.getSetName(item)
        if not cmds.objExists(name):
            self.refreshSets()
            return None
        if cmds.attributeQuery(self.settingsAttribName, node=name, exists=True):
            settings = cmds.getAttr(name+'.'+self.settingsAttribName)
            try:
                data =  json.loads(settings)
                return data
            except:
                return {}
        else:
            return None


    def getAttribString(self):
        ui = self.par.getUiOptions()
        return ui

    def openMenu(self,item, pos):
        selectetCount = len(self.selectedItems())
        menu = QMenu(self)
        if selectetCount == 1:
            copy = QAction('Copy Parameters', self)
            copy.connect(copy, SIGNAL('triggered()'),partial(self.copyParameters,item))
            menu.addAction(copy)
        paste = QAction('Paste Parameters', self)
        paste.connect(paste, SIGNAL('triggered()'),partial(self.pasteParameters,item))
        # if not self.bufer:
        #     paste.setEnabled(0)
        menu.addAction(paste)

        if selectetCount == 1:
            rename = QAction('Rename Set', self)
            rename.connect(rename, SIGNAL('triggered()'),partial(self.renameSet,item))
            menu.addAction(rename)

        dup = QAction('Duplicate Sets', self)
        dup.connect(dup, SIGNAL('triggered()'),self.duplicateSets)
        menu.addAction(dup)
        menu.exec_(pos)

    def updateUi(self, item):
        op = self.readAttrib(item)
        if op:
            self.par.setUiOptions(op)
            self.par.statusMsg('Current set: '+str(self.itemWidget(item).text))

    def updateMarkers(self, item):
        op = self.readAttrib(item)
        if op:
            self.itemWidget(item).updateMarkers(op)

    def saveUiSettings2(self, item=None):
        if not item or not type(item) == QListWidgetItem:
            if self.selectedItems():
                item = self.selectedItems()[0]
        if item:
            self.writeAttrib(self.getSetName(item))

    def saveUiSettings(self, widget=None):
        # import inspect
        # print inspect.stack()[1][3]
        items = self.selectedItems()
        if items:
            for item in items:
                self.writeAttribByName(self.getSetName(item), widget)
                self.updateMarkers(item)

    def exportEnable(self):
        if self.count():
            self.par.exportEnable(1)
        else:
            self.par.exportEnable(0)

    def copyParameters(self, item):
        self.par.msg2(0,'Copy parameters from '+ str(item.text()))
        text = self.readAttrib(item)
        self.bufer = text
        clipboard = QApplication.clipboard()
        clipboard.setText(json.dumps(text))

    def pasteParameters(self, item):
        self.par.msg2(0,'Paste parameters to '+ str(item.text()))
        items = self.selectedItems()
        if not self.bufer:
            try:
                clipboard = QApplication.clipboard()
                self.bufer = json.loads(clipboard.text())
            except:
                pass

        if items and self.bufer:
            for item in items:
                self.writeAttrib(self.getSetName(item), self.bufer)
                self.updateUi(item)

    def duplicateSets(self):
        dup = self.selectedItems()
        if dup:
            for item in dup:
                name = self.getSetName(item)
                if name:
                    new = cmds.duplicate(name)
                    content = cmds.sets( name, q=True )
                    for o in content:
                        cmds.sets(o, add=new[0])
                    msg = 'Set created:' + new[0].replace(self.prefix, '')
                    self.par.msg2(0, msg)
                    self.par.statusMsg(msg)

            self.refreshSets()

    def renameSet(self, item):
        old = self.itemWidget(item).text
        text, ok = QInputDialog.getText(self, 'Rename', 'Enter name:', QLineEdit.Normal, old)
        if ok:
            cmds.rename(self.getSetName(item), self.prefix+str(text))
            self.refreshSets()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Z and  event.modifiers() == Qt.ControlModifier:
            self.refreshSets()
        QListWidget.keyPressEvent(self, event)

    def getSetName(self, item):
        try:#Pyqt
            return str(item.data(32).toString())
        except: #PySide
            return str(item.data(32))
