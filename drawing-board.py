import mido
from time import time, sleep
import random

from mido import Message

from launchkey import LaunchKey, BRIGHT_WHITE, PINK, TEAL


class DrawingBoard(LaunchKey):
    state = []
    colors = [BRIGHT_WHITE, PINK, TEAL]

    def __init__(self):
        self.setup()
        self.reset()
        self.loop()

    def reset(self):
        self.state = [0 for n in range(0, 32)]

        self.clear_lights()

    def update_color(self, position):
        current_color = self.state[position] or 0
        next_color = (current_color + 1) % len(self.colors)
        self.state[position] = next_color

        next_color_code = self.colors[next_color]

        self.light(position, next_color_code)

        return next_color_code

    def loop(self):
        while True:
            while self.ctrl_in.poll():
                msg = self.ctrl_in.receive()
                print("Message>", msg)

                if msg and hasattr(msg, "note"):
                    position = msg.note - 95
                    self.update_color(position)

                if msg and msg.type == "control_change" and msg.control is 59:
                    self.reset()


DrawingBoard()
