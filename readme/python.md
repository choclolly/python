# Idea下Python开发平台的搭建
    1，创建python项目
        IntelliJ IDEA
            File
                New
                    Project
![](learning syllabus/images\New Project.png)
                
                    发现没有Python
                
        or
        
            File
                New
                    Module
![](learning syllabus/images\New Project.png)
                        
                    发现没有Python
                    
    2，idea下python插件的安装
        IntelliJ IDEA
            File
                Settings
                    Plugins
                    搜索python
![](learning syllabus/images\search python.png) 
       
![](learning syllabus/images\search python2.png)   
 
                    install    
![](learning syllabus/images\install python plugin.png)

![](learning syllabus/images\install python plugin2.png)
                    
                    OK
                    重启ide
![](learning syllabus/images\restart.png)   
    
    3，创建python项目
        创建项目的时候，我们就可以看到python，然后选择python，选择相应的版本，点击下一步我们创建好一个python项目
        IntelliJ IDEA
            File
                New
                    Project
                    项目类型中多了一个Python。点击它
                    Python
                        Project SDK：    Python 3.7
                    Next
                        Project name：    python-example
                    Finsh
![](learning syllabus/images\New Project2.png)
            
            
            如果你的电脑中已经安装过了python的环境，它会自动检测SDK。如果没有安装，这里推荐使用Anaconda，安装与配置方法请移步python神器——Anaconda。
                url:
                        https://blog.csdn.net/qq_38188725/article/details/80624004
       
        创建好python 项目，我们就可以在里面创建python类，然后运行
            main.yp
               print("hello python")
            右键 Run 'main' or Debug 'main'

    4，关于pip
            import urllib
                No module named urllib more
            1，如果上面的错误   No module named urllib more，则是没有引入urllib的包，需要通过pip进行引入。
            2,pip引入的命令为pip install urllib ，默认安装在C:\Python27\Lib\site-packages
            3,pip未安装，则进入命令行，然后把目录切换到python的安装目录下的Script文件夹下，运行 easy_inatall pip。
        这样就可以引入python的package。
        
        注意:
            这里的python文件都必须要有明确的程序入口才能执行，不像自己随便写写的一个print一样。也就是说，必须要有 if __name__ == '__main__': 才行。
![](learning syllabus/images\if  name.png)
        
        Intellij Idea是一个非常优秀的IDE，但是JetBrains好像不希望客户利用插件来使其成为一个万能的IDE，于是它先后推出了Clion、Pycharm、Datagrip等重磅产品，都是精品，
            并着重于自己分内的语言工作。2015年之前还能在Intellij Idea的仓库里找到C/C++的插件，但是自那以后就再也不更新了，既不兼容，也无法通过上述安装插件的方式找到了。
            不知道python这个插件还能活几年，能用几年是几年吧！个人觉得集成式的IDE还是相当爽的。
            
    5,idea中java和python并存之道
        url:
            https://www.jianshu.com/p/d452cfcdda10
            
        在开发java项目的过程中，可能会有一些python的小工具并存在java项目的git中，此时需要同时编辑python和java文件
            安装python插件
                打开perference->plugin 搜索python 安装第一个插件
            配置python SDK
                IntelliJ IDEA
                    File
                        Project Structrue -> PlatFrom Settings --> SDK -> +python sdk-> 
                    virtualenv environment -> existing environment-> interceptor 
                        选择python命令路径    D:\Anaconda3\python.exe
                        勾选 make available to all projects
