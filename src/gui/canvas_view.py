"""图像 Canvas 视图 —— 大图显示、缩放平移、切分框交互"""

from PyQt6.QtWidgets import QGraphicsView, QGraphicsScene
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter


class CanvasView(QGraphicsView):
    """基于 QGraphicsView 的大图显示与切分框交互区"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self._scene = QGraphicsScene(self)
        self.setScene(self._scene)

        # 渲染设置
        self.setRenderHints(
            QPainter.RenderHint.Antialiasing |
            QPainter.RenderHint.SmoothPixmapTransform
        )
        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)
        self.setTransformationAnchor(
            QGraphicsView.ViewportAnchor.AnchorUnderMouse
        )
        self.setResizeAnchor(
            QGraphicsView.ViewportAnchor.AnchorUnderMouse
        )
        self.setViewportUpdateMode(
            QGraphicsView.ViewportUpdateMode.SmartViewportUpdate
        )

        # 背景
        self.setBackgroundBrush(Qt.GlobalColor.darkGray)
        self.setFrameStyle(0)

        # 空场景占位
        from PyQt6.QtWidgets import QGraphicsTextItem
        placeholder = QGraphicsTextItem("拖入或导入字稿图片")
        placeholder.setDefaultTextColor(Qt.GlobalColor.gray)
        self._scene.addItem(placeholder)

    def wheelEvent(self, event):
        """鼠标滚轮缩放"""
        zoom_in = event.angleDelta().y() > 0
        factor = 1.15 if zoom_in else 1 / 1.15
        self.scale(factor, factor)
