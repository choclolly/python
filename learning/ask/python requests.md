#requests.post()方法中的data参数和json参数
    url
        https://www.jianshu.com/p/9095a27b1bf2
    json和dict
        python中的dict类型要转换为json格式的数据需要用到json库：
            import json

            <json> = json.dumps(<dict>)
            <dict> = json.loads(<json>)
        需要注意的是python中并没有json类型这一说法，通过json.dumps(<dict>)转换的字典对象，最后得到的是一个字符串对象，也就是说，在python中json格式的数据实际上就是一个字符串
            >>> j = json.dumps(<dict>)
            >>> type(j)
            <class 'str'>
        虽说json格式的数据在python中是以字符串的类型存在的，但是通过str(<dict>)工厂函数所得到的结果同json.dumps(<dict>)方法所得到的结果是不相同的
            >>> d = {'a': 1, 'b': 2}
            >>> d_d = {"a": 1, "b": 2}
            >>> string = str(d)
            >>> string_d = str(d_d)
            >>> js = json.dumps(d)
            >>> js_d = json.dumps(d_d)
            >>> string == string_d
            True
            >>> js = js_d
            True
            >>> string == js
            False
            >>> string
            "{'a': 1, 'b': 2}"
            >>> js
            '{"a": 1, "b": 2}'
        可以看出来string和js的区别在于引号。对于可以作为json.loads(<str>)参数对象的字符串，除了要满足字典类型的格式外，所有的字符串对象必须是双引号。
    requests.post()
        在通过requests.post()进行POST请求时，传入报文的参数有两个，
            一个是data
            一个是json
            
        常见的form表单可以直接使用data参数进行报文提交，而data的对象则是python中的字典类型
        而在最新爬虫的过程中遇到了一种payload报文，是一种json格式的报文，因此传入的报文对象也应该是格式的；这里有两种方法进行报文提交：
            import requests
            import json
            
            url = "http://example.com"
            data = {
                'a': 1,
                'b': 2,
            }
            # 1
            requests.post(url, data=json.dumps(data))
            # 2-json参数会自动将字典类型的对象转换为json格式
            requests.post(url, json=data)
    other
        在requests.get()方法中可以使用params参数来构建url
        有时候请求得到的结果可能呈现乱码的状态，可以通过resp.encoding属性查看网页编码方式，
        同时可以在获取resp.text之前对resp.encoding='utf-8'赋值，这样再次获取的resp.text则会使用我们要求的编码方式。
#python requests用法总结
    url
        https://www.cnblogs.com/lilinwei340/p/6417689.html
    requests是一个很实用的Python HTTP客户端库，编写爬虫和测试服务器响应数据时经常会用到。可以说，Requests 完全满足如今网络的需求
        安装方式一般采用$ pip install requests。其它安装方式参考官方文档
    