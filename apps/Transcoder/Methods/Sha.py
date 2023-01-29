import hashlib
from ..Module import CoderInterface
class Sha(CoderInterface):
    Name = "Sha Family"
    Description = "All SHA-family algorithms, " \
                  "as FIPS-approved security functions, " \
                  "are subject to official validation by the CMVP " \
                  "(Cryptographic Module Validation Program)\n" \
                  "For example:\n" \
                  "abc:edeaaff3f1774ad2888673770c6d64097e391bc362d7d6fb34982ddf0efd18cb"
    version = '0.0.1'

    def __init__(self,str="",method="256"):
        super().__init__(str,method=method)
        self.FamilyMembers=[
            "512",
            "384",
            "256",
            "224",
            "1"
        ]
        self.config_dict = {
            "256": "self.sha256_encode()",
            "512": "self.sha512_encode()",
            "1": "self.sha1_encode()",
            "384": "self.sha384_encode()",
            "224": "self.sha224_encode()",
        }
    def isLegal(self):
        pass
    def encode(self):
        return eval(self.config_dict[self.FamilyMember])
    def decode(self):
        pass

    def sha256_encode(self):
        return hashlib.sha256(self.String.encode(encoding='UTF-8')).hexdigest()

    def sha512_encode(self):
        return hashlib.sha256(self.String.encode(encoding='UTF-8')).hexdigest()

    def sha1_encode(self):
        return hashlib.sha1(self.String.encode(encoding='UTF-8')).hexdigest()

    def sha384_encode(self):
        return hashlib.sha384(self.String.encode(encoding='UTF-8')).hexdigest()

    def sha224_encode(self):
        return hashlib.sha224(self.String.encode(encoding='UTF-8')).hexdigest()
