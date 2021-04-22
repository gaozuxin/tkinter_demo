#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json

import requests


def request_post(url, headers,formdata):
    res = requests.post(url=url,  headers=headers, data=json.loads(formdata))  # 发送请求
    print("url:{}\nhearders:{}\ndata:{}".format(url, headers, formdata))
    print(res.text)
    # 如果是json文件可以直接显示
    print(res.json())

    # data_eval = json.loads(r.text)  # 字符串转成字典类型
    # data_json = json.dumps(res_data, sort_keys=True, indent=4, separators=(',', ': '))  # JSON数据格式化输出
    # print(data_eval)
    data_eval = res.text
    return data_eval


def request_get(url, headers):
    if headers == "":
        headers = {
            # "Content-type": "application/json",
            "Accept-Language":"zh-CN,zh;q=0.9",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"

        }
        print("url:{}\nhearders:{}".format(url, headers))
    res = requests.get(url=url, headers=headers)
    return res


