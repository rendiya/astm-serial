# -*- coding: utf-8 -*-
# rendiya (c) 2017
from .constanta import *

class DataHandler(object):
    def __init__(self):
        pass
    def astm_string(self, string,type_data="Termination"):
        """Pad carriage return and line feed to a string
        :param string: String to pad
        :type string: str
        :returns: the padded string
        :rtype: str
        """
        check_sum = CheckSum()
        command = string+CR
        print check_sum.make_checksum('{string}{ETX}{CR}'.format(string=string,ETX=ETX,CR=CR))
        if type_data == "Intermidiate":
            return "{STX}{command}{ETB}{C}{CR}{LF}".format(STX=STX,command=command,ETB=ETB,C=check_sum.make_checksum(string+ETX+CR),CR=CR,LF=LF)
            #return STX + command + ETB + check_sum.make_checksum(string+ETX+CR) + CR + LF
        elif type_data == "Termination":
            return "{STX}{command}{ETX}{C}{CR}{LF}".format(STX=STX,command=command,ETX=ETX,C=check_sum.make_checksum(string+ETX+CR),CR=CR,LF=LF)
            #return STX + commands + ETX + check_sum.make_checksum(string+ETB+CR) + CR + LF


class CheckSum(object):
    def __init__(self):
        pass
    def make_checksum(self,message):
        """Calculates checksum for specified message.
        :param message: ASTM message.
        :type message: bytes
        :returns: Checksum value that is actually byte sized integer in hex base
        :rtype: bytes
        """
        if not isinstance(message[0], int):
            message = map(ord, message)
        return hex(sum(message) & 0xFF)[2:].upper().zfill(2).encode()