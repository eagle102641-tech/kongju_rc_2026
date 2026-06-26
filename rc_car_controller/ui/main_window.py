from PySide6.QtWidgets import (
    QWidget,
    QMainWindow,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QSlider,
)

from PySide6.QtCore import Qt

from ui.status_widget import StatusWidget
from ui.control_widget import ControlWidget
from ui.log_widget import LogWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("RC Car Controller")

        self.resize(1000,700)

        self.build_ui()

    def build_ui(self):

        root = QWidget()

        main_layout = QVBoxLayout()

        title = QLabel("RC CAR CONTROLLER")

        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet("""
        font-size:28px;
        font-weight:bold;
        """)

        top_layout = QHBoxLayout()

        self.status = StatusWidget()

        self.control = ControlWidget()

        top_layout.addWidget(self.status,1)
        top_layout.addWidget(self.control,2)

        speed_title = QLabel("Speed")

        self.slider = QSlider(Qt.Horizontal)

        self.slider.setRange(0,100)

        self.slider.setValue(50)

        self.log = LogWidget()

        main_layout.addWidget(title)

        main_layout.addLayout(top_layout)

        main_layout.addWidget(speed_title)

        main_layout.addWidget(self.slider)

        main_layout.addWidget(self.log)

        root.setLayout(main_layout)

        self.setCentralWidget(root)

        self.control.command_clicked.connect(self.button_pressed)

    def button_pressed(self, command):

        self.log.add_log(command)

        self.status.command.setText(f"Current : {command}")