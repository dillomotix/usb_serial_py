from serial import Serial
import time
import sys


serialPort = Serial("/dev/tty.usbmodem", baudrate = 115200)

if (serialPort.isOpen() == False):
    print ("Python is opening port:\n\tSerial(\"/dev/cu.SLAB_USBtoUART\", 1200)")
    serialPort.open()
else:
    print ("Python sees that the port:\n\tSerial(\"/dev/cu.SLAB_USBtoUART\", 1200)\n\n\tis already open.")

print ('Number of arguments:', len(sys.argv), 'arguments.')
print 'Argument List:', str(sys.argv)
argList = str(sys.argv)

if (len(sys.argv) > 1):
    sendStr = sys.argv[1]
else:
    sendStr = "null"

serialPort.flushInput()
serialPort.flushOutput()
print("\nPython will attempt to send string: " + sendStr)
byteData = bytes((sendStr, 'UTF-8'))
byteData = bytes("sendStr, 'UTF-8'")
byteData = sendStr.encode("UTF-8")
byteArr = bytearray(sendStr)
#serialPort.write("test")
#numBytesSent = serialPort.write( byteData )
#numBytesSent = serialPort.write( sendStr )
numBytesSent = serialPort.write( byteArr )
time.sleep(8)//seconds
#serialPort.flush()

# bytesLeft = serialPort.outWaiting()
# print bytesLeft
# while ( bytesLeft > 0):
#     print "loop"
#     bytesLeft = serialPort.outWaiting()

print("\nPyton sent " + str(numBytesSent) + "bytes")
print("\nPython sent: " + repr( byteData ) )

    #wait
#while (bytesToRead = serialPort.inWaiting() > 0):
bytesToRead = serialPort.inWaiting()
print( serialPort.read(bytesToRead) )


if (serialPort.isOpen() == True):
    print("\nPython is closing the serial port")
    serialPort.close()
else:
    print("\nThe serial port is not open, Python will not close it.")
