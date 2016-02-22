def UTF82GB2312(fileName):
    content = open(fileName).read()
    content = content.decode('UTF-8').encode('gbk')
    content = content.replace("encoding='utf8'", 'encoding="gb2312"')
    file_write = open(fileName,'w')
    file_write.write(content)
    file_write.close()

def FileIsVaild(fileName):
    for ch in Constant.inVaildList:
        if ch in fileName:
            return False
    return True


def isHATTOrMML(casePrefixName):
    for word in Constant.MMLKeyWord:
        if word in casePrefixName:
            return Constant.MmlCase
    
    for word in Constant.NotAutoCaseKeyWord:
        if word in casePrefixName:
            return Constant.NoAutoCase
    return Constant.HattCase
        

class Constant():
    NoAutoCase = 0
    MmlCase    = 1
    HattCase   = 2
    
    MMLTPL='mml.tpl'
    HATTTPL='hatt.tpl'
    HATTSetTPL='hattset.tpl'

    inVaildList = ['/', '\\', ':', '*', '?' , '"', '<', '>', '|'] 
    MMLKeyWord = ['mml', 'Mml', 'MML']
    NotAutoCaseKeyWord = ['Omc', 'omc', 'OMC', 'WEBAGENT', 'Webagent']

        