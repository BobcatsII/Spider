"""
  分析：
  若已登录，先退出，并清除cookie
  打开github页面，输入用户\密码，打开F12，勾选Preserve Log（显示持续日志）
  点击登录，看到各个请求过程
  打开第一个请求，进入详情页
  请求url: https://github.com/session, 请求方式：post
  继续查看Form Data 和 Headers 两部分
  Headers 包含：Cookies、Host、Origin、Refer、User-Agent等
  Form Data 包含五个字段：commit 固定字符串 Sign in， 
                         utf8 是一个勾选字符， 
                         authenticity_token 是一个Base64 加密字符串，
                         login是用户名，
                         password是密码。
  所以，无法直接构造的内容有cookies和authenticity_token.
  清除cookie，重新登录，发现 Response Headers 里有一个 Set-Cookie 字段。这就是设置Cookie的过程。
  查看网页源码，搜索到authenticity_token，他是一个隐藏式表单元素。
  以上，获取到所有信息，可以实现模拟登录了。
"""



class Login(object):
  def __init__(self):
    
