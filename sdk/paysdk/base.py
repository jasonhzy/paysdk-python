# -*- coding: utf-8 -*-

import sys, time, hashlib, requests, json, urllib
from paysdk.config import API_URL, API_VERSION, SDK_VERSION

class Base:
    def __init__(self):
        self.app_id = ''
        self.app_secret = ''
        self.master_secret = ''
        self.test_secret = ''
        self.flag = False
        self.timeout = 30

    def registerApp(self, app_id, app_secret, master_secret, test_secret) :
        self.app_id = app_id
        self.app_secret = app_secret
        self.master_secret = master_secret
        self.test_secret = test_secret

    def setSandbox(self, flag = False):
        self.flag = flag

    def getSandbox(self):
        return self.flag

    def setTimeout(self, timeout = 30):
        self.timeout = timeout

    def getTimeout(self):
        return self.timeout

    def getPyVersion(self):
        if sys.version_info[0] >= 3:
            return True
        else:
            return False

    def getTimestamp(self):
        return int(time.time() * 1000)

    def getSign(self, app_id, timestamp, app_secret):
        return hashlib.md5((app_id + str(timestamp) + app_secret).encode('UTF-8')).hexdigest()

    def getSdkVersion(self, data):
        data["bc_analysis"] = {'sdk_version' : SDK_VERSION}

    def getApiUrl(self, url):
        return API_URL + '/' + API_VERSION + '/' + url

    def getCommonParams(self, data, secret_type = 0):
        if secret_type == 1:
            secret = self.master_secret
            param = 'Master Secret'
        elif secret_type == 2:
            secret = self.test_secret
            param = 'Test Secret'
        else:
            secret = self.app_secret
            param = 'APP Secret'

        if not self.app_id:
            raise ValueError('APP ID is empty')

        if not secret:
            raise ValueError('%s is empty'.format(param))

        data['app_id'] = self.app_id
        if ('timestamp' not in data) or (not data['timestamp']):
            data["timestamp"] = self.getTimestamp()
        data["app_sign"] = self.getSign(data["app_id"], data["timestamp"], secret)

    def http_get(self, data, request_url):
        self.getCommonParams(data)
        url_prefix = self.getApiUrl(request_url)
        if self.getPyVersion():
            params = urllib.parse.urlencode({'para': json.dumps(data)}).encode('utf-8')
        else:
            params = urllib.urlencode({'para' : json.dumps(data)})
        url = url_prefix + '?' + params
        r = requests.get(url, timeout=self.getTimeout()) #设置超时时间30s
        r.encoding = 'utf-8'

        if r.status_code != requests.codes.ok:
            r.raise_for_status()
        return r.json()
    def http_post(self, data, request_url):
        self.getCommonParams(data)
        url = self.getApiUrl(request_url)
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(data), timeout=self.getTimeout(), headers=headers)  # 设置超时时间30s
        if r.status_code != requests.codes.ok:
            r.raise_for_status()
        return r.json()