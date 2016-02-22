#coding=utf-8
import zipfile
import os
import string
from TestModule import TestCase,HATTCaseSetFile,MMLCaseSetFile
from xml.etree import ElementTree
import public

namespace = {"w":"http://schemas.openxmlformats.org/wordprocessingml/2006/main"}

def parseWordGetCaseSetName(tr):
    tcs = tr.findall("w:tc",namespaces=namespace)
    wt0 =tcs[0].find("w:p/w:r/w:t", namespaces=namespace)
    wts1 =tcs[1].findall("w:p/w:r/w:t", namespaces=namespace)
    if wt0.text != u'用例编号':
        print(u"不是以用例编号作为开头表格,跳过 (%s)!!!!" % wt0.text)
        return None
    if wts1 is None:
        print(u"用例编号后没有找到数据,格式有误(%s)!!!!" % wts1.text)
        return None
    text = ''
    for wt in wts1:
        text += wt.text
    return text
    

def parseWordDocx(docFilePath):
    testCaseFileList = []
    z = zipfile.ZipFile(docFilePath)
    doc_xml_file = z.read("word/document.xml")
    doc = ElementTree.fromstring(doc_xml_file)
    tblsList = doc.findall("w:body/w:tbl",namespaces=namespace)
    for tbl in tblsList:
        testCaseFileObj =  parseWordTables(tbl)
        if testCaseFileObj is not None:
            testCaseFileList.append(testCaseFileObj)
    print("total parse success caseset = %d" % len(testCaseFileList))
    return testCaseFileList


def parseWordTables(tbl):
    trs = tbl.findall("w:tr",namespaces=namespace)
    casePrefixName = parseWordGetCaseSetName(trs[0])
    if casePrefixName is None:
        return None
    
    ret = public.isHATTOrMML(casePrefixName)
    if ret == public.Constant.MmlCase:
        testCaseFileObj = MMLCaseSetFile(casePrefixName)
    elif ret == public.Constant.HattCase:
        testCaseFileObj = HATTCaseSetFile(casePrefixName)
    else:
        print(u"此类型用例不生成自动化.. Name=%s" % casePrefixName)
        return None
    
    #按照指定的格式跳过trs
    newTrs = trs[20:]
    for tr in newTrs:
        breakNum = True
        testCaseObj = TestCase()
        tcs = tr.findall("w:tc", namespaces=namespace)
        if len(tcs) != 4:
            print("The docx format is not ok....")
            return None
        for tc in tcs:
            if breakNum:
                breakNum = False
                continue
            tmpStr = ""
            wts = tc.findall("w:p/w:r/w:t", namespaces=namespace)
            for wt in wts:
                tmpStr += wt.text
            testCaseObj.addPropty(tmpStr)
        testCaseFileObj.appendCase(testCaseObj)
    return testCaseFileObj   
 
if __name__ == '__main__':
#   ToolType=input("please choose Tool Type(1---hatt, 2---mml):")
    for file in os.listdir("."):
        if string.split(file,".")[-1] == 'docx':
            testCaseFileList = parseWordDocx(file)
            for testCaseFileObj in testCaseFileList:
                testCaseFileObj.writeFile() 
    print(u"用例构建结束....有问题请联系...")
    os.system("pause")
    
    
    
