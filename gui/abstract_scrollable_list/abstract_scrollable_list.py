from PyQt5.QtCore import QEasingCurve
from PyQt5.QtWidgets import QScrollerProperties, QScroller, QWidget


class AbstractScroller:

    def __init__(self, viewport: QWidget = None):
        self._viewport = viewport

        self._sp = QScrollerProperties()
        # self._sp.setScrollMetric(QScrollerProperties.DragVelocitySmoothingFactor, 0.6)
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

        self._gesture = QScroller.scroller(self._viewport)
        self._gesture.setScrollerProperties(self._sp)

    def setScrollable(self, is_true: bool, gesture: QScroller.ScrollerGestureType):
        if is_true:
            self._gesture.grabGesture(self._viewport, QScroller.LeftMouseButtonGesture)
        else:
            self._gesture.ungrabGesture(self._viewport)

