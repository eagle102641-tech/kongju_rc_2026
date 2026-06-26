from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("RC Car Controller")

        self.resize(900, 700)

        self.init_ui()

    def init_ui(self):

        title = QLabel("RC CAR CONTROLLER")

        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
        """)

        button = QPushButton("Forward")

        layout = QVBoxLayout()

        layout.addWidget(title)

        layout.addWidget(button)

        container = QWidget()

        container.setLayout(layout)

        self.setCentralWidget(container)