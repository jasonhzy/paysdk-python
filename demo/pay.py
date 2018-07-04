# -*- coding: utf-8 -*-

import sys
from os import path

# sys.path.append(path.dirname(path.realpath(__file__)) + '/../')
from flask import Flask, render_template, request, redirect
from paysdk.api import Api
from common import *

app = Flask(__name__, static_folder='static', template_folder='views')

apiClass = Api()
apiClass.registerApp(APP_ID, APP_SECRET, MASTER_SECRET, TEST_SECRET)
apiClass.setSandbox(False)

@app.route('/')
def index():
    return render_template('index.tpl')

@app.route('/bill', methods = ['GET'])
def pay():
    channel = request.args.get('type')

    bill = {}
    timestamp = apiClass.getTimestamp()

    bill["timestamp"] = timestamp
    bill["bill_no"] = "pydemo" + str(timestamp)
    # total_fee(int 类型) 单位分
    bill["total_fee"] = 1
    # title UTF8编码格式，32个字节内，最长支持16个汉字
    bill["title"] = 'py ' + channel + u'支付测试'
    # 渠道类型:ALI_WEB 或 ALI_QRCODE 或 UN_WEB或JD_WAP或JD_WEB, BC_GATEWAY为京东、BC_WX_WAP、BC_ALI_WEB渠道时为必填, BC_ALI_WAP不支持此参数
    bill["return_url"] = "https://paysdk.cn"
    '''
    选填 optional, 附加数据, eg: {"key1”:“value1”,“key2”:“value2”}
    用户自定义的参数，将会在webhook通知中原样返回，该字段主要用于商户携带订单的自定义数据
    '''
    bill["optional"] = {'company' : 'paysdk'}

    '''
    选填 订单失效时间bill_timeout
    必须为非零正整数，单位为秒，建议最短失效时间间隔必须大于360秒
    京东(JD*)不支持该参数。
    '''
    # bill["bill_timeout"] = 360
    '''
    notify_url 选填，该参数是为接收支付之后返回信息的,仅适用于线上支付方式, 等同于在beecloud平台配置webhook，
    如果两者都设置了，则优先使用notify_url。配置时请结合自己的项目谨慎配置，具体请
    参考demo/webhook.php
    '''
    # bill["notify_url"] = "https://beecloud.cn"

    '''
    buyer_id选填
    商户为其用户分配的ID.可以是email、手机号、随机字符串等；最长64位；在商户自己系统内必须保证唯一。
    '''
    # bill["buyer_id"] = "xxxx"

    '''
    coupon_id string 选填 卡券id
    传入卡券id，下单时会自动扣除优惠金额再发起支付
    '''
    # bill["coupon_id"] = "xxxxxx"

    '''
    analysis选填, 分析数据
    用于统计分析的数据，将会在控制台的统计分析报表中展示，用户自愿上传。包括以下基本字段：
         os_name(系统名称，如"iOS"，"Android") os_version(系统版本，如"5.1") model(手机型号，如"iPhone 6")
         app_name(应用名称) app_version(应用版本号) device_id(设备ID) category(类别，用户可自定义，如游戏分发渠道，门店ID等)
         browser_name(浏览器名称) browser_version(浏览器版本)
    下单产品保存格式：
         product固定的key，
         name 产品名，eg: T恤
         count 产品件数, eg: 1
         price 单价（单位分）,eg : 200
     {"product":[{"name" : "xxx", "count":1, "price" : 111}, {"name" : "yyy", "count":2, "price" : 222}]}
    '''
    detail = {}
    detail["product"] = [{'name': 'xxx', 'count': 1, 'price': 111}, {'name': "yyy", 'count': 2, 'price': 222}]
    detail["otherkey"] = "othervalue"
    bill["analysis"] = detail

    if channel == 'ALI_WEB' : #支付宝即时到账
        bill['channel'] = 'ALI_WEB'
    elif channel == 'ALI_WAP' : #支付宝移动网页
        bill['channel'] = 'ALI_WAP'
        #非必填参数,boolean型,是否使用APP支付,true使用,否则不使用
        #bill['use_app'] = false
    elif channel == 'ALI_QRCODE' : #支付宝扫码支付
        bill['channel'] = 'ALI_QRCODE'
        #qr_pay_mode必填 二维码类型含义
        #0： 订单码-简约前置模式, 对应 eliframe 宽度不能小于 600px, 高度不能小于 300px
        #1： 订单码-前置模式, 对应 eliframe 宽度不能小于 300px, 高度不能小于 600px
        #3： 订单码-迷你前置模式, 对应 eliframe 宽度不能小于 75px, 高度不能小于 75px
        bill['qr_pay_mode'] = '0'
    elif channel == 'ALI_SCAN' : #支付宝刷卡
        bill['channel'] = 'ALI_SCAN'
        bill['auth_code'] = '28886955594xxxxxxxx'
    elif channel == 'ALI_OFFLINE_QRCODE' : #支付宝线下扫码
        bill['channel'] = 'ALI_OFFLINE_QRCODE'
    elif channel == 'BD_WEB' : #百度网页支付
        bill['channel'] = 'BD_WEB'
    elif channel == 'BD_WAP' : #百度移动网页
        bill['channel'] = 'BD_WAP'
    elif channel == 'JD_B2B' : #京东B2B
        bill['channel'] = 'JD_B2B'
        '''
        bank_code(int 类型) for channel JD_B2B
        9102    中国工商银行      9107    招商银行
        9103    中国农业银行      9108    光大银行
        9104    交通银行          9109    中国银行
        9105    中国建设银行		9110 	 平安银行
        '''
        bill['bank_code'] = 9102
    elif channel == 'JD_WEB' : #京东网页
        bill['channel'] = 'JD_WEB'
    elif channel == 'JD_WAP' : #京东移动网页
        bill['channel'] = 'JD_WAP'
    elif channel == 'UN_WEB' :#银联网页
        bill['channel'] = 'UN_WEB'
    elif channel == 'UN_WAP' : #银联移动网页, 由于银联做了适配,需在移动端打开,PC端仍显示网页支付
        bill['channel'] = 'UN_WAP'
    elif channel == 'WX_NATIVE': #微信扫码
        bill['channel'] = 'WX_NATIVE'
    elif channel == 'WX_JSAPI': #微信公众号
        bill['channel'] = 'WX_JSAPI'
    elif channel == 'WX_WAP': #微信H5网页, 请在手机浏览器内测试
        bill['channel'] = 'WX_WAP'
        #需要参数终端ip，格式如下：
        bill["analysis"] = {'ip': getClientIp()}
    elif channel == 'WX_SCAN' :
        bill['channel'] = 'WX_SCAN'
        bill['auth_code'] = '13022657110xxxxxxxx'
    elif channel == 'YEE_WEB' : #易宝网页
        bill['channel'] = 'YEE_WEB'
    elif channel == 'YEE_WAP' : #易宝移动网页
        bill['channel'] = 'YEE_WAP'
        bill['identity_id'] = 'xxxxxxxxxxxxxx'
    elif channel == 'YEE_NOBANKCARD': #易宝点卡支付
        #total_fee(订单金额)必须和充值卡面额相同，否则会造成金额丢失(渠道方决定)
        bill['total_fee'] = 10
        bill['channel'] = 'YEE_NOBANKCARD'
        #点卡卡号，每种卡的要求不一样
        bill['cardno'] = '622662180018xxxx'
        #点卡密码，简称卡密
        bill['cardpwd'] = 'xxxxxxxxxxxxxx'
        '''
        frqid 点卡类型编码
        骏网一卡通(JUNNET),盛大卡(SNDACARD),神州行(SZX),征途卡(ZHENGTU),Q币卡(QQCARD),联通卡(UNICOM),
         久游卡(JIUYOU),易充卡(YICHONGCARD),网易卡(NETEASE),完美卡(WANMEI),搜狐卡(SOHU),电信卡(TELECOM),
        纵游一卡通(ZONGYOU),天下一卡通(TIANXIA),天宏一卡通(TIANHONG),32 一卡通(THIRTYTWOCARD)
        '''
        bill['frqid'] = 'SZX'
    elif channel == 'KUAIQIAN_WEB' : #快钱移动网页
        bill['channel'] = 'KUAIQIAN_WEB'
    elif channel == 'KUAIQIAN_WAP' : #快钱移动网页
        bill['channel'] = 'KUAIQIAN_WEB'
    elif channel == 'PAYPAL_PAYPAL' : #Paypal网页
        bill['channel'] = 'PAYPAL_PAYPAL'
        # currency参数的对照表, 请参考:
        # https:#github.com/paysdk/paysdk-rest-api/tree/master/international
        bill['currency'] = 'USD'
    elif channel == 'PAYPAL_CREDITCARD' : #Paypal信用卡
        bill['channel'] = 'PAYPAL_CREDITCARD'

        # currency参数的对照表, 请参考:
        # https://github.com/beecloud/beecloud-rest-api/tree/master/international
        bill['currency'] = 'USD'

        card_info = {}
        card_info['card_number'] = ''
        card_info['expire_month'] = 1
        card_info['expire_year'] = 2016
        card_info['cvv'] = 0
        card_info['first_name'] = ''
        card_info['last_name'] = ''
        card_info['card_type'] = 'visa'
        bill['credit_card_info'] = card_info
    elif channel == 'PAYPAL_SAVED_CREDITCARD' : #Paypal快捷
        bill['channel'] = 'PAYPAL_SAVED_CREDITCARD'

        #currency参数的对照表, 请参考:
        #https://github.com/beecloud/beecloud-rest-api/tree/master/international
        bill['currency'] = 'USD'
        bill['credit_card_id'] = ''
    elif channel == 'BC_GATEWAY' : #BC网关支付
        bill['channel'] = 'BC_GATEWAY'
        '''
        card_type(string 类型) for channel BC_GATEWAY
        卡类型: 1代表信用卡；2代表借记卡
        '''
        bill['card_type'] = '1'
        bill['bank'] = '交通银行'
    elif channel == 'BC_EXPRESS' : #快捷支付
        bill['channel'] = 'BC_EXPRESS'
        #银行卡卡号, (选填，注意：可能必填，根据信息提示进行调整)
        #bill['card_no'] = '622662183243xxxx'
    elif channel == 'BC_NATIVE' : #BC微信扫码
        bill['channel'] = 'BC_NATIVE'
    elif channel == 'BC_WX_WAP' : #BC微信H5支付, 请在手机浏览器内测试
        bill['channel'] = 'BC_WX_WAP'
        #需要参数终端ip，格式如下：
        bill["analysis"] = {'ip': getClientIp()}
    elif channel == 'BC_WX_SCAN' : #BC微信刷卡
        bill['channel'] = 'BC_WX_SCAN'
        bill['auth_code'] = '13022657110xxxxxxxx'
    elif channel == 'BC_WX_JSAPI': #微信公众号
        bill['channel'] = 'BC_WX_JSAPI'
    elif channel == 'BC_ALI_QRCODE' : #BC支付宝线下扫码
        bill['channel'] = 'BC_ALI_QRCODE'
    elif channel == 'BC_ALI_SCAN' : #BC支付宝刷卡
        bill['channel'] = 'BC_ALI_SCAN'
        bill['auth_code'] = '28886955594xxxxxxxx'
    elif channel == 'BC_ALI_WAP' : #请在手机浏览器内测试
        bill['channel'] = 'BC_ALI_WAP'
    elif channel == 'BC_QQ_NATIVE' :
        bill['channel'] = 'BC_QQ_NATIVE'
    elif channel == 'BC_JD_QRCODE' : #BC京东扫码
        bill['channel'] = 'BC_JD_QRCODE'
    else :
        return 'No this type.'

    try:
        result = apiClass.bill(bill)
        apiClass.printResp(result)
        if result.has_key('url') and result['url']:
            return redirect(result['url'])
        elif result.has_key('html') and result['html']:
            return result['html']
        elif result.has_key('code_url') and result['code_url']:
            return redirect(result['code_url'])
        elif result.has_key('credit_card_id') and result['credit_card_id']:
            return result['credit_card_id']
        elif result.has_key('id') and result['id']:
            return result['id']
        else:
            return ''
    except Exception as e:
        return e.message

