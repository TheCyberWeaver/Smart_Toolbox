from ..Module import CoderInterface
import hashlib
class MD5(CoderInterface):
    Name = "MD5"
    Description = "The MD5 message-digest algorithm is a cryptographically broken" \
                  " but still widely used hash function producing a 128-bit hash value.\n" \
                  "For example:\n" \
                  "abc:900150983cd24fb0d6963f7d28e17f72"
    version = '0.0.1'
    def __init__(self,str="",method="32"):
        super().__init__(str,method=method)
        self.FamilyMembers = [
            "32",
            "16"
        ]
        self.config_dict = {
            "32": "self.md5_32_encode()",
            "16": "self.md5_16_encode()",
        }
    def isLegal(self):
        pass
    def encode(self):
        return eval(self.config_dict[self.FamilyMember])
    def decode(self):
        pass

    def md5_32_encode(self):
        return hashlib.md5(self.String.encode(encoding='UTF-8')).hexdigest()

    def md5_16_encode(self):
        return hashlib.md5(self.String.encode(encoding='UTF-8')).hexdigest()[8:-8]
