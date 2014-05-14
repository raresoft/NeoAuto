import time

def getNST(offset):
    systime = time.strftime("%H%M")
    intTime = int(systime)
    intNST = intTime + offset
    if (intNST > 2400):
        intNST = intNST - 2400
    return intNST