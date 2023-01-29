import base64
from ..Module import CoderInterface
class Base(CoderInterface):
    Name = "Base Family"
    Description = "Common to all binary-to-text encoding schemes, " \
                  "Base64 is designed to carry data stored in binary formats " \
                  "across channels that only reliably support text content. \n" \
                  "For example:\n" \
                  "abc:YWJjCg=="
    version = '0.0.1'

    def __init__(self,str="",method="64"):
        super().__init__(str,method=method)
        self.FamilyMembers = [
            "64",
            "32",
            "16",
        ]
        self.configDictEncode = {
            "64": "self.base64_encode()",
            "32": "self.base32_encode()",
            "16": "self.base16_encode()",

        }
        self.configDictDecode = {
            "64": "self.base64_decode()",
            "32": "self.base32_decode()",
            "16": "self.base16_decode()",
        }

        self.FailReport='[Failed]: This base'+' string is illegal, please check!'
    def isLegal(self):
        pass
    def encode(self):
        return eval(self.configDictEncode[self.FamilyMember])
    def decode(self):
        return eval(self.configDictDecode[self.FamilyMember])

    def base64_decode(self):
        r = ''
        try:
            r = base64.b64decode(self.String).decode('utf-8')
        except:
            r = self.FailReport
        return r

    def base64_encode(self):
        r = ''
        try:
            r = base64.b64encode(self.String.encode('utf-8')).decode('utf-8')
        except:
            r =self.FailReport
        return r

    def base32_decode(self):
        r = ''
        try:
            r = base64.b32decode(self.String).decode('utf-8')
        except:
            r = self.FailReport
        return r

    def base32_encode(self):
        r = ''
        try:
            r = base64.b32encode(self.String.encode('utf-8')).decode('utf-8')
        except:
            r = self.FailReport
        return r

    def base16_decode(self):
        r = ''
        try:
            r = base64.b16decode(self.String).decode('utf-8')
        except:
            r = self.FailReport
        return r

    def base16_encode(self):
        r = ''
        try:
            r = base64.b16encode(self.String.encode('utf-8')).decode('utf-8')
        except:
            r = self.FailReport
        return r