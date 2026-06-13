"""GlyphSlicer 主窗口 —— 双视图面板布局"""

from PyQt6.QtWidgets import (
    QMainWindow, QSplitter, QWidget, QVBoxLayout, QHBoxLayout,
    QToolBar, QStatusBar, QLabel, QMenuBar, QMenu,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QKeySequence

from src.gui.canvas_view import CanvasView
from src.gui.thumbnail_panel import ThumbnailPanel


class MainWindow(QMainWindow):
    """主窗口：双视图面板 + 工具栏 + 状态栏"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("GlyphSlicer - 手写字体制作辅助工具")
        self.resize(1400, 900)
        self._setup_menu_bar()
        self._setup_toolbar()
        self._setup_central_widget()
        self._setup_status_bar()
        self._apply_dark_theme()

    def _setup_menu_bar(self):
        menubar = self.menuBar()

        # 文件菜单
        file_menu = menubar.addMenu("文件(&F)")
        file_menu.addAction(QAction("新建项目(&N)", self, shortcut=QKeySequence.StandardKey.New))
        file_menu.addAction(QAction("打开项目(&O)...", self, shortcut=QKeySequence.StandardKey.Open))
        file_menu.addAction(QAction("保存项目(&S)", self, shortcut=QKeySequence.StandardKey.Save))
        file_menu.addSeparator()
        file_menu.addAction(QAction("导入图片(&I)...", self))
        file_menu.addSeparator()
        export_action = QAction("导出所有图片(&X)...", self)
        export_action.setShortcut(QKeySequence("Ctrl+Shift+X"))
        file_menu.addAction(export_action)
        file_menu.addSeparator()
        file_menu.addAction(QAction("退出(&Q)", self, shortcut=QKeySequence.StandardKey.Quit))

        # 视图菜单
        view_menu = menubar.addMenu("视图(&V)")
        view_menu.addAction(QAction("放大", self, shortcut=QKeySequence.StandardKey.ZoomIn))
        view_menu.addAction(QAction("缩小", self, shortcut=QKeySequence.StandardKey.ZoomOut))

        # 切分菜单
        slice_menu = menubar.addMenu("切分(&S)")
        slice_menu.addAction(QAction("手动框选模式", self))
        slice_menu.addAction(QAction("网格切分模式", self))
        slice_menu.addAction(QAction("投影辅助模式", self))
        slice_menu.addAction(QAction("固定尺寸模式", self))

        # 帮助菜单
        help_menu = menubar.addMenu("帮助(&H)")
        help_menu.addAction(QAction("关于(&A)...", self))

    def _setup_toolbar(self):
        toolbar = QToolBar("主工具栏")
        toolbar.setMovable(False)
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, toolbar)

        # 切分模式按钮（占位，后续完善）
        self.tb_manual = toolbar.addAction("✂ 手动")
        self.tb_grid = toolbar.addAction("⊞ 网格")
        self.tb_project = toolbar.addAction("📊 投影")
        self.tb_fixed = toolbar.addAction("📐 固定尺寸")

        toolbar.addSeparator()
        toolbar.addAction("🖼 增强")
        toolbar.addAction("📂 裁剪")
        toolbar.addSeparator()
        toolbar.addAction("📤 导出")

    def _setup_central_widget(self):
        """左侧：Canvas 图片视图 | 右侧：缩略图 + 字符映射面板"""
        splitter = QSplitter(Qt.Orientation.Horizontal)

        # 左侧 —— 图像交互区
        self.canvas = CanvasView()
        splitter.addWidget(self.canvas)

        # 右侧 —— 缩略图 + 映射面板
        self.thumb_panel = ThumbnailPanel()
        splitter.addWidget(self.thumb_panel)

        # 默认比例 70:30
        splitter.setSizes([980, 420])
        splitter.setStretchFactor(0, 7)
        splitter.setStretchFactor(1, 3)

        self.setCentralWidget(splitter)

    def _setup_status_bar(self):
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)

        self.lbl_progress = QLabel("就绪")
        self.lbl_slice_count = QLabel("切分块: 0")
        self.lbl_mapped_count = QLabel("已映射: 0 / 0")

        self.statusbar.addWidget(self.lbl_progress, 1)
        self.statusbar.addPermanentWidget(self.lbl_slice_count)
        self.statusbar.addPermanentWidget(self.lbl_mapped_count)

    def _apply_dark_theme(self):
        """应用暗色主题减轻视觉疲劳"""
        dark_stylesheet = """
        QMainWindow {
            background-color: #1e1e2e;
        }
        QMenuBar {
            background-color: #181825;
            color: #cdd6f4;
            border-bottom: 1px solid #313244;
        }
        QMenuBar::item:selected {
            background-color: #45475a;
        }
        QMenu {
            background-color: #1e1e2e;
            color: #cdd6f4;
            border: 1px solid #313244;
        }
        QMenu::item:selected {
            background-color: #45475a;
        }
        QToolBar {
            background-color: #181825;
            border-bottom: 1px solid #313244;
            spacing: 4px;
            padding: 2px;
        }
        QToolBar QToolButton {
            color: #cdd6f4;
            padding: 4px 8px;
            border-radius: 4px;
        }
        QToolBar QToolButton:hover {
            background-color: #45475a;
        }
        QStatusBar {
            background-color: #181825;
            color: #a6adc8;
            border-top: 1px solid #313244;
        }
        QSplitter::handle {
            background-color: #313244;
            width: 2px;
        }
        """
        self.setStyleSheet(dark_stylesheet)
