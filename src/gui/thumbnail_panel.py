"""缩略图面板 —— 切分块列表、字符映射输入、状态统计"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QListWidget, QLineEdit,
    QPushButton, QHBoxLayout, QGroupBox,
)
from PyQt6.QtCore import Qt


class ThumbnailPanel(QWidget):
    """右侧面板：缩略图列表 + 字符输入 + 统计信息"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(6)

        # 统计信息
        stats_group = QGroupBox("统计")
        stats_layout = QVBoxLayout(stats_group)
        self.lbl_total = QLabel("切分块总数: 0")
        self.lbl_mapped = QLabel("已映射: 0")
        self.lbl_warnings = QLabel("⚠ 警告: 0")
        stats_layout.addWidget(self.lbl_total)
        stats_layout.addWidget(self.lbl_mapped)
        stats_layout.addWidget(self.lbl_warnings)
        layout.addWidget(stats_group)

        # 字符映射输入
        mapping_group = QGroupBox("字符映射")
        mapping_layout = QVBoxLayout(mapping_group)

        input_row = QHBoxLayout()
        self.char_input = QLineEdit()
        self.char_input.setPlaceholderText("输入字符...")
        self.char_input.setMaxLength(2)  # 允许辅助平面（代理对）
        input_row.addWidget(self.char_input)

        self.btn_apply = QPushButton("确认")
        input_row.addWidget(self.btn_apply)
        mapping_layout.addLayout(input_row)

        self.lbl_codepoint = QLabel("码点: —")
        self.lbl_codepoint.setStyleSheet("color: #a6adc8; font-family: monospace;")
        mapping_layout.addWidget(self.lbl_codepoint)

        layout.addWidget(mapping_group)

        # 缩略图列表
        list_group = QGroupBox("切分块列表")
        list_layout = QVBoxLayout(list_group)
        self.list_widget = QListWidget()
        self.list_widget.setSelectionMode(
            QListWidget.SelectionMode.ExtendedSelection
        )
        list_layout.addWidget(self.list_widget)

        # 批量操作按钮
        btn_row = QHBoxLayout()
        self.btn_sort = QPushButton("排序")
        self.btn_delete = QPushButton("删除")
        self.btn_batch_map = QPushButton("批量映射")
        btn_row.addWidget(self.btn_sort)
        btn_row.addWidget(self.btn_delete)
        btn_row.addWidget(self.btn_batch_map)
        list_layout.addLayout(btn_row)

        layout.addWidget(list_group, stretch=1)
