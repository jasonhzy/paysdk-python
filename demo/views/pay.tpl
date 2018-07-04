{{template "header.tpl" .}}

{{ if ne .channel "JSAPI"}}
    <body>
        {{.content}}
    </body>
{{else}}
    <script type="text/javascript">
        //调用微信JS api 支付
        function jsApiCall() {
            WeixinJSBridge.invoke(
                'getBrandWCPayRequest',
                {{ .jsapi }},
                function(res){
                    /* 参考:https://pay.weixin.qq.com/wiki/doc/api/jsapi.php?chapter=7_7&index=6
                     * res.err_msg的返回值
                     * 1.支付成功, get_brand_wcpay_request：ok
                     * 2.支付过程中用户取消, get_brand_wcpay_request：cancel
                     * 3.支付失败, get_brand_wcpay_request：fail
                     */
                    alert(JSON.stringify(res)) //供调试使用
                    if(res.err_msg == "get_brand_wcpay_request：ok" ) {
                        //用户自己的操作, eg: window.location.href = '用户自己的URL';
                    }else{
                        //用户自己的操作, eg: window.location.href = '用户自己的URL';
                    }
                }
            );
        }
        function callpay() {
            if (typeof WeixinJSBridge == "undefined"){
                if( document.addEventListener ){
                    document.addEventListener('WeixinJSBridgeReady', jsApiCall, false);
                }else if (document.attachEvent){
                    document.attachEvent('WeixinJSBridgeReady', jsApiCall);
                    document.attachEvent('onWeixinJSBridgeReady', jsApiCall);
                }
            }else{
                jsApiCall();
            }
        }
    </script>
    <body onload="callpay();"> </body>
{{end}}
</html>