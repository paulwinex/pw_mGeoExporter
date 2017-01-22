from imports import *

pattern = r'(`\$([\w\d_]+)`)'
variablesColor = (207, 202, 26)

class ColorWordLineEdit(QTextEdit):
    editingFinished = Signal()
    returnPressed = Signal()
    def __init__(self, parent):
        super(ColorWordLineEdit, self).__init__()
        self.par = parent
        self.setWordWrapMode(QTextOption.NoWrap)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        metrics = QFontMetrics(self.document().defaultFont())
        h = metrics.height()
        self.setMaximumHeight(h*1.9)
        self.setMinimumHeight(h*1.9)

        self.hgl = PathHighlighterClass(self)

    def text(self):
        return self.toPlainText()

    def setText(self, txt):
        super(ColorWordLineEdit, self).setText(txt)
        self.update_tooltip()

    def keyPressEvent(self, event):
        if event.key() in [Qt.Key_Return , Qt.Key_Enter]:
            self.returnPressed.emit()
            self.update_tooltip()
            return
        super(ColorWordLineEdit, self).keyPressEvent(event)

    def focusOutEvent(self, event):
        self.editingFinished.emit()
        self.update_tooltip()
        super(ColorWordLineEdit, self).focusOutEvent(event)


    def insertFromMimeData (self, source ):
        text = source.text()
        line = text.replace('\n','')
        self.update_tooltip()
        self.insertPlainText(line)

    def wheelEvent(self, QWheelEvent):
        return

    def vars_exists(self):
        bool(re.findall(pattern, self.text()))

    def parse_export_path(self, line):
        vars =re.findall(pattern, line)
        for v in vars:
            if v[1] in os.environ:
                line = line.replace(v[0], os.environ[v[1]])
            else:
                return
        return line

    def update_tooltip(self):
        line = self.parse_export_path(self.text())
        if line:
            self.par.resolve_path_le.setText('   ' + line)
            self.setToolTip(line)
        elif line == '':
            self.par.resolve_path_le.setText('')
        else:
            self.setToolTip('Error parse path')
            self.par.resolve_path_le.setText('   Error')



class PathHighlighterClass (QSyntaxHighlighter):
    def __init__(self, document):
        QSyntaxHighlighter.__init__(self, document)

        rules = []
        rules += [(pattern, 0, self.getStyle(variablesColor, True))]

        self.rules = [(QRegExp(pat), index, fmt) for (pat, index, fmt) in rules]
        self.rehighlight()

    def getStyle(self, color, bold=False):
        brush = QBrush( QColor(*color))
        f = QTextCharFormat()
        if bold:
            f.setFontWeight( QFont.Bold )
        f.setForeground( brush )
        return f

    def highlightBlock(self, text):
        # defFormat = self.getStyle((170,170,170))
        # self.setFormat(0, len(text), defFormat)
        for expression, nth, format in self.rules:
            index = expression.indexIn(text, 0)
            while index >= 0:
                index = expression.pos(nth)
                length = len(expression.cap(nth))
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)
        self.setCurrentBlockState(0)