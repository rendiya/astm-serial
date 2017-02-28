class DataHandler(object):
    def __init__():
        return "DataHandler"

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