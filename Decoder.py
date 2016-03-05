from libDiameter import *
from TestCaseCfgTemplete import *



class DimConverter():
    def __init__(self, msgObj):
        self.ObjH = HDRItem()
        self.msgObj = msgObj
        stripHdr(self.ObjH, self.msgObj.rawCodeStr)
        self.avpsList = []
        for avpRaw in splitMsgAVPs(self.ObjH.msg):
            self.avpsList.append(decodeAVP(avpRaw, self.ObjH.cmd))


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


    def replaceAvpsList(self, nameStr, fieldObj):
        pass


    def encodeNewRawCode(self, newAvpList):
        pass


    def replaceByChangeField(self, changeFieldObj,resultList):
        for field in changeFieldObj.fieldList:
            newAvpList = self.replaceAvpsList(changeFieldObj.changeFieldNameStr, field)


    def converter(self):
        resultList = [].append(self.tuple2List(self.avpsList))
        for changeFieldObj in self.msgObj.changeFieldList:
            for tmpResult in resultList:
                newResultList = self.replaceByChangeField(changeFieldObj, tmpResult)
            resultList = newResultList

        for result in resultList:
            self.encodeNewRawCode(result)









if __name__ == '__main__':
    LoadDictionary("dictDiameter.xml")
    tcXmlTplObj = TestCaseXmlTPL("TCTemplete.xml")
    for msgObj in tcXmlTplObj.msgList:
        if msgObj.typeStr == "dim":
            converterObj = DimConverter(msgObj)
            print(converterObj)
            #converterObj.converter()



