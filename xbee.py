from xbee import XBee
from serial import Serial

port = '/dev/ttyUSB1'
baud = 9600
serial = Serial(port, baud)
xbee = XBee(serial)

def run():
    if key & 0xFF in [ord('S'), ord('s')]:
        xbee.tx(dest_addr='\x00\x01', data='S')
        print "SSSSSS"

    print(xbee.wait_read_frame())
    serial.close()

if __name__ == '__main__':
    run()