@app.route('/bill/query')
def billQuery():
    channel = request.args.get('type')
    if channel == "ALI":
        title = u"支付宝"
    elif channel == "BD":
        title = u"百度"
    elif channel == "JD":
        title = u"京东"
    elif channel == "WX":
        title = u"微信"
    elif channel == "UN":
        title = u"银联"
    elif channel == "YEE":
        title = u"易宝"
    elif channel == "KUAIQIAN":
        title = u"快钱"
    elif channel == "PAYPAL":
        title = "PAYPAL"
    elif channel == "BC":
        title = u"BC网关/快捷支付"
    else :
        return 'No this channel'

    data = {}
    data["channel"] = channel
    data["spay_result"] = True  #只列出了支付成功的订单
    data["limit"] = 10

    try:
        list = apiClass.billQuery(data)
        apiClass.printResp(list)

        count = apiClass.billCount(data)
        apiClass.printResp(count)

        return render_template('bills.tpl', type='bill', data=list['bills'], count=count['count'], title=title + u'支付')
    except Exception as e:
        return e.message

@app.route('/refund/query')
def refundQuery():
    channel = request.args.get('type')
    if channel == "ALI":
        title = u"支付宝"
    elif channel == "BD":
        title = u"百度"
    elif channel == "JD":
        title = u"京东"
    elif channel == "WX":
        title = u"微信"
    elif channel == "UN":
        title = u"银联"
    elif channel == "YEE":
        title = u"易宝"
    elif channel == "KUAIQIAN":
        title = u"快钱"
    elif channel == "PAYPAL":
        title = "PAYPAL"
    elif channel == "BC":
        title = u"BC网关/快捷支付"
    else :
        return 'No this channel'

    data = {}
    data["channel"] = channel
    data["limit"] = 10

    try:
        list = apiClass.refundQuery(data)
        apiClass.printResp(list)

        count = apiClass.refundCount(data)
        apiClass.printResp(count)

        return render_template('bills.tpl', type='refund', data=list['refunds'], count=count['count'], title=title + u'退款')
    except Exception as e:
        return e.message

@app.route('/refund/status')
def refundStatus(self):
    refund_no = request.args.get('refund_no')
    channel = request.args.get('channel')

    data = {}
    data["refund_no"] = refund_no
    data["channel"] = channel

    if channel in {"WX", "YEE", "KUAIQIAN", "BD"}:
        apiClass.refundStatus(data)

def getClientIp() :
    return request.remote_addr

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.tpl'), 404

if __name__ == '__main__':
    app.debug = True #开启调试模式
    app.run(host='127.0.0.1', port=8080, debug=True)
