import time
class Plane:
    velocity = 0.0
    height = 0.0
    slope = 0.0
    start = 0.0
    max_velocity = 900.0
    started = False
    def __init__(self):
        self.start = time.time()
