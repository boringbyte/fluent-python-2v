class InvalidCommand(Exception):
    def __int__(self, message):
        self.message = message
        super().__init__(self.message)


class Robot:
    def __int__(self):
        self.leds = dict()

    def beep(self, times, frequency):
        pass

    def rotate_neck(self, angle):
        pass

    def handle(self, message):
        match message:
            case ['BEEPER', frequency, times]:
                self.beep(times, frequency)
            case ['NECK', angle]:
                self.rotate_neck(angle)
            case ['LED', ident, intensity]:
                self.leds[ident].set_brightness(ident, intensity)
            case ['LED', ident, red, green, blue]:
                self.leds[ident].set_color(ident, red, green, blue)
            case _:
                raise InvalidCommand(message)
