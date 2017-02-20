from  astm.client import AstmConn

astm = AstmConn(port='/dev/ttyACM0', baudrate=9600)
#print astm.send_command(command='coba')
print astm.open_session()
#print astm.get_data()
#print astm.nak_handler()
#print astm.status()
#print astm.close_session()