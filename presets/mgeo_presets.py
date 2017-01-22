from pymel.core import *
try:
    from PySide.QtCore import *
    from PySide.QtGui import *
except:
    from PySide2.QtCore import *
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *
import os, re, json


class PresetEditorClass(QWidget):
    def __init__(self, parent=None):
        super(PresetEditorClass, self).__init__(parent)
        self.setWindowFlags(Qt.Tool)
        self.setWindowTitle('mGeo Preset Editor')
        self.ly = QVBoxLayout()
        self.setLayout(self.ly)

        self.list = QListWidget()
        self.list.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.ly.addWidget(self.list)

        self.hly = QHBoxLayout()
        self.ly.addLayout(self.hly)

        self.del_btn = QPushButton('Delete')
        self.hly.addWidget(self.del_btn)
        self.del_btn.clicked.connect(self.delete_preset)

        self.fill_list()

    def delete_preset(self):
        sel = self.list.selectedItems()
        if sel:
            if QMessageBox.question(self, 'Delete Preset', 'Remove selected presets?') == QMessageBox.Yes:
                for pr in sel:
                    path = pr.data(32)
                    if os.path.exists(path):
                        try:
                            os.remove(path)
                        except:
                            warning('Cant remove preset %s' % path)
                self.fill_list()

    def fill_list(self):
        self.list.clear()
        presets = self.get_presets()
        for preset in presets:
            it = QListWidgetItem(os.path.basename(preset))
            it.setData(32, preset)
            self.list.addItem(it)

    @staticmethod
    def presets_lib():
        return os.path.join(os.path.dirname(__file__), 'lib').replace('\\', '/')

    @classmethod
    def get_presets(cls):
        lib = cls.presets_lib()
        array = []
        if os.path.exists(lib):
            for f in os.listdir(lib):
                path = os.path.join(lib, f)
                array.append(path)
        return array

    @classmethod
    def checkLegalChar(cls, string):
        pattern = '[^A-Za-z0-9]+'
        return re.sub(pattern, '_', string)

    @classmethod
    def save_preset(cls, name, opt):
        lib = cls.presets_lib()
        if lib:
            preset = dict(
                name=name,
                preset=opt
            )
            path = os.path.join(lib, cls.checkLegalChar(name)+'.json')
            try:
                json.dump(preset, open(path, 'w'), indent=4)
            except:
                print 'Error Save Preset', name
    @staticmethod
    def get_preset(path):
        try:
            data = json.load(open(path))
        except:
            data = {}
        return data