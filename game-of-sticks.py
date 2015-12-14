class random:
    cooking = False
    power = 100
    time = 0

    def start(self, time, power):
        if self.cooking:
            raise ValueError("Microwave already in use")
        self.time = time
        self.power = power
        self.cooking = True

    def stop(self):
        if not self.cooking:
            raise ValueError("Microwave already stopped")
        self.cooking = False
        self.time = 0
        self.power = 100

    def __str__(self):
        return "Cooking: {} Power: {} Time: {}".format(self.cooking, self.power, self.time)