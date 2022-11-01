from PyQt5.QtCore import QTimeLine
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QWidget, QTabWidget, QStackedWidget


class FaderWidget(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.pixmap_opacity = None
        self.timeline = QTimeLine(200, self)
        self.timeline.valueChanged.connect(self.animate)
        self.timeline.finished.connect(self.close)

    def start(self, old_widget, new_widget):
        self.pixmap_opacity = 1.0
        self.old_pixmap = QPixmap(new_widget.size())
        old_widget.render(self.old_pixmap)

        self.timeline.start()

        self.resize(new_widget.size())
        self.show()

    def paintEvent(self, event):
        if self.pixmap_opacity:
            QWidget.paintEvent(self, event)
            painter = QPainter(self)
            painter.setOpacity(self.pixmap_opacity)
            painter.drawPixmap(0, 0, self.old_pixmap)

    def animate(self, value):
        self.pixmap_opacity = 1.0 - value
        self.update()


class FaderTabWidget(QTabWidget):
    def __init__(self, parent=None):
        QTabWidget.__init__(self, parent)
        self.currentChanged.connect(self.onCurrentIndex)
        self.last = -1
        self.current = self.currentIndex()

    def onCurrentIndex(self, index):
        self.last = self.current
        self.current = self.currentIndex()
        if self.widget(self.last):
            self.widget(self.last).setCurrentIndex(1)
            old_widget = self.widget(self.last).widget(0)
            current_widget = self.widget(self.current).widget(0)
            fade = self.widget(self.current).widget(1)
            fade.start(old_widget, current_widget)

    def addTab(self, widget, text):
        stack = QStackedWidget(self)
        stack.addWidget(widget)
        fade = FaderWidget(self)
        fade.timeline.finished.connect(lambda: stack.setCurrentIndex(0))
        stack.addWidget(fade)
        stack.setCurrentIndex(0 if self.currentIndex() == -1 else 1)
        QTabWidget.addTab(self, stack, text)