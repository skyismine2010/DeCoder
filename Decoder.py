import copy
from libDiameter import *
from TestCaseCfgTemplete import *


class DimConverter():
    def __init__(self, msgObj):
        self.ObjH = HDRItem()
        self.msgObj = msgObj
        stripHdr(self.ObjH, self.msgObj.rawCodeStr)
        self.avpsList = []
        for avpRaw in splitMsgAVPs(self.ObjH.msg):
            self.avpsList.append(decodeAVP(avpRaw,str(self.ObjH.cmd)))


    def __str__(self):
        resultStr = ""
        for avpTuple in self.avpsList:
            resultStr += str(avpTuple) +"\n"
        return resultStr


    def tuple2List(self, avpsList):
        tmpAVPsList = []
        for avpTuple in avpsList:
            tmpList = list(avpTuple)
            if isinstance(tmpList[2], list):
                tmpList[2] = self.tuple2List(tmpList[2])
            tmpAVPsList.append(tmpList)
        return tmpAVPsList


    def encodeNewRawCode(self, newAvpList):
        avps = []
        for avp in newAvpList:
            avps.append(encodeAVP(avp[1],avp[2]))
        ret = createRes(self.ObjH, avps)
        print(ret)



    def findAvpByAvpCodeVendorID(self, avpName, avpList):
        for avp in avpList:
            if avp[0] == avpName:
                return avp
            elif isinstance(avp[2], list):
                tmp = self.findAvpByAvpCodeVendorID(avpName, avp[2])
                if tmp != None:
                    return tmp
        return None



    def replaceAvpsListByField(self, nameStr, fieldObj, oldAvpList):
        newAvpList = copy.deepcopy(oldAvpList)
        avp = self.findAvpByAvpCodeVendorID(nameStr, newAvpList)
        if avp == None:
            print("Can not find AVP in RawCode,please check it is right or not.")
            return
        avp[2] = fieldObj.valStr
        return newAvpList


    def replaceAvpsListByChangeField(self, changeFieldObj, oldAvpList):
        resultList = []
        for field in changeFieldObj.fieldList:
            newAvpList = self.replaceAvpsListByField(changeFieldObj.changeFieldNameStr, field, oldAvpList)
            resultList.append(newAvpList)
        print("herererer %d" % len(resultList))
        return resultList


    def converter(self):
        tmpResultList = []
        tmpResultList.append(self.tuple2List(self.avpsList))

        for changeFieldObj in self.msgObj.changeFieldList:
            newTmpResultList = []
            for tmpResult in tmpResultList:
                newTmpResultList = self.replaceAvpsListByChangeField(changeFieldObj, tmpResult)
            tmpResultList = newTmpResultList

        for result in tmpResultList:
            self.encodeNewRawCode(result)



if __name__ == '__main__':
    LoadDictionary("dictDiameter.xml")
    tcXmlTplObj = TestCaseXmlTPL("TCTemplete.xml")
    for msgObj in tcXmlTplObj.msgList:
        if msgObj.typeStr == "dim":
            converterObj = DimConverter(msgObj)
            print("$"*30)
            converterObj.converter()



