# -*- coding: utf-8 -*-
from aliyunsdkcore.client import AcsClient
from aliyunsdkrds.request.v20140815.ModifySecurityIpsRequest import ModifySecurityIpsRequest
from aliyunsdkrds.request.v20140815 import DescribeDBInstancesRequest

import os
import json
import urllib.request

    
def GetLocalIP():
    IPInfo = urllib.request.urlopen("http://members.3322.org/dyndns/getip").read()
    IP = IPInfo.strip()
    return IP
# 初始化客户端
client = AcsClient(
    ak=os.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"),           # 替换为你的 AccessKey ID
    secret=os.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"),   # 替换为你的 AccessKey Secret
    region_id='cn-hangzhou'      # 替换为你的实例所在地域
)

# 2. 创建请求对象
request = DescribeDBInstancesRequest.DescribeDBInstancesRequest()
request.set_accept_format("json")  # 返回JSON格式

# （可选）设置查询参数
# request.set_PageSize(100)        # 每页实例数（默认30，最大100）
# request.set_PageNumber(1)         # 页码
# request.set_DBInstanceId("rm-xxx") # 按实例ID过滤

# 3. 发起请求并获取响应
response = client.do_action_with_exception(request)
j = json.loads(response.decode("utf-8"))

for dbinstance in  j["Items"]["DBInstance"]:
    print(dbinstance["DBInstanceId"])

    # 创建请求对象
    request = ModifySecurityIpsRequest()
    request.set_accept_format('json')
    
    ip=GetLocalIP()
    # 设置参数
    request.set_DBInstanceId(dbinstance["DBInstanceId"])            # 替换为你的实例ID
    request.set_SecurityIps(ip)  # 要设置的IP地址列表，逗号分隔
    
    # 发送请求
    response = client.do_action_with_exception(request)
    
    # 打印返回结果
    print(response.decode('utf-8'))
    
