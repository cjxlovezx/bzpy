
import serial

gcode_file = 'spirographBase.gcode'

fh = open(gcode_file)


for line in fh.readlines():
    line = line.strip('\n')
    if ';' in line:
        line = line[:line.index(';')].rstrip()
    if line:
        print line

fh.close()

