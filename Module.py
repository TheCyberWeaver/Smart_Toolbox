
class CoderInterface:
    Name = ""
    Description = "The Author of this plugin is stupid, he gives no description about this plugin"
    version = ""
    def __init__(self, str="",key="",method=""):
        self.FamilyMember=method
        self.FamilyMembers=[]
        self.Key=key
        self.String=str
        self.configDictEncode = {
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
    def isLegal(self):
        pass

    def decode(self):
        pass


    def encode(self):
        pass
