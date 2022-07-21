import random
import datetime


def caputureRun(devices, sections):
    # Use a breakpoint in the code line below to debug your script.
    initialTime = datetime.datetime.now()


    print('yo')

def collectCoin(coins):
    return coins + 1


def collectLife(lives):
    return lives + 1


def collectStar(stars):
    return stars + 1


def finishSection(initialTime, sections):
    currentTime = datetime.datetime.now()
    sectionTime = currentTime - initialTime
    sections.append(currentTime)


if __name__ == '__main__':
    devices = [
        'n64',
        'snes',
        'nes',
        'emulator',
        'PC',
        'phone'
    ]
    sections = []
    caputureRun(devices, sections)

