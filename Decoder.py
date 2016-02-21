from libDiameter import *
import xml.etree.cElementTree as ET

def loadTCTemplete(str):
    root = ET.parse(str).getroot()
    for msgElement in root.findall("Msg"):
        if msgElement.get("type") == "dim":
            strRawCode = msgElement.findtext("RawCode")
            objConverter = DimConverter(msgElement.get("ChangeField"), strRawCode, msgElement.get("pos"))






class DimConverter():
    def __init__(self,strChangeField, strRawCode, strPos):
        self.strChangeField = strChangeField
        self.strRawCode = strRawCode
        self.strPos = strPos
        self.ObjH = HDRItem()
        self.listAVPs = []
        self.rawCode2Struct(self)

    def rawCode2Struct(self):
        stripHdr(self.ObjH, self.strRawCode)
        self.listAVPs = splitMsgAVPs(self.ObjH.msg)

    def



if __name__ =="__main__":
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
    loadTCTemplete("TCTemplete.xml")


