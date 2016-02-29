from libDiameter import *
from libDiameterEx import *
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
        for avp in splitMsgAVPs(self.ObjH.msg):
            self.AVPsList.append(decodeAVP(avp))



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


    def findAVPByName(self):






if __name__ == '__main__':
    LoadDictionary("dictDiameter.xml")
    tcXmlTplObj = TestCaseXmlTPL("TCTemplete.xml")
    for msgObj in tcXmlTplObj.msgList:
        if msgObj.typeStr == "dim":
            converterObj = DimConverter(msgObj)
            #converterObj.printDecodeResult()
            converterObj.converter()



