# -*- coding: utf-8 -*-
# rendiya (c) 2017

"""ASTM e1381 client result
"""

import time
import serial
from .constanta import *
from .codec import CheckSum,DataHandler

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
        self.string = DataHandler()

    def send_command(self, command):
        """Send a command and check if it is positively acknowledged
        :param command: The command to send
        :type command: str
        :raises IOError: if the negative acknowledged or a unknown response
            is returned
        <STX>[FN][TEXT]<ETB>[C1][C2]<CR><LF>
        """
        string = self.string.astm_string(string=command)
        self.serial.write(string)
    def send_null(self):
        """Send Null to serial"""
        self.serial.write(Null)
    def send_enq(self):
        """Send ENQ to serial"""
        self.serial.write(ENQ)
    def send_ack(self):
        """Send ACK to serial"""
        self.serial.write(ACK)
    def send_nak(self):
        """Send NAK to serial"""
        self.serial.write(NAK)
    def send_eot(self):
        """Send EOT to serial"""
        self.serial.write(EOT)
    def open_session(self):
        """Get the session communication in ASTM 
        :send: data ENQ
        :return: data ACK
        """
        """Get the session communication in ASTM 
        :send: data ENQ
        :return: data ACK
        """
        self.send_null()
        self.serial.readline()
        self.send_enq()
        data = self.serial.readline()
        print data.encode('hex')
        if data == ACK:
            return "ACK"
        elif data == NAK:
            self.nak_handler()
            return "NAK"
        elif data == EOT:
            return "EOT"
    def get_data(self):
        """Get the data that is ready on the device
        :returns: the raw data
        :rtype:str
        """
        data = None
        check_data = self.serial.readline()
        if check_data == ENQ:
            self.send_ack()
            data = self.serial.readline()
        elif check_data == NAK:
            self.nak_handler
            data = "NAK"
            return "NAK"
        else:
            data = check_data
            self.send_ack()
        return data
    def close_session(self):
        """End the communication data
        will send EOT to host
        :return: EOT
        """
        self.send_eot()
        return "session has expired"
    def nak_handler(self):
        """If server send NAK or Not Acknowledge
        the client will be send EOT and close_session
        :return: EOT
        """
        check_data = self.serial.readline()
        if check_data == NAK:
            return self.close_session()
        return False
    def close_connection(self):
        self.serial.close()
    def test(self):
        self.serial.write("test")
    def send_string(self,string):
        self.serial.write(string)