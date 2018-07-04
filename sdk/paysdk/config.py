# -*- coding: utf-8 -*-
#payLib version

API_VERSION = "2"
SDK_VERSION = "python_1.0.0"

#payLib request url
API_URL = "https://api.paysdk.cn"

#支付、支付订单查询(指定id)
URI_BILL = "rest/bill"
#订单查询
URI_BILLS = "rest/bills"
#订单总数查询
URI_BILLS_COUNT = "rest/bills/count"

URI_TEST_BILL = "rest/sandbox/bill"
URI_TEST_BILLS = "rest/sandbox/bills"
URI_TEST_BILLS_COUNT = "rest/sandbox/bills/count"

#确认支付
URI_PAY_CONFIRM = "rest/bill/confirm"

#退款预退款批量审核退款订单查询(指定id)
URI_REFUND = "rest/refund"
#退款查询
URI_REFUNDS = "rest/refunds"
#退款总数查询
URI_REFUNDS_COUNT = "rest/refunds/count"
#退款状态更新
URI_REFUND_STATUS = "rest/refund/status"

#获取银行列表
URI_BC_GATEWAY_BANKS = "rest/bc_gateway/banks"

#单笔打款 - 支付宝/微信
URI_TRANSFER = "rest/transfer"
#批量打款 - 支付宝
URI_TRANSFERS = "rest/transfers"
#bc企业打款 - 支持银行
URI_BC_TRANSFER_BANKS = "rest/bc_transfer/banks"
#代付 - 银行卡
URI_BC_TRANSFER = "rest/bc_transfer"
#畅捷代付
URI_CJ_TRANSFER = "rest/cj_transfer"
#京东代付
URI_JD_TRANSFER = "rest/bc_user_transfer"
#beepay自动打款 - 打款到银行卡
URI_GATEWAY_TRANSFER = "rest/gateway/bc_transfer"

#线下支付-撤销订单
URI_OFFLINE_BILL = "rest/offline/bill"
#线下订单状态查询
URI_OFFLINE_BILL_STATUS = "rest/offline/bill/status"
#线下退款
URI_OFFLINE_REFUND = "rest/offline/refund"

#international
URI_INTERNATIONAL_BILL = "rest/international/bill"
URI_INTERNATIONAL_REFUND = "rest/international/refund"

#发送验证码
URI_SMS = "sms"

#代扣api
URI_CARD_CHARGE_SIGN = "sign"

#t1代付银行列表接口
URI_T1_EXPRESS_TRANSFER_BANKS = "rest/t1express/transfer/banks"
#代付接口
URI_T1_EXPRESS_TRANSFER = "rest/t1express/transfer"

#auth
URI_AUTH = "auth"

#subscription
URI_SUBSCRIPTION = "subscription"
URI_SUBSCRIPTION_PLAN = "plan"
URI_SUBSCRIPTION_BANKS = "subscription_banks"

#user system
#单个用户注册接口
URI_USERSYS_USER = "rest/user"
#批量用户导入接口／查询接口
URI_USERSYS_MULTI_USERS = "rest/users"
#历史数据补全接口（批量）
URI_USERSYS_HISTORY_BILLS = "rest/history_bills"

#coupon
#发放卡券, 优惠券根据id或其他条件查询
URI_COUPON = "rest/coupon"
#根据优惠券模板id或其他条件查询
URI_COUPON_TEMP = "rest/coupon/template"