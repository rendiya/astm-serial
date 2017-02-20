# -*- coding: utf-8 -*-
# rendiya (c) 2017

"""ASTM e1381 client result
"""

import time
import serial
from .constanta import *

class AstmConn(object):
    r"""Abstract class that implements the common driver for the TPG 261 and
    TPG 262 dual channel measurement and control unit. The driver implements
    the following 6 commands out the 39 in the specification:
    * PNR: Program number (firmware version)
    * PR[1,2]: Pressure measurement (measurement data) gauge [1, 2]
    * PRX: Pressure measurement (measurement data) gauge 1 and 2
    * TID: Transmitter identification (gauge identification)
    * UNI: Pressure unit
    * RST: RS232 test
    """

    def __init__(self, port='/dev/ttyACM0', baudrate=9600,timeout=10):
        """Initialize internal variables and serial connection
        :param port: The COM port to open. See the documentation for
            `pyserial <http://pyserial.sourceforge.net/>`_ for an explanation
            of the possible value. The default value is '/dev/ttyUSB0'.
        :type port: str or int
        :param baudrate: 9600, 19200, 38400 where 9600 is the default
        :type baudrate: int
        """
        # The serial connection should be setup with the following parameters:
        # 1 start bit, 8 data bits, No parity bit, 1 stop bit, no hardware
        # handshake. These are all default for Serial and therefore not input
        # below
        #self.serial = serial.Serial(port=port, baudrate=baudrate, timeout=1)
        self.serial = serial.Serial(port = port, baudrate=baudrate, 
        timeout=timeout, writeTimeout=timeout,stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE)
    def _astm_string(self, string,c1=0,c2=0,type_data="Intermidiate"):
        """Pad carriage return and line feed to a string
        :param string: String to pad
        :type string: str
        :returns: the padded string
        :rtype: str
        """
        if type_data == "Intermidiate":
            return STX + string + ETB + chr(c1) + chr(c2) + CR + LF
        elif type_data == "Termination":
            return STX + string + ETX + chr(c1) + chr(c2) + CR + LF

    def send_command(self, command):
        """Send a command and check if it is positively acknowledged
        :param command: The command to send
        :type command: str
        :raises IOError: if the negative acknowledged or a unknown response
            is returned
        <STX>[FN][TEXT]<ETB>[C1][C2]<CR><LF>
        """

        self.serial.write(self._astm_string(string=command))
        response = self.serial.readline()
        print response
        if response == NAK:
            message = 'Serial communication returned negative acknowledge'
            message = response.encode('hex')
            return IOError(message)
        elif response != ACK:
            message = response.encode('hex')
            return IOError(message)
    def open_session(self):
        """Get the session communication in ASTM 
        :send: data ENQ
        :return: data ACK
        """
        i = 0
        for i in range(0,9):
            if self.serial.in_waiting:
                check_data = self.serial.read()
                if check_data == ENQ:
                    self.serial.write(ACK)
                    return "client open with ACK"
            else:
                self.serial.write(ENQ)
                data = self.serial.read()
                print 'data hex: '+data.encode('hex')
                print 'data byte: '+data
        
                if data == ACK:
                    return "open session with ACK response"
                elif data == NAK:
                    self.nak_handler()
                    return "receiver send NAK"
                    time.sleep(0.2)
                    i = i + 1
    def get_data(self):
        """Get the data that is ready on the device
        :returns: the raw data
        :rtype:str
        """
        data = None
        if self.serial.in_waiting:
            check_data = self.serial.readline()
            if check_data == ENQ:
                self.serial.write(ACK)
                data = self.serial.readline()
            elif check_data == NAK:
                return "status data NAK"
            elif check_data == ACK:
                self.serial.write(NAK)
            else:
                data = check_data
            print data.encode('hex')
            return data
    def close_session(self):
        """End the communication data
        will send EOT to host
        :return: EOT
        """
        self.serial.write(EOT)
        return "session has expired"
    def nak_handler(self):
        """If server send NAK or Not Acknowledge
        the client will be send EOT and close_session
        :return: EOT
        """
        return self.close_session()
    def status(self):
        data = self.serial.readline()
        return data.encode('hex')
