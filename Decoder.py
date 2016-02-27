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
        self.RawCode = msgCfgElement.find("RawCode").text
        self.changeFieldList = []
        for changeFieldElement in msgCfgElement.findall("ChangeField"):
            self.changeFieldList.append(ChangeField(changeFieldElement))



class TestCaseXmlTPL():
    def __init__(self, pathStr):
        self.root = ET.parse(pathStr).getroot()
        self.msgList = []
        for msgTagElement in self.root.findall("Msg"):
            self.msgList.append(Message(msgTagElement))


# class DimConverter():
#     def __init__(self,msgObj):
#         self.ObjH = HDRItem()
#         self.listAVPs = []
#         self.rawCode2Struct(self)
#
#     def rawCode2Struct(self):
#         stripHdr(self.ObjH, self.strRawCode)
#         self.listAVPs = splitMsgAVPs(self.ObjH.msg)
#
#     def converter(self):
#         pass



if __name__ == '__main__':
    LoadDictionary("dictDiameter.xml")
    tcXmlTplObj = TestCaseXmlTPL("TCTemplete.xml")
    print(tcXmlTplObj)
    # LoadDictionary("dictDiameter.xml")
    # msg="0100008c8000010100000000000000010860000100000108400000167374612e737072696e742e636f6d00000000012840000012737072696e742e636f6d0000000001014000000e00010a1e60c800000000010a4000000c000028af0000010d000000154c616e64736c69646548534757000000000001024000000c01000022000001164000000c4f32a086"
    # print "="*30
    # H=HDRItem()
    # stripHdr(H,msg)
    # avps=splitMsgAVPs(H.msg)
    # cmd=dictCOMMANDcode2name(H.flags,H.cmd)
    # if cmd==ERROR:
    #     print 'Unknown command',H.cmd
    # else:
    #     print cmd
    # print "Hop-by-Hop=",H.HopByHop,"End-to-End=",H.EndToEnd,"ApplicationId=",H.appId
    # for avp in avps:
    #   print "RAW AVP",avp
    #   print "Decoded AVP",decodeAVP(avp)
    # print "-"*30





