from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QFrame,
    QPushButton,
    QGridLayout,
)


class ControlWidget(QFrame):

    command_clicked = Signal(str)

    def __init__(self):
        super().__init__()

        self.setFrameShape(QFrame.StyledPanel)

        layout = QGridLayout()

        forward = QPushButton("↑\nForward")
        backward = QPushButton("↓\nBackward")
        left = QPushButton("←\nLeft")
        right = QPushButton("→\nRight")
        stop = QPushButton("STOP")

        layout.addWidget(forward,0,1)
        layout.addWidget(left,1,0)
        layout.addWidget(stop,1,1)
        layout.addWidget(right,1,2)
        layout.addWidget(backward,2,1)

        self.setLayout(layout)

        forward.clicked.connect(lambda:self.command_clicked.emit("Forward"))
        backward.clicked.connect(lambda:self.command_clicked.emit("Backward"))
        left.clicked.connect(lambda:self.command_clicked.emit("Left"))
        right.clicked.connect(lambda:self.command_clicked.emit("Right"))
        stop.clicked.connect(lambda:self.command_clicked.emit("Stop"))