from libDiameter import *
import xml.etree.cElementTree as ET




class Field():
    def __init__(self, fieldElement):
        self.typeStr = fieldElement.get("type")
        self.valStr = fieldElement.text
        self.trueVal = None

    def typeConvert(self):
        pass


class ChangeField():
    def __init__(self, changeFieldElement):
        self.nameStr = changeFieldElement.get("name")
        self.fieldList = []
        for filedElement in changeFieldElement.findall("Field"):
            self.fieldList.append(Field(filedElement))


class Message():
    def __init__(self, msgCfgElement):
        self.typeStr = msgCfgElement.get("type")
        self.nameStr = msgCfgElement.get("name")
        self.rawCodeStr = msgCfgElement.find("RawCode").text
        self.changeFieldList = []
        for changeFieldElement in msgCfgElement.findall("ChangeField"):
            self.changeFieldList.append(ChangeField(changeFieldElement))



class TestCaseXmlTPL():
    def __init__(self, pathStr):
        self.root = ET.parse(pathStr).getroot()
        self.msgList = []
        for msgTagElement in self.root.findall("Msg"):
            self.msgList.append(Message(msgTagElement))



class DimConverter():
    def __init__(self, msgObj):
        self.ObjH = HDRItem()
        self.AVPsList = []
        self.msgObj = msgObj
        stripHdr(self.ObjH, self.msgObj.rawCodeStr)
        for avpRaw in splitMsgAVPs(self.ObjH.msg):
            avpKeyStr = self.getAVPKey(avpRaw, self.ObjH.cmd)
            self.AVPsList.append((avpKeyStr, decodeAVP(avpRaw)))

        for avpTuple in self.AVPsList:
            print(avpTuple)


    def getAVPKey(self,avpRaw, cmdCode):
        avpCode = struct.unpack("!I",avpRaw[0:8].decode("hex"))[0]
        avpFlag = struct.unpack("!B",avpRaw[8:10].decode("hex"))[0]
        if avpFlag & DIAMETER_FLAG_VENDOR:
            vendorID = struct.unpack("!I", avpRaw[16:24].decode("hex"))[0]
        else:
            vendorID = 0
        return ("%d.%d_%d" % (cmdCode, avpCode, vendorID))


    def printDecodeResult(self):
        print "-"*30
        cmd=dictCOMMANDcode2name(self.ObjH.flags,self.ObjH.cmd)
        if cmd==ERROR:
            print 'Unknown command',self.ObjH.cmd
        else:
            print cmd
        print "Hop-by-Hop=",self.ObjH.HopByHop,"End-to-End=",self.ObjH.EndToEnd,"ApplicationId=",self.ObjH.appId
        for avp in self.AVPsList:
          print "RAW AVP",avp
          print "Decoded AVP",decodeAVP(avp)
        print "-"*30



    def converter(self):
        rawCodeList = []
        for changeFieldObj in self.msgObj.changeFieldList:
            nameStr = changeFieldObj.nameStr
            for field in changeFieldObj:
                pass


if __name__ == '__main__':
    LoadDictionary("dictDiameter.xml")
    tcXmlTplObj = TestCaseXmlTPL("TCTemplete.xml")
    for msgObj in tcXmlTplObj.msgList:
        if msgObj.typeStr == "dim":
            converterObj = DimConverter(msgObj)
            #converterObj.printDecodeResult()
           # converterObj.converter()



