import mido
from time import time, sleep
import random

from mido import Message

LIGHT_BLUE = 37
PINK = 52
LIGHT_TEAL = 33
PURPLE = 80
ORANGE = 9
DARK_PINK = 58
BRIGHT_WHITE = 119
RED = 72
LEMON_GREEN = 17
GREEN = 26
BRIGHT_PINK = 53
TEAL = 34
BRIGHT_ORANGE = 108


class LaunchKey:
    key_in = None
    ctrl_in = None
    ctrl_out = None

    def __init__(self):
        self.setup()

    def setup(self):
        ports = self.init_launchkey_ports()
        self.enable_extended_mode()

        return ports

    def init_launchkey_ports(
        self,
        midi_name="Launchkey MK2 49 Launchkey MIDI",
        incontrol_name="Launchkey MK2 49 Launchkey InControl",
    ):
        self.key_in = mido.open_input(midi_name)
        self.ctrl_in = mido.open_input(incontrol_name)
        self.ctrl_out = mido.open_output(incontrol_name)

    def debug_list_ports(self):
        print("Input ->", mido.get_input_names())
        print("Output ->", mido.get_output_names())

    def enable_extended_mode(self):
        extended_mode_msg = Message("note_on", channel=15, note=12, velocity=127)
        self.ctrl_out.send(extended_mode_msg)

    def light(self, position, color):
        note = 95 + position
        msg = Message("note_on", channel=15, note=note, velocity=color)
        # print("Note {} -> Color {}".format(note, color))
        self.ctrl_out.send(msg)

    def clear_lights(self, color=BRIGHT_WHITE):
        for p in range(1, 32):
            self.light(p, color)
