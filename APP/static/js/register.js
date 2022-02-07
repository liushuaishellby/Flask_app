//绑定获取验证码点击事件
function bindCaptchaBtnClick() {
    $("#captcha-btn").on("click", function (event) {
        var $this = $("#captcha-btn");
        //获取发送验证码的邮箱
        var email = $("input[name='email']").val();
        //判断邮箱是为空
        if (!email) {
            alert("请输入邮箱")
            return;
        }
        //通过ajax发送请求
        $.ajax({
            url: "/api/email",
            type: "POST",
            data: {
                "email": email
            },
            //接收响应数据
            success: function (res) {
                //获取响应状态码
                var code = res['code'];
                //判断状态码是否为200
                if (code === 200) {
                    //取消按钮的点击事件
                    $this.off("click");
                    //开始倒计数
                    var countDown = 60;
                    var timer = setInterval(function () {
                        countDown -= 1;
                        if (countDown > 0) {
                            $this.text(countDown + "秒后重新发送");
                        } else {
                            $this.text("获取验证码")
                            //重新执行这个函数，重新绑定点击事件
                            bindCaptchaBtnClick();
                            //清除倒计时
                            clearInterval(timer)
                        }
                    },1000)
                    alert("验证码发送成功！")
                } else {
                    alert(res['msg'])
                }

            }

        })
    });

}


$(function () {
    bindCaptchaBtnClick();
})