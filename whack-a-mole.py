from launchkey import LaunchKey, TEAL, PINK, ORANGE, BRIGHT_WHITE, RED
from time import sleep
from random import randint, choice
from simpleaudio import WaveObject


class WhackMole(LaunchKey):
    state = [False for n in range(0, 26)]
    decay_state = [0 for n in range(0, 26)]

    score = 0
    colors = [TEAL, PINK]
    squeak_sound = WaveObject.from_wave_file("squeak.wav")
    oof_sound = WaveObject.from_wave_file("oof.wav")

    def __init__(self):
        self.setup()
        self.clear_lights()

        print("Go!")
        self.game_loop()

    def add_mole(self, n):
        if self.decay_state[n] == 1:
            self.decay_state[n] = 0
            self.state[n] = False
            self.light(n, BRIGHT_WHITE)

            print("Whoops! You missed the mole at {}".format(n))
            self.fail()

        elif self.decay_state[n] > 1:
            self.decay_state[n] = self.decay_state[n] - 1

        if randint(1, 2000) < 10:
            color = choice(self.colors)
            self.state[n] = True
            self.light(n, color)

            self.decay_state[n] = randint(20, 40)

    def add_moles(self):
        for n in range(1, 9):
            self.add_mole(n)

        for n in range(17, 25):
            self.add_mole(n)

    def whack(self, position):
        if self.state[position]:
            self.score = self.score + 1
            self.state[position] = False
            self.decay_state[position] = 0

            self.light(position, BRIGHT_WHITE)

            self.squeak_sound.play()

            print("Whacked Mole at {}! Score = {}".format(position, self.score))
        else:
            print("Oops! You did not hit the mole at {}".format(position))
            self.fail()

    def fail(self):
        self.oof_sound.play()
        self.score = self.score - 1

    def game_loop(self):
        while True:
            for msg in self.ctrl_in.iter_pending():
                if msg.type == "note_on":
                    if msg.note < 95:
                        continue

                    self.whack(msg.note - 95)

            self.add_moles()

            sleep(0.05)


WhackMole()
