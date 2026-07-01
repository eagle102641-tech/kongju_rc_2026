class AutoCar:

    def __init__(self):

        self.speed = 50

    def forward(self):

        print("Forward")

    def backward(self):

        print("Backward")

    def left(self):

        print("Left")

    def right(self):

        print("Right")

    def stop(self):

        print("Stop")

    def set_speed(self, speed):

        self.speed = speed

        print(f"Speed : {speed}")