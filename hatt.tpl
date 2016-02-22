<?xml version="1.0" encoding="gb2312"?>
<TestCase FileType="FuncTestCase">
    <Version HLRVer="4.01.20" HATTVer="HATTV1.00.00.I3" />
    <TDIndex Desp="15178401" />
    <SimpleDesp Desp="" />
    <DetailDesp Desp="" />
    <OutPutFile FilePath="tpl.fcas_out" />
    <CaseType Desp="业务测试用例" />
    <PreCondSet>
        <MMLCmd InterName="BOSS" InstName="Del User" InstID="1" AcVer="3" Weight="1" ExecTimes="1" StopMode="0" SimpleDesp="" State="3">
            <Message MsgName="Del User" Type="MML" EventNo="15000" Action="Send" Timeout="0" NewInstID="" RuleID="0" ExecNum="0" AdaNum="0" ExecTime="0" AdaTime="0" SimpleDesp="" State="3">DEL USER:IMSI=460000000000000</Message>
            <Message MsgName="ACK" Type="MML" EventNo="15001" Action="Receive" Timeout="90000" NewInstID="" RuleID="1" ExecNum="0" AdaNum="0" ExecTime="1" AdaTime="94" SimpleDesp="" State="3">ACK : DEL USER : RETN = 000000 , DESC = success  ; ACK : DEL USER : RETN = 110109 , DESC = Subscriber does not exist  ; ACK : DEL USER : RETN = 101030 , DESC = IMSI does not exist  ; ACK : DEL USER : RETN = 110109 , DESC = Subscriber does not exist  ; </Message>
        </MMLCmd>
        <MMLCmd InterName="BOSS" InstName="Del User" InstID="2" AcVer="3" Weight="1" ExecTimes="1" StopMode="0" SimpleDesp="" State="3">
            <Message MsgName="Del User" Type="MML" EventNo="15000" Action="Send" Timeout="0" NewInstID="" RuleID="0" ExecNum="0" AdaNum="0" ExecTime="0" AdaTime="0" SimpleDesp="" State="3">DEL USER:MSISDN=8613900000000</Message>
            <Message MsgName="ACK" Type="MML" EventNo="15001" Action="Receive" Timeout="90000" NewInstID="" RuleID="2" ExecNum="0" AdaNum="0" ExecTime="1" AdaTime="94" SimpleDesp="" State="3">ACK : DEL USER : RETN = 000000 , DESC = success  ; ACK : DEL USER : RETN = 101040 , DESC = ISDN is unavailable  ; ACK : DEL USER : RETN = 101030 , DESC = IMSI does not exist  ; ACK : DEL USER : RETN = 101040 , DESC = ISDN is unavailable  ; </Message>
        </MMLCmd>
        <MMLCmd InterName="BOSS" InstName="Del Auth" InstID="3" AcVer="3" Weight="1" ExecTimes="1" StopMode="0" SimpleDesp="" State="3">
            <Message MsgName="Del Auth" Type="MML" EventNo="15000" Action="Send" Timeout="0" NewInstID="" RuleID="0" ExecNum="0" AdaNum="0" ExecTime="0" AdaTime="0" SimpleDesp="" State="3">DEL AUTH:IMSI=460000000000000</Message>
            <Message MsgName="ACK" Type="MML" EventNo="15001" Action="Receive" Timeout="90000" NewInstID="" RuleID="3" ExecNum="0" AdaNum="0" ExecTime="1" AdaTime="125" SimpleDesp="" State="3">ACK : DEL AUTH : RETN = 000000 , DESC = success  ; ACK:DEL AUTH : RETN=101030, DESC=IMSI does not exist</Message>
        </MMLCmd>
        <MMLCmd InterName="BOSS" InstName="Add Auth" InstID="4" AcVer="3" Weight="1" ExecTimes="1" StopMode="0" SimpleDesp="" State="3">
            <Message MsgName="Add Auth" Type="MML" EventNo="15000" Action="Send" Timeout="0" NewInstID="" RuleID="0" ExecNum="0" AdaNum="0" ExecTime="1" AdaTime="0" SimpleDesp="" State="3">ADD AUTH:IMSI=460000000000000,SECVER=0,KI=11111111111111111111111111111111,KEYID=1</Message>
            <Message MsgName="ACK" Type="MML" EventNo="15001" Action="Receive" Timeout="90000" NewInstID="" RuleID="4" ExecNum="0" AdaNum="0" ExecTime="2" AdaTime="125" SimpleDesp="" State="3">ACK : ADD AUTH : RETN = 000000 , DESC = success  ; </Message>
        </MMLCmd>
        <MMLCmd InterName="BOSS" InstName="Add User" InstID="5" AcVer="0" Weight="1" ExecTimes="1" StopMode="0" SimpleDesp="" State="3">
            <Message MsgName="Add User" Type="MML" EventNo="15000" Action="Send" Timeout="0" NewInstID="" RuleID="0" ExecNum="0" AdaNum="0" ExecTime="0" AdaTime="0" SimpleDesp="" State="3">ADD USER:IMSI=460000000000000,MSISDN=8613900000000,PROFILE=0</Message>
            <Message MsgName="ACK" Type="MML" EventNo="15001" Action="Receive" Timeout="90000" NewInstID="" RuleID="5" ExecNum="0" AdaNum="0" ExecTime="2" AdaTime="125" SimpleDesp="" State="3">ACK : ADD USER : RETN = 000000 , DESC = success  ; </Message>
        </MMLCmd>
    </PreCondSet>
    <MessageFlow />
    <PostCondCheck />
    <VerifyRule>
        <RspRule RuleName="" RuleID="1" RuleType="Part">RETN</RspRule>
        <RspRule RuleName="" RuleID="2" RuleType="Part">RETN</RspRule>
        <RspRule RuleName="" RuleID="3" RuleType="Part">RETN</RspRule>
        <RspRule RuleName="" RuleID="4" RuleType="Part">RETN</RspRule>
        <RspRule RuleName="" RuleID="5" RuleType="Part">RETN</RspRule>
    </VerifyRule>
    <Rlt Result="0" ErrCode="0" ErrMsg="" ErrPos="" ErrDesc="" />
</TestCase>
