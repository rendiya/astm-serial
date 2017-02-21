from astm_serial.client import AstmConn
astm = AstmConn(port='/dev/ttyACM0', baudrate=9600)
astm.open_session()
print astm.get_data()
astm.close_session()