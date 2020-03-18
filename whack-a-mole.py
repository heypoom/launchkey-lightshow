from launchkey import LaunchKey
from time import sleep


class WhackMole(LaunchKey):
    state = [n for n in range(0, 32)]
    score = 0

    def __init__(self):
        self.setup()
        self.game_loop()

    def game_loop(self):
        while True:
            for msg in self.ctrl_in.iter_pending():
                print(msg)

            sleep(0.05)


WhackMole()
