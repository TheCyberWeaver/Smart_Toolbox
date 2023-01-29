from Crypto.Cipher import AES
import os
import base64
from ..Module import CoderInterface
class AdvancedEncryptionStandard(CoderInterface):
    Name = "AES Family"
    Description = "The Advanced Encryption Standard (AES), also known " \
                  "by its original name Rijndael (Dutch pronunciation: " \
                  "[ˈrɛindaːl]),[5] is a specification for the encryption " \
                  "of electronic data established by the U.S. National Institute " \
                  "of Standards and Technology (NIST) in 2001."
    version = '0.0.1'

    def __init__(self,str="",method="AES ECB"):
        super().__init__(str,method=method)
        self.FamilyMembers = [
            "AES CBC",
            "AES ECB"
        ]
        self.configDictEncode = {
            "AES CBC": "self.CBC_encode()",
            "AES ECB": "self.ECB_encode()",

        }
        self.configDictDecode = {
            "AES CBC": "self.CBC_decode()",
            "AES ECB": "self.ECB_decode()",
        }

        self.FailReport='[Failed]: This base'+' string is illegal, please check!'

        self.iv=key = os.urandom(16)
    def isLegal(self):
        pass
    def encode(self):
        return eval(self.configDictEncode[self.FamilyMember])
    def decode(self):
        return eval(self.configDictDecode[self.FamilyMember])

    def CBC_encode(self):
        mode = AES.MODE_CBC
        text = add_to_16(self.String)
        cryptos = AES.new(self.Key.encode('utf-8'), mode, self.iv)
        cipher_text = cryptos.encrypt(text)# 因为AES加密后的字符串不一定是ascii字符集的，输出保存可能存在问题，所以这里转为16进制字符串
        return str(base64.b64encode(cipher_text),encoding='utf-8')

    # 解密后，去掉补足的空格用strip() 去掉
    def CBC_decode(self):
        mode = AES.MODE_CBC
        cryptos = AES.new(self.Key.encode('utf-8'), mode, self.iv)
        text = bytes(self.String, encoding='utf-8')  # 将密文转换为bytes，此时的密文还是由basen64编码过的
        text = base64.b64decode(text)  # 对密文再进行base64解码
        de_text = cryptos.decrypt(text)  # 密文进行解密，返回明文的bytes
        return str(de_text, encoding='utf-8').strip()  # 将解密后得到的bytes型数据转换为str型，并去除末尾的填充

    """
    ECB没有偏移量
    """
    def ECB_encode(self):
        mode = AES.MODE_ECB
        text = add_to_16(self.String)
        cryptos = AES.new(self.Key.encode('utf-8'), mode)
        cipher_text = cryptos.encrypt(text)  # 因为AES加密后的字符串不一定是ascii字符集的，输出保存可能存在问题，所以这里转为16进制字符串
        return str(base64.b64encode(cipher_text), encoding='utf-8')

    # 解密后，去掉补足的空格用strip() 去掉
    def ECB_decode(self):
        mode = AES.MODE_ECB
        cryptos = AES.new(self.Key.encode('utf-8'), mode)
        text = bytes(self.String, encoding='utf-8')  # 将密文转换为bytes，此时的密文还是由basen64编码过的
        text = base64.b64decode(text)  # 对密文再进行base64解码
        de_text = cryptos.decrypt(text)  # 密文进行解密，返回明文的bytes
        return str(de_text, encoding='utf-8').strip()  # 将解密后得到的bytes型数据转换为str型，并去除末尾的填充

# 如果text不足16位的倍数就用空格补足为16位
def add_to_16(text):
    if len(text.encode('utf-8')) % 16:
        add = 16 - (len(text.encode('utf-8')) % 16)
    else:
        add = 0
    text = text + ('\0' * add)
    return text.encode('utf-8')






