from os import remove, _exit
import driver as d
import qr as q
import bot as b
import gui as g
from threading import Thread


def startThread(func, *args):
    thread = Thread(target=func, args=args)
    thread.start()


def stopThread(thread):
    thread.stop()


def isDestroyed():
    while True:
        if g.isDestroyed:
            remove('assets/qrCode.png')
            d.driver.quit()
            _exit()

def waitFileToExist(filename):
    while True:
        try:
            with open(f'assets/{filename}', 'r') as f:
                print(f'{filename} found')
            return
        except:
            print(f'{filename} not found')
            pass


def main():
    startThread(isDestroyed)
    startThread(g.GUI)
    startThread(q.captureQR, d.getDriver())
    waitFileToExist('qrCode.png')
    startThread(g.updateQRCode)
    


if __name__ == '__main__':
    main()
