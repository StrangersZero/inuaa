# coding    :utf-8
# @Time     :2022/4/18 9:53
# @Author   :张子捷
# @File     :inuaa.py
# @Software :PyCharm


from http import cookiejar
from urllib import request
from urllib import parse
import time
import json


date = str(time.localtime().tm_year) + str(time.localtime().tm_mon) + str(
    time.localtime().tm_mday)  # get the local time

_data = {'area': '江苏省+南京市+江宁区', 'province': '江苏省', 'city': '南京市'}


def localtime():
    ls = time.localtime()
    hour = ls.tm_hour
    min = ls.tm_min
    sec = ls.tm_sec
    return str(hour) + ' : ' + str(min) + ' : ' + str(sec)


def inuaa(account):
    time_now = localtime()
    opener = get_cookie(account)
    response = opener.open('https://m.nuaa.edu.cn/ncov/wap/default/save',
                           data=parse.urlencode(account['data']).encode('utf-8'))
    if response.read().decode('utf-8') == '{"e":0,"m":"操作成功","d":{}}':
        print('{} i 南航成功......	登录时间---->>{}日:{}'.format(account['name'], date, time_now))
    else:
        print('{}cookie is out of date'.format(account['name']) + '===' * 30)


def get_cookie(account):
    cookie_jar = cookiejar.CookieJar()
    handler = request.HTTPCookieProcessor(cookie_jar)
    opener = request.build_opener(handler)
    info = dict()
    info['username'] = account['username']
    info['password'] = account['password']
    opener.open('https://m.nuaa.edu.cn/uc/wap/login/check', data=parse.urlencode(account).encode('utf-8'))
    return opener


def loadjson():
    with open("data.json", "r") as fp:
        tem = json.load(fp)
    if tem[-1:][0]["if in school"] == "1":
        for i in tem[:-1]:
            i["data"] = _data
    else:
        pass
    return tem[:-1]


if __name__ == '__main__':
    for item in loadjson():
        inuaa(item)
        time.sleep(0.5)
    print("按Ctrl+C退出")
    time.sleep(10)
