{{template "header.tpl" .}}
<body>
<div align="center" id="qrcode" ></div>
<div align="center">
    <p>id：{{.id}}</p>
    <p>订单号：{{.bill_no}}</p>
    <button id="query">查询订单状态</button>
    <p id="query-result"></p>
</div>
</body>
<script src="static/js/jquery-1.11.1.min.js"></script>
<script src="static/js/qrcode.js"></script>
<script>
    {{if .code_url }}
        var options = {text: {{ .code_url }} };
        //参数1表示图像大小，取值范围1-10；参数2表示质量，取值范围'L','M','Q','H'
        var canvas = BCUtil.createQrCode(options);
        var wording=document.createElement('p');
        wording.innerHTML = "扫我 扫我";
        var element=document.getElementById("qrcode");
        element.appendChild(wording);
        element.appendChild(canvas);
    {{end}}

    $('#query').click(function(){
        $.getJSON('/bill/status', {'bill_no' : {{ .bill_no }}, 'channel' : {{ .channel }}}, function(res){
            var str = '';
            if (res.result_code == 0 ) {
                str = res.pay_result ? "支付成功" : "未支付";
            }else if (res && res.result_code != 0) {
                str = 'Error: ' + res.err_detail;
            }else {
                str = 'Notice: 该记录不存在';
            }
            $('#query-result').text(str);
        })
    });
</script>
</body>
</html>