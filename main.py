import driver as d
import gui as g
from sys import exit


def main():
    d.createDriver()
    d.captureQR()
    if (g.GUI() == -1):
        d.destroyDriver()
        exit()


if __name__ == '__main__':
    main()