# Idea下建立Python工程
    url：
        https://blog.csdn.net/silentwolfyh/article/details/52191206
    一、五个步鄹：
        5.1,Windows中Python安装
            如果你的电脑中已经安装过了python的环境，IDEA它会自动检测SDK。
            如果没有安装，这里推荐使用Anaconda，安装与配置方法请移步python神器——Anaconda。
                在idea中配置python sdk
                    IntelliJ IDEA
                        File
                            Project Structrue -> 
                                PlatFrom Settings --> 
                                    SDK -> +
                                        python sdk-> 
                                            virtualenv environment -> 
                                                existing environment-> 
                                                    interceptor 
                                                        选择python命令路径    D:\Anaconda3\pythonw.exe
                                                        勾选 make available to all projects
                    OK
        5.2,Intellij IDEA中Python安装
        5.3,Intellij IDEA建立Python项目
        5.4,编辑Python脚本
        5.5,安装pip  
    二、编辑Python脚本
        python项目上右键
            New
                Python File
                    into.yp
                       #! /usr/bin/env python
                       # -*- coding: utf-8 -*-
                        
                       def foo():
                           str="function"
                           print(str);
                        
                       def foo1(num):
                           print('num' ,num);
                        
                       def foo2(name ,age):
                           print('name' ,name);
                           print('age' ,age);
                        
                       if __name__=="__main__":
                           print("main")
                           foo2('yuhui' ,30)
                           foo1(6)
                           foo()
# 查看python及其第三方库的版本和安装位置
    1，查看python版本
        python -V
        or
        python --version
        1.1，
            启动Anaconda Prompt 
            (base) D:\Anaconda3>python -V
            Python 3.7.3
        1.2，
            如果配置了python环境变量的换
            启动cmd 
            Microsoft Windows [版本 10.0.17763.475]
            (c) 2018 Microsoft Corporation。保留所有权利。
            
            C:\Users\h_don>python -V
            Python 3.7.3
            
            C:\Users\h_don>
    2，查看python安装位置
        2.1，
            启动Anaconda Prompt 
        2.2，
            找到电脑中安装Python的位置
            (base) C:\Users\h_don>where python
            D:\Anaconda3\python.exe
            
            (base) C:\Users\h_don>
