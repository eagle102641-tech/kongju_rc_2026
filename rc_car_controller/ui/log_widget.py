from PySide6.QtWidgets import (
    QFrame,
    QTextEdit,
    QVBoxLayout,
    QLabel,
)

from datetime import datetime


class LogWidget(QFrame):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        title = QLabel("LOG")
        title.setStyleSheet("font-size:18px;font-weight:bold;")

        self.log = QTextEdit()
        self.log.setReadOnly(True)

        layout.addWidget(title)
        layout.addWidget(self.log)

        self.setLayout(layout)

    def add_log(self,text):

        now = datetime.now().strftime("%H:%M:%S")

        self.log.append(f"[{now}] {text}")