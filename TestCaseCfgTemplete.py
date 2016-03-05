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
        self.changeFieldNameStr = changeFieldElement.get("ChangeFieldName")
        self.fieldList = []
        for filedElement in changeFieldElement.findall("Field"):
            self.fieldList.append(Field(filedElement))


class Message():
    def __init__(self, msgCfgElement):
        self.typeStr = msgCfgElement.get("type")
        self.msgNameStr = msgCfgElement.get("MsgName")
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


