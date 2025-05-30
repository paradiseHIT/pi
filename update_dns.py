from aliyunsdkcore import client
from aliyunsdkalidns.request.v20150109 import DescribeDomainsRequest,DescribeDomainRecordsRequest,UpdateDomainRecordRequest
import json,urllib,re
import urllib.request
import os


#替换以下参数
ID=os.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID")
Secret=os.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET")
RegionId="cn-hangzhou"
IP1="192.168.0.1"
DomainName="yourdomain.com"
#想要自动修改的主机名和域名类型
HostRecordList = ['www','@']
HostRecordList2 = ['www2', 'www3']
Types = "A"

clt = client.AcsClient(ID,Secret,RegionId)

#获取公网ip
def GetLocalIP():
    IPInfo = urllib.request.urlopen("http://members.3322.org/dyndns/getip").read()
    IP = IPInfo.strip()
    return IP

#获取域名列表（暂时无用）
def GetDomainList():
    DomainList = DescribeDomainsRequest.DescribeDomainsRequest()
    DomainList.set_accept_format('json')
    DNSListJson = json.loads(clt.do_action(DomainList))
    print("GetDomainList ", DNSListJson)

#更新域名ip
def EditDomainRecord(HostName, RecordId, Types, IP):
    UpdateDomainRecord = UpdateDomainRecordRequest.UpdateDomainRecordRequest()
    UpdateDomainRecord.set_accept_format('json')
    UpdateDomainRecord.set_RecordId(RecordId)
    UpdateDomainRecord.set_RR(HostName)
    UpdateDomainRecord.set_Type(Types)
    UpdateDomainRecord.set_TTL('600')
    UpdateDomainRecord.set_Value(IP)
    UpdateDomainRecordJson = json.loads(clt.do_action(UpdateDomainRecord))
    print(UpdateDomainRecordJson)

#获取域名信息
def GetAllDomainRecords(DomainName, Types, HostNameList, IP):
    DomainRecords = DescribeDomainRecordsRequest.DescribeDomainRecordsRequest()
    DomainRecords.set_accept_format('json')
    DomainRecords.set_DomainName(DomainName)
    DomainRecordsJson = json.loads(clt.do_action(DomainRecords))
    for HostName in HostNameList:
        for x in DomainRecordsJson['DomainRecords']['Record']:
            RR = x['RR']
            Type = x['Type']
            print("RR=" + RR + ",Type=" + Type)
            if RR == HostName and Type == Types:
                RecordId = x['RecordId']
                print(RecordId)
                EditDomainRecord(HostName, RecordId, Types, IP)

GetAllDomainRecords(DomainName, Types, HostRecordList, IP1)
IP = GetLocalIP()
GetAllDomainRecords(DomainName, Types, HostRecordList2, IP)
