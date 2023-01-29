class CoderInterface:
    Name = "CodeInterface"  #模块名称
    Description = "The Author of this plugin is stupid, he gives no description about this plugin"  #模块描述，展示到Info窗口
    version = ""    #模块版本
    def __init__(self, str="",key="",method=""):
        self.FamilyMember=method    #当前使用的加密族成员
        self.FamilyMembers = []#加密族成员列表
        self.Key=key        #用户输入的密钥
        self.String=str     #用户输入的字符串
        self.FailedStringOutput="Sorry, something went wrong!!!"
        self.configDictEncode = {   #用于对应加密族成员具体的实现方法
            "be_called_function_name": "be_called_function()",
        }
    def _getString(self):
        return self.String

    def _setString(self,str):
        self.String=str

    def getFamilyMember(self):
        return self.FamilyMembers

    def setFamilyMember(self,method):
        self.FamilyMember=method

    def getKey(self):
        return self.Key

    def setKey(self,key):
        self.Key=key

    # 判断输入的字符串是否合法，返回布尔变量
    def isLegal(self):
        pass

    # 加密输入的字符串
    def decode(self):
        pass

    # 解密输入的字符串
    def encode(self):
        pass

"""
#写给小白的测试代码，复制到你的程序的底部
if __name__ == "__main__":
    Transcoder=CoderInterface("abc",key="",method="")
    
    encodedString=Transcoder.encode()
    
    Transcoder.String=encodedString
    decodedString=Transcoder.decode()
    
    print("[encoded from original string]:",encodedString)
    print("[decoded from encoded string]:",decodedString)
"""

"""
详细说明：
由于一种加密方法可以有多个变种，所以提供了加密族成员列表，用于储存一类加密方法下有哪些具体分支，它们会被展示在界面二级窗口上。
若此加密方法为单一方法，则只需要在加密族成员列表添加加密方法本身即可
self.Key里储存了用户当前输入的密钥
islegal暂时无需实现
若模块和此文件在同级目录下，import此接口的语句：
    from Module import CoderInterface
"""