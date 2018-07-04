<!Doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>{% if title %} {{ title }} {% else %} BeeCloud支付示例 {% endif %}</title>
    <link rel="shortcut icon" href="/static/img/favicon.ico" type="image/x-icon" />
    <link rel="stylesheet" href="/static/css/demo.css" type="text/css">
</head>
<body>
    <table border="1" align="center" cellspacing=0>
        {% if type=='bill' %}
            <tr><th>ID</th><th>是否支付</th><th>创建时间</th><th>总价(分)</th><th>渠道类型</th><th>订单号</th><th>订单标题</th></tr>
            {% if data %}
                {% for v in data %}
                   <tr>
                   <td>{{ v.id }}</td>
                   <td>{% if v.refund_result %}已退款{% elif v.spay_result %}已支付{% else %}未支付{% endif %}</td>
                   <td> {{v.create_time}}</td>
                   <td>{{v.total_fee}}</td>
                   <td>{{v.sub_channel}}</td>
                   <td>{{v.bill_no}}</td>
                   <td>{{v.title}}</td>
                   </tr>
                {% endfor %}
            {% else %}
                <tr><td colspan="9" align="center">无支付订单记录</td></tr>
            {% endif %}
            {% if count %}
                <tr><td colspan="1">支付订单总数:</td><td colspan="8"> {{ count }}</td></tr>
            {% endif %}

        {% elif type=='refund' %}
            <tr><td colspan="11"><h3>注意:退款状态更新接口提供查询退款状态以更新退款状态的功能，用于对退款后不发送回调的渠道（WX、YEE、KUAIQIAN、BD）退款后的状态更新。</h3></td></tr>
            <tr><th>ID</th><th>退款是否成功</th><th>退款是否完成</th><th>退款创建时间</th><th>退款号</th><th>订单金额(分)</th><th>退款金额(分)</th><th>渠道类型</th><th>订单号</th><th>订单标题</th><th>查看状态</th></tr>;
            {% if data %}
                {% for v in data %}
                   <tr>
                   <td>{{v.id}}</td>
                   <td>{% if v.refund %}成功{% else %}失败{% endif %}</td>
                   <td>{% if v.finish %}完成{% else %}未完成{% endif %}</td>
                   <td> {{v.create_time }}</td>
                   <td>{{v.refund_no}}</td>
                   <td>{{v.total_fee}}</td>
                   <td>{{v.refund_fee}}</td>
                   <td>{{v.sub_channel}}</td>
                   <td>{{v.bill_no}}</td>
                   <td>{{v.title}}</td>
                   <td>
                     {% if v.channel %}
                        <a href='/refund/status?channel={{v.channel}}&refund_no={{v.refund_no}}' target='_blank'>查询</a>
                     {% endif %}
                   </td>
                   </tr>
                {% endfor %}
            {% else %}
               <tr><td colspan="9">无退款订单记录</td></tr>
            {% endif %}
            {% if count %}
               <tr><td colspan="1">退款订单总数:</td><td colspan="10"> {{ count }}</td></tr>
            {% endif %}
        {% endif %}
    </table>
</body>
</html>