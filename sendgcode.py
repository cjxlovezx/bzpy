import sys
import serial

gcode_file = sys.argv[1:][0]

port = "/dev/cu.usbmodem1421"
baud = 250000

ser = serial.Serial(port, baud, timeout=200)

def wait( resp ):
    while True:
        response = ser.readline().strip()
        if resp in response.lower():
            print '<' + response
            break

def send( cmd ):
    print '>' + cmd
    ser.write(cmd + '\r\n')
    wait( 'ok' )


wait('start' )
wait('sd init' )

fh = open(gcode_file)

for line in fh.readlines():
    line = line.strip('\n')
    if ';' in line:
        line = line[:line.index(';')].rstrip()
    if line:
        send(line)

fh.close()

ser.close()
