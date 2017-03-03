# -*- coding: utf-8 -*-

from astm_serial.client import AstmConn
astm = AstmConn(port='/dev/ttyUSB0', baudrate=9600)

#print astm.open_session()
#astm.send_enq()
print astm.send_string(string='1H|\^&|||HOST^P_1|||||BIOLIS NEO^SYSTEM1||P|1|20161019212729')
#print astm.get_data()
#print astm.nak_handler()
#print astm.status()
#print astm.close_session()
#astm.test()
#from astm_serial import Version

#from astm_serial.codec import CheckSum

#checksum = CheckSum()
#print checksum.make_checksum("1H|\^&|||BIOLIS NEO^SYSTEM1|||||HOST^P_1||P|1|20161020075348\x0D\x03")