# 退出python命令行
    python命令行是新手学习python过程中必须要学的一个工具
    
    首先确认pythonvan本以及python正常工作
        启动Anaconda Prompt 
        (base) PS C:\Users\h_don> python -V
        Python 3.7.3
        (base) PS C:\Users\h_don> python
        Python 3.7.3 (default, Mar 27 2019, 17:13:21) [MSC v.1915 64 bit (AMD64)] :: Anaconda, Inc. on win32
        Type "help", "copyright", "credits" or "license" for more information.
        >>>
    方式一、
        使用python提供的exit()函数
            linux平台和windows平台上的exit()函数执行结果。可以看到，都可以正常退出。唯一的区别是，windows平台cmd下结束后多输出了一行空行。
            windows
                Anaconda Prompt下
                    (base) PS C:\Users\h_don> python
                    Python 3.7.3 (default, Mar 27 2019, 17:13:21) [MSC v.1915 64 bit (AMD64)] :: Anaconda, Inc. on win32
                    Type "help", "copyright", "credits" or "license" for more information.
                    >>> exit()
                    (base) PS C:\Users\h_don>
                cmd下
                    C:\Users\h_don>python
                    Python 3.7.3 (default, Mar 27 2019, 17:13:21) [MSC v.1915 64 bit (AMD64)] :: Anaconda, Inc. on win32
                    
                    Warning:
                    This Python interpreter is in a conda environment, but the environment has
                    not been activated.  Libraries may fail to load.  To activate this environment
                    please see https://conda.io/activation
                    
                    Type "help", "copyright", "credits" or "license" for more information.
                    >>> exit()
                    
                    C:\Users\h_don>
    方式二、
        python提供的第二个函数quit()，同样是linux和windows平台，执行结果一致。都可以正常退出，windows平台cmd下quit()多输出一行空行
            linux和windows平台，执行结果一致。都可以正常退出，windows平台多输出一行空行。
            windows
                Anaconda Prompt下
                    (base) PS C:\Users\h_don> python
                    Python 3.7.3 (default, Mar 27 2019, 17:13:21) [MSC v.1915 64 bit (AMD64)] :: Anaconda, Inc. on win32
                    Type "help", "copyright", "credits" or "license" for more information.
                    >>> exit()
                    (base) PS C:\Users\h_don> python
                    Python 3.7.3 (default, Mar 27 2019, 17:13:21) [MSC v.1915 64 bit (AMD64)] :: Anaconda, Inc. on win32
                    Type "help", "copyright", "credits" or "license" for more information.
                    >>> quit()
                    (base) PS C:\Users\h_don>
                cmd下
                    C:\Users\h_don>python
                    Python 3.7.3 (default, Mar 27 2019, 17:13:21) [MSC v.1915 64 bit (AMD64)] :: Anaconda, Inc. on win32
                    
                    Warning:
                    This Python interpreter is in a conda environment, but the environment has
                    not been activated.  Libraries may fail to load.  To activate this environment
                    please see https://conda.io/activation
                    
                    Type "help", "copyright", "credits" or "license" for more information.
                    >>> quit()
                    
                    C:\Users\h_don>
    方式三、
        函数方式看完了以后，我们来看快捷键退出的方式。v
        1,快捷键Ctrl +D的组合
            linux平台和windows平台上使用Ctrl+D的组合键
            linux
                linux平台上直接退出
            windows
                windows平台上直接退出
                Anaconda Prompt下
                    (base) PS C:\Users\h_don> python
                    Python 3.7.3 (default, Mar 27 2019, 17:13:21) [MSC v.1915 64 bit (AMD64)] :: Anaconda, Inc. on win32
                    Type "help", "copyright", "credits" or "license" for more information.
                    >>>
                    (base) PS C:\Users\h_don>
                
                cmd下
                    C:\Users\h_don>python
                    Python 3.7.3 (default, Mar 27 2019, 17:13:21) [MSC v.1915 64 bit (AMD64)] :: Anaconda, Inc. on win32
                    
                    Warning:
                    This Python interpreter is in a conda environment, but the environment has
                    not been activated.  Libraries may fail to load.  To activate this environment
                    please see https://conda.io/activation
                    
                    Type "help", "copyright", "credits" or "license" for more information.
                    >>>
                    
                    C:\Users\h_don>
        2,快捷键的组合方式Ctrl+Z
            linux平台和windows平台，linux平台上显示进程已结束，程序退出。而在windows平台上按下Ctrl+Z组合键时，直接退出
            windows
                Anaconda Prompt下
                   直接退出
                   (base) PS C:\Users\h_don> python
                   Python 3.7.3 (default, Mar 27 2019, 17:13:21) [MSC v.1915 64 bit (AMD64)] :: Anaconda, Inc. on win32
                   Type "help", "copyright", "credits" or "license" for more information.
                   >>>
                   (base) PS C:\Users\h_don>
                
                cmd下
                    C:\Users\h_don>python
                    Python 3.7.3 (default, Mar 27 2019, 17:13:21) [MSC v.1915 64 bit (AMD64)] :: Anaconda, Inc. on win32
                    
                    Warning:
                    This Python interpreter is in a conda environment, but the environment has
                    not been activated.  Libraries may fail to load.  To activate this environment
                    please see https://conda.io/activation
                    
                    Type "help", "copyright", "credits" or "license" for more information.
                    >>>
                    
                    C:\Users\h_don>
    Linux平台上的python命令行退出方式
        这个方式只适合一些特殊场合，例如通过xshell工具连接到linux服务器上运行python命令行时，xshell卡死了。这个时候就可以用这个方法。
        打开另外一个命令行，输入命令：
            ps aux  | grep python
            找到所有python命令行，比如我这里就有两个，进程ID分别是12525 12655，
            然后使用kill命令杀掉这两个进程
                kill -9 12525
                kill -9 12655
