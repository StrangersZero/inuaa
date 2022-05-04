# coding    :utf-8
# @Time     :2022/5/4 20:55
# @Author   :张子捷
# @File     :demo.py
# @Software :PyCharm
import json
Accounts = [
    {'username': '000000000', 'password': '000000', 'name': '0',
     'data': {'area': '江苏省+南京市+江宁区', 'province': '江苏省', 'city': '南京市'}},  # 0
    {'username': '000000001', 'password': '000000', 'name': '1',
     'data': {'area': '江苏省+南京市+江宁区', 'province': '江苏省', 'city': '南京市'}},  # 1
    {'username': '000000002', 'password': '000000', 'name': '2',
     'data': {'area': '江苏省+南京市+江宁区', 'province': '江苏省', 'city': '南京市'}},  # 2
    {'username': '000000003', 'password': '000000', 'name': '3',
     'data': {'area': '江苏省+南京市+江宁区', 'province': '江苏省', 'city': '南京市'}},  # 3
    {'username': '000000004', 'password': '000000', 'name': '4',
     'data': {'area': '江苏省+南京市+江宁区', 'province': '江苏省', 'city': '南京市'}}   # 4
]

with open("data1.json", "w") as fp:
    json.dump(Accounts, fp)
