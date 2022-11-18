from ..Module import CoderInterface
class Morse(CoderInterface):

    Name = "Morse Code"
    Description = "Morse code is a method used in telecommunication" \
                  " to encode text characters as standardized sequences of two different signal durations, " \
                  "called dots and dashes, or dits and dahs.\n" \
                  " For example: \n " \
                  "abc:.-/-.../-.-./"

    version = '0.0.2'

    def __init__(self, str="",sign="/"):
        super().__init__(str=str,key=sign,method="")
        self.FamilyMembers = [
            "Morse"
        ]
        self.MorseList = {
            ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G",
            "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N",
            "---": "O", ".--．": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
            "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z",

            "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
            ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9",

            ".-.-.-": ".", "---...": ":", "--..--": ",", "-.-.-.": ";", "..--..": "?",
            "-...-": "=", ".----.": "'", "-..-.": "/", "-.-.--": "!", "-....-": "-",
            "..--.-": "_", ".-..-.": '"', "-.--.": "(", "-.--.-": ")", "...-..-": "$",
            ".. ..": "&", ".--.-.": "@", ".-.-.": "+",
            " ":" ",
            "[??]":"[??]",
            "":""
        }
        self.reverse_MorseList = {v: k for k, v in self.MorseList.items()}


    def isLegal(self):
        for x in self.String:
            if x != '.' and x != '-' and x != self.Key and x!= ' ':
                return False
        return True


    def decode(self):
        if self.isLegal():
            # 分割，字符串string，分割标识符sign
            lists = self.String.split(self.Key)
            str = ''
            for code in lists:
                str += self.MorseList.get(code)
            return str
        else:
            return 'Failed: The morse_code string is illegal, please check!!!'


    def encode(self):
        str = ''
        for char in self.String:
            str += self.reverse_MorseList.get(char.upper(),"[??]")
            str += self.Key
        return str