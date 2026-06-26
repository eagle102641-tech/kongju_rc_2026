from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
)


class StatusWidget(QFrame):

    def __init__(self):
        super().__init__()

        self.setFrameShape(QFrame.StyledPanel)

        layout = QVBoxLayout()

        title = QLabel("STATUS")
        title.setStyleSheet("font-size:20px;font-weight:bold;")

        self.connection = QLabel("Connection : Disconnected")
        self.battery = QLabel("Battery : 100 %")
        self.speed = QLabel("Speed : 0 %")
        self.command = QLabel("Current : STOP")

        layout.addWidget(title)
        layout.addSpacing(10)
        layout.addWidget(self.connection)
        layout.addWidget(self.battery)
        layout.addWidget(self.speed)
        layout.addWidget(self.command)
        layout.addStretch()

        self.setLayout(layout)