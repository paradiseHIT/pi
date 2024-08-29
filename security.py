#!/usr/bin/env python
#-*- coding:utf8 -*-
# Author Shi Xing <shi-xing-xing@163.com> 2024-08-14 23:20:08

#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import os
import sys

from typing import List

from alibabacloud_ecs20140526.client import Client as Ecs20140526Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_ecs20140526 import models as ecs_20140526_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
import urllib.request


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> Ecs20140526Client:
        """
        使用AK&SK初始化账号Client
        @return: Client
        @throws Exception
        """
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考。
        # 建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378659.html。
        config = open_api_models.Config(
            # 必填，请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID。,
            access_key_id=os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'],
            # 必填，请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_SECRET。,
            access_key_secret=os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET']
        )
        # Endpoint 请参考 https://api.aliyun.com/product/Ecs
        config.endpoint = f'ecs-cn-hangzhou.aliyuncs.com'
        return Ecs20140526Client(config)

    @staticmethod
    def GetLocalIP():
        IPInfo = urllib.request.urlopen("http://members.3322.org/dyndns/getip").read()
        IP = IPInfo.strip()
        return IP

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()

        src_ip = Sample.GetLocalIP()
        print(f"src_ip {src_ip}")

        permissions_0 = ecs_20140526_models.AuthorizeSecurityGroupRequestPermissions(
            policy='accept',
            priority='1',
            ip_protocol='TCP',
            source_cidr_ip=src_ip,
            port_range='22/22',
            description='22 by nas'
        )
        permissions_1 = ecs_20140526_models.AuthorizeSecurityGroupRequestPermissions(
            policy='accept',
            priority='1',
            ip_protocol='TCP',
            source_cidr_ip=src_ip,
            port_range='3360/3360',
            description='3360 by nas'
        )
        authorize_security_group_request = ecs_20140526_models.AuthorizeSecurityGroupRequest(
            region_id='cn-hangzhou',
            security_group_id='sg-bp10isrefh0g1x51pdj5',
            permissions=[
                permissions_0,
                permissions_1
            ]
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            ret = client.authorize_security_group_with_options(authorize_security_group_request, runtime)
            print(ret)
        except Exception as error:
            # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        src_ip = Sample.GetLocalIP()

        permissions_0 = ecs_20140526_models.AuthorizeSecurityGroupRequestPermissions(
            policy='accept',
            priority='1',
            ip_protocol='TCP',
            source_cidr_ip=src_ip,
            port_range='22/22',
            description='22 by nas'
        )
        permissions_1 = ecs_20140526_models.AuthorizeSecurityGroupRequestPermissions(
            policy='accept',
            priority='1',
            ip_protocol='TCP',
            source_cidr_ip=src_ip,
            port_range='3360/3360',
            description='3360 by nas'
        )
        authorize_security_group_request = ecs_20140526_models.AuthorizeSecurityGroupRequest(
            region_id='cn-hangzhou',
            security_group_id='sg-bp10isrefh0g1x51pdj5',
            permissions=[
                permissions_0,
                permissions_1
            ]
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            await client.authorize_security_group_with_options_async(authorize_security_group_request, runtime)
        except Exception as error:
            # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)


if __name__ == '__main__':
    Sample.main(sys.argv[1:])