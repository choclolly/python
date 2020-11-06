"""
参考资料
    https://www.cnblogs.com/0bug/p/8893677.html
什么是Urllib?
    Python内置的HTTP请求库
    urllib.request          请求模块
    urllib.error              异常处理模块
    urllib.parse             url解析模块
    urllib.robotparser    robots.txt解析模块
相比Python的变化
    Python2中的urllib2在Python3中被统一移动到了urllib.request中
    python2
        import urllib2
        response = urllib2.urlopen('http://www.cnblogs.com/0bug')
    Python3
        import urllib.request
        response = urllib.request.urlopen('http://www.cnblogs.com/0bug/')
"""
