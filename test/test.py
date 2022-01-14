import os
import re

import requests
import subprocess
import platform
import sys

from fumo_test import config


header = {
    'Cache-Control': 'private',
    'Connection': 'close',
    'User-Agent': 'HTTP SyncML Client [en] (WinNT; I)',
    'Accept-Language': 'en',
    'Accept-Charset': 'utf-8',
    # 'Host': "127.0.0.1\:9081",
    'Content-Type': 'application/vnd.syncml.dm+xml',
    # 'Content-Type': 'application/vnd.syncml.dm+wbxml',
}

def re_get_msg_id(xml):
    # <MsgID>1</MsgID>
    #return re.search(r'src=\"(?P<url>.*?)\"', search).group('url')
    return re.search(r'<MsgID>(?P<msg_id>.*?)</MsgID>', xml).group('msg_id')

def re_get_client_uri(xml):
    # <SessionID>2DF</SessionID>
    # return re.search(r'src=\"(?P<url>.*?)\"', search).group('url')
    search = re.search(r'<Source><LocURI>(?P<LocURI>.*?)</LocURI><LocName>(?P<LocName>.*?)</LocName></Source>', xml)
    loc_uri = search.group('LocURI')
    loc_name = search.group('LocName')
    return (loc_uri, loc_name)

def start_test():
   uri = re_get_msg_id("""
    <?xml version="1.0" encoding="UTF-8"?><SyncML xmlns=\'SYNCML:SYNCML1.2\'><SyncHdr><VerDTD>1.2</VerDTD><VerProto>DM/1.2</VerProto><SessionID>2DF</SessionID><MsgID>1</MsgID><Target><LocURI>http://192.168.50.134:5000/dongsheng/dm</LocURI><LocName>dongsheng_ds</LocName></Target><Source><LocURI>IMEI:861139020041603</LocURI><LocName>861139020041603</LocName></Source><Cred><Meta><Format xmlns=\'syncml:metinf\'>b64</Format><Type xmlns=\'syncml:metinf\'>syncml:auth-md5</Type></Meta><Data>4p4RdCYSC+f0Jb3U2gBpEQ==</Data></Cred><Meta><MaxMsgSize>36864</MaxMsgSize><MaxObjSize>1048576</MaxObjSize></Meta></SyncHdr><SyncBody><Alert><CmdID>1</CmdID><Data>1201</Data></Alert><Alert><CmdID>2</CmdID><Data>1226</Data><Item><Meta><Format xmlns=\'syncml:metinf\'>b64</Format><Type xmlns=\'syncml:metinf\'>org.openmobilealliance.dm.firmwareupdate.userrequest</Type><Mark xmlns=\'syncml:metinf\'>informational</Mark></Meta><Source><LocURI>./ManagedObjects/FUMO</LocURI></Source><Data>Y2hlY2tDb25maWd1cmF0aW9u</Data></Item></Alert><Replace><CmdID>3</CmdID><Item><Source><LocURI>./DevInfo/DevId</LocURI></Source><Data>IMEI:861139020041603</Data></Item><Item><Source><LocURI>./DevInfo/Man</LocURI></Source><Data>wingtech</Data></Item><Item><Source><LocURI>./DevInfo/Mod</LocURI></Source><Data>S98421AA1</Data></Item><Item><Source><LocURI>./DevInfo/DmV</LocURI></Source><Data>1.2</Data></Item><Item><Source><LocURI>./DevInfo/Lang</LocURI></Source><Data>English</Data></Item><Item><Source><LocURI>./DevInfo/Ext/FwV</LocURI></Source><Data>full_S98421AA1-userdebug 11 RP1A.200720.011 mp1V81071 test-keys</Data></Item><Item><Source><LocURI>./DevInfo/Ext/ICCID</LocURI></Source><Data>NULL</Data></Item><Item><Source><LocURI>./DevInfo/Ext/ConfigurationVer</LocURI></Source><Data>full_S98421AA1-userdebug 11 RP1A.200720.011 mp1V81071 test-keys.0</Data></Item><Item><Meta><Format xmlns=\'syncml:metinf\'>node</Format></Meta><Source><LocURI>./DevInfo/Ext</LocURI></Source><Data>ICCID/ConfigurationVer/FwV</Data></Item></Replace><Final/></SyncBody></SyncML>
    """)
   print("uri="+uri)

if __name__ == "__main__":
    start_test()
