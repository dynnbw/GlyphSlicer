"""GlyphSlicer —— 手写字体制作辅助工具

将手写字稿扫描件切分成单个字符图片，支持全 Unicode 码点映射与自动命名导出。
一键打包：pyinstaller --onefile --windowed --name GlyphSlicer main.py
"""

import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt

from src.gui.main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("GlyphSlicer")
    app.setApplicationVersion("0.1.0")

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