# 如何查看Python 安装位置以及已经安装的库
    
    方式一、
        1，启动Anaconda Prompt 
        2，找到电脑中安装Python的位置
            (base) C:\Users\h_don>where python
            D:\Anaconda3\python.exe
            
            (base) C:\Users\h_don>
        3，打开路径， cd 到输出的路径，之后 start
            (base) C:\Users\h_don>where python
            D:\Anaconda3\python.exe
            
            (base) C:\Users\h_don>D:
            
            (base) D:\>cd D:\Anaconda3
            
            (base) D:\Anaconda3>start
        4,
            4.1,显示pip安装的所有库
                命令：pip list <or> pip freeze
                Microsoft Windows [版本 10.0.17763.475]
                (c) 2018 Microsoft Corporation。保留所有权利。
                
                (base) D:\Anaconda3>pip list
                Package                            Version
                ---------------------------------- --------
                alabaster                          0.7.12
                anaconda-client                    1.7.2
                anaconda-navigator                 1.9.7
                anaconda-project                   0.8.2
                asn1crypto                         0.24.0
                astroid                            2.2.5
                astropy                            3.1.2
                atomicwrites                       1.3.0
                attrs                              19.1.0
                Babel                              2.6.0
                backcall                           0.1.0
                (base) D:\Anaconda3>
            4.2,查看过时的库
                命令：pip list --outdated
    方式二、  
         如果是从python 的解释器   Anaconda Prompt  里面查看，可以使用如下命令(python 3.x)   
            import sys
            print(sys.path) 
            
         启动python，检查已安装版本
            安装完成后最好确认一下你的python环境是不是能正常工作。
            下面是检测环境用的脚本。其中import我们用到的每个库，并输出版本号。
            打开命令行，启动python解释器
                Python
            我推荐直接在解释器里（Anaconda Prompt）输入下面脚本，或者自己写好版本然后在命令行运行，而不是在一个大的编辑器或者IDE里运行。尽量让事情简单化，确保注意力关注在机器学习上而不是各种工具链上。
            脚本如下：
                # Checkthe versions of libraries
                #Python version
                import sys
                print('Python: {}'.format(sys.version))
                # scipy
                import scipy
                print('scipy: {}'.format(scipy.__version__))
                # numpy
                import numpy
                print('numpy: {}'.format(numpy.__version__))
                #matplotlib
                import matplotlib
                print('matplotlib: {}'.format(matplotlib.__version__))
                #pandas
                import pandas
                print('pandas: {}'.format(pandas.__version__))
                #scikit-learn
                import sklearn
                print('sklearn: {}'.format(sklearn.__version__))
    
    python 标准库位置： %python安装路径%\Lib
        example:   D:\Anaconda3\Lib
    第三方库位置： %python安装路径%\Lib\site-packages
        example:   D:\Anaconda3\Lib\site-packages 
    
# python开发工具IDE(编辑器)
    一、
        Jupyter Notebook
            这是Anaconda自带的python编辑器，非常好用，也是这里推荐的IDE。
            
            Jupyter Notebook作图教程
                url:
                    https://baijiahao.baidu.com/s?id=1621998768410766469&wfr=spider&for=pc
            python IDE之jupyter notebook详细教程讲解
                url
                    https://baijiahao.baidu.com/s?id=1606393150485328586&wfr=spider&for=pc
    二、
        Intellij Idea       
            是JetBrains的Intellij Idea，它不仅仅是java的IDE，还是当今世界大部分主流高级语言的IDE。
                详细设置方法请移步如何用Intellij Idea搭建pythonIDE
                    url https://blog.csdn.net/qq_38188725/article/details/80623710
    三、
        PyCharm
            PyCharm是一种Python IDE，带有一整套可以帮助用户在使用Python语言开发时提高其效率的工具，
                比如调试、语法高亮、Project管理、代码跳转、智能提示、自动完成、单元测试、版本控制。此外，
                该IDE提供了一些高级功能，以用于支持Django框架下的专业Web开发。
# 5个超级好用的Python开发工具，小白迅速成长的神技！  
    url
        http://baijiahao.baidu.com/s?id=1600617302423168648&wfr=spider&for=pc
        
    工具一 Anaconda
    工具二 Skulpt
    工具三 Python Tutor
    工具四 IPython
    工具五 Jupyter Notebook