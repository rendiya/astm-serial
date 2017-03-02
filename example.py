

from astm_serial.client import AstmConn
astm = AstmConn(port='/dev/ttyACM0', baudrate=9600)

print astm.open_session()
#print astm.send_command(command='1H|\^&|||BIOLIS NEO^SYSTEM1|||||HOST^P_1||P|1|20161020075348')
print astm.get_data()
#print astm.nak_handler()
#print astm.status()
print astm.close_session()

#from astm_serial import Version

from astm_serial.codec import CheckSum

checksum = CheckSum()
print checksum.make_checksum("1H|\^&|||BIOLIS NEO^SYSTEM1|||||HOST^P_1||P|1|20161020075348\x0D\x03")