from time import sleep
from launchkey import LaunchKey

board = LaunchKey()
board.clear_lights()

def running_lights():
    color = 2

    while color < 127:
        # First row is 1 - 16
        for n in range(1, 16):
            board.light(n, color)
            sleep(0.05)

        # Second row is 25 - 17
        n = 25
        while n > 16:
            board.light(n, color)
            sleep(0.05)
            n = n - 1

        color = color + 1


def random_lights():
    while True:
        for p in range(1, 32):
            board.light(p, random.randint(1, 127))

        sleep(0.1)


running_lights()
