#coding=utf-8
import string
import os
import public
import shutil
from xml.etree import ElementTree
from xml.etree.ElementTree import Element

from libDiameter import HDRItem

class TestCase:
    def __init__(self):
        self.m_invokeTime = 0
        self.opTable ={}
    
    def addPropty(self,propertyStr):
        self.opTable[self.m_invokeTime] = propertyStr
        self.m_invokeTime += 1


class CaseSetFile:
    def __init__(self, casePrefixName):
        self.testCaseList = []
        self.testCasePathStr = None
        self.caseNum = 0
        self.casePrefixName = casePrefixName

    #interface
    def writeFile(self):
        pass

    def appendCase(self, testCase):
        self.testCaseList.append(testCase) 


class HATTCaseSetFile(CaseSetFile):
    def __init__(self, casePrefixName):
        CaseSetFile.__init__(self, casePrefixName)
        

    def createHattFcasFile(self, fileName):
        if fileName:
            buildFileName = self.casePrefixName +"_" + str(self.caseNum) +  " " + fileName + '.fcas'
        else:
            buildFileName = self.casePrefixName +"_" + str(self.caseNum) + fileName + '.fcas'
        shutil.copyfile(public.Constant.HATTTPL, self.casePrefixName + "\\" +buildFileName)
        return buildFileName
    

    def addCase2Set(self, setFileElement, fcasFileName):
        item = Element('FuncTestCase', {'State':'0', 'FilePath':fcasFileName, 'ErrCode':'0', 'ErrMsg':"", 'ErrPos':"", 'ErrDesc':"", 'SimpleDesp':""})
        setFileElement.append(item)


    def writeFile(self):
        print(u'创建目录: %s, 创建hatt用例，用例个数:%d' % (self.casePrefixName, len(self.testCaseList)))
        try:
            os.makedirs(self.casePrefixName)
        except WindowsError:
            print(u"名称=%s 文件夹已经存在，无法再次创建文件夹" % self.casePrefixName)
            return
        
        caseSetTree = ElementTree.parse(public.Constant.HATTSetTPL)
        setFileElement = caseSetTree.getroot()
        
        for tcObj in self.testCaseList:
            self.caseNum += 1
            if public.FileIsVaild(tcObj.opTable[2]) == False:
                print(u"备注中包含非法字符，无法创建用例文件...备注名：%s" % tcObj.opTable[2])
                continue 
            caseFileName = self.createHattFcasFile(string.strip(tcObj.opTable[2]))
            self.addCase2Set(setFileElement, caseFileName)
        
        fileName = self.casePrefixName + "/" + self.casePrefixName + '.tcst'
        caseSetTree.write(fileName, encoding='utf8')
        public.UTF82GB2312(fileName)


    
class MMLCaseSetFile(CaseSetFile):
    def __init__(self, casePrefixName):
        CaseSetFile.__init__(self, casePrefixName)
        
    def writeMmlCase(self, mmlFileName):
        mmlFile = open(mmlFileName, 'a')
        
        for tcObj in self.testCaseList:
            tmpStr = '//%02d' % self.caseNum +  tcObj.opTable[0] + '\n'
            tmpStr +=  '//' + tcObj.opTable[1] + '\n'
            tmpStr += '//' + tcObj.opTable[2] + ('\n'*6)
            mmlFile.write(tmpStr.encode("GB2312"))
            self.caseNum += 1

        mmlFile.close()
    
    def writeFile(self):
        print(u'创建MML用例，用例个数: %d' % len(self.testCaseList))
        
        try:
            os.makedirs(self.casePrefixName)
        except WindowsError:
            print(u"名称=%s 文件夹已经存在，无法再次创建文件夹" % self.casePrefixName)
            return
        
        mmlFileName =self.casePrefixName + "\\" + self.casePrefixName + '.mml'
        shutil.copyfile(public.Constant.MMLTPL, mmlFileName)
        self.writeMmlCase(mmlFileName)
        
        

