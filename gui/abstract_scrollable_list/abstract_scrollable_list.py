from PyQt5.QtCore import QEasingCurve
from PyQt5.QtWidgets import QScrollerProperties, QScroller, QWidget


class AbstractScroller:

    def __init__(self, viewport: QWidget = None):
        self._viewport = viewport

        self._sp = QScrollerProperties()
        # # self._sp.setScrollMetric(QScrollerProperties.DragVelocitySmoothingFactor, 0.6)
        self._sp.setScrollMetric(QScrollerProperties.DragVelocitySmoothingFactor, 0.1)
        self._sp.setScrollMetric(QScrollerProperties.ScrollingCurve, QEasingCurve(QEasingCurve.OutExpo))
        self._sp.setScrollMetric(QScrollerProperties.MinimumVelocity, 0.0)
        self._sp.setScrollMetric(QScrollerProperties.MaximumVelocity, 0.2)
        self._sp.setScrollMetric(QScrollerProperties.AcceleratingFlickMaximumTime, 0.5)
        self._sp.setScrollMetric(QScrollerProperties.AcceleratingFlickSpeedupFactor, 1.2)
        # self._sp.setScrollMetric(QScrollerProperties.SnapPositionRatio, 0.2)
        self._sp.setScrollMetric(QScrollerProperties.SnapPositionRatio, 1)
        self._sp.setScrollMetric(QScrollerProperties.MaximumClickThroughVelocity, 1)
        self._sp.setScrollMetric(QScrollerProperties.DragStartDistance, 0.001)
        self._sp.setScrollMetric(QScrollerProperties.MousePressEventDelay, 0.5)

        self._mouse_scroller = QScroller.scroller(self._viewport)
        self._mouse_scroller.setScrollerProperties(self._sp)

        self._touch_scroller = QScroller.scroller(self._viewport)
        self._touch_scroller.setScrollerProperties(self._sp)

    def setMouseScrollable(self, is_true: bool):
        if is_true:
            self._mouse_scroller.grabGesture(self._viewport, QScroller.LeftMouseButtonGesture)
        else:
            self._mouse_scroller.ungrabGesture(self._viewport)

    def setTouchScrollable(self, is_true: bool):
        if is_true:
            self._touch_scroller.grabGesture(self._viewport, QScroller.TouchGesture)
        else:
            self._touch_scroller.ungrabGesture(self._viewport)
