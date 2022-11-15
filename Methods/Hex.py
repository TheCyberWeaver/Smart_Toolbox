from Module import CoderInterface
class Hex(CoderInterface):
    Name = "Hex Code"
    Description = "In mathematics and computing, the hexadecimal " \
                  "(also base-16 or simply hex) numeral system " \
                  "is a positional numeral system that represents numbers using a radix (base) of 16." \
                  "For example:\n" \
                  "abc:6162630a"
    version = '0.0.1'

    def __init__(self, str=""):
        super().__init__(str)
        self.FamilyMembers = [
            "Hex"
        ]

    def isLegal(self):
        pass

    def encode(self):
        r=''
        try:
            r = self.String.encode('utf-8').hex()
        except:
            r = 'Failed: Illegal to convert this string to hex, please check!'
        return r
    def decode(self):
        r = ''
        try:
            r = bytes.fromhex(self.String).decode('utf-8')
        except:
            r = 'Failed: This hex string is illegal, please check!'
        return r
