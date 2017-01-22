import os
import getpass

from widgets.imports import cmds


class settingsClass(object):
    def __init__(self):
        home = self.getConfigFolder()
        self.active = bool(home)
        if self.active:
            filename = 'mgeoexporter_settings_' + getpass.getuser()
            self.path = os.path.join(home, filename+'.ini')
            self.data = None
            self.update()

    def checkActive(self):
        if not self.active:
            cmds.warning('Options not active')
            return False
        else:
            return True

    def getConfigFolder(self):
        home = os.getenv('APPDATA')
        if not home:
            home = os.path.join(os.path.expanduser('~'), '.config')
            if not os.path.exists(home):
                try:
                    os.makedirs(home, 0777)
                except:
                    home = os.path.expanduser('~')
        return home

    def readFile(self):
        if self.checkActive():
            lines = []
            if os.path.exists(self.path):
                try:
                    with open(self.path, 'r') as f:
                        lines = f.readlines()
                except:
                    cmds.warning('Cant open options file')
                if lines:
                    lines.pop(0)
                    return lines
                else:
                    return []
            else:
                return []

    def writeFile(self):
        if self.checkActive():
            try:
                with open(self.path, 'w') as f:
                    f.write('#mGeo settings file\n')
                    for i in self.data.items():
                        f.write(str(i[0]) + '=' + str(i[1]) + '\n')
            except:
                cmds.warning('Cant open options file 1')

    def getValue(self, name, default):
        if self.checkActive():
            if name in self.data:
                return self.toType(str(self.data[name]))
            else:
                self.data[name] = str(default)
                self.writeFile()
                return default
        return default

    def setValue(self, name, value):
        if self.checkActive():
            self.data[name] = str(value)
            self.writeFile()

    def update(self):
        if self.checkActive():
            lines = self.readFile()
            self.data = {}
            if not lines is None:
                for l in lines:
                    split = l.split('=')
                    if split:
                        val = self.toType(split[1])
                        self.data[split[0]] = val

    def getData(self):
        return self.data

    def toType(self, val):
        if val == 'True':
            # print 'bool'
            return True
        elif val == 'False':
            # print 'bool'
            return False
        elif val.isdigit():
            # print 'integer'
            return int(val)
        elif val.replace('.', '').isdigit():
            # print 'floatger'
            return float(val)
        else:
            return val.strip()