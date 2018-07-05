# -*- coding: utf-8 -*-

from paysdk.config import *
from paysdk.base import Base

class Api(Base):
    def printResp(self, data):
        if data['result_code'] > 0:
            if self.getPyVersion():
                raise ValueError(data['errMsg'])
            else:
                raise ValueError(data['errMsg'].encode('utf8'))

    def bill(self, data):
        self.getSdkVersion(data)
        if self.getSandbox():
            url = URI_TEST_BILL
        else:
            url = URI_BILL
        return self.http_post(data, url)

    def billQuery(self, data):
        if self.getSandbox():
            url = URI_TEST_BILLS
        else:
            url = URI_BILLS
        return self.http_get(data, url)

    def billCount(self, data):
        if self.getSandbox():
            url = URI_TEST_BILLS_COUNT
        else:
            url = URI_BILLS_COUNT
        return self.http_get(data, url)

    def billQueryByID(self, data):
        if self.getSandbox():
            url = URI_TEST_BILL
        else:
            url = URI_BILL
        return self.http_get(data, url)

    def refund(self, data):
        return self.http_post(data, URI_REFUND)

    def refundQuery(self, data):
        return self.http_get(data, URI_REFUNDS)

    def refundCount(self, data):
        return self.http_get(data, URI_REFUNDS_COUNT)

    def refundQueryByID(self, data):
        if self.getSandbox():
            url = URI_TEST_BILL
        else:
            url = URI_BILL
        return self.http_get(data, url)

    def refundStatus(self, data):
        return self.http_get(data, URI_REFUND_STATUS)
