# python神器——Anaconda的安装与优化配置
    url:
            https://blog.csdn.net/qq_38188725/article/details/80624004
        前言：
            对于初学者来说，原版的python在使用的时候非常麻烦，特别是在添加库、升级库的时候总是会报好多错误，缺这缺那。但是自从有了Anaconda以后，妈妈再也不用担心我用不了python啦！
            Anaconda相当于一个python的整合包，是一个开源的python发行版本，里面有各种科学包和依赖项，使用起来非常简单。
        一、安装：
            1,安装非常简单。进入Anaconda网站https://www.anaconda.com/点击Download。选择你需要的配置进行下载，
![](learning syllabus/images\download anaconda.png)
    
![](learning syllabus/images\download anaconda2.png)
            
            2,完成下载之后，双击下载文件，启动安装程序。然后依照提示一步一步安装就可以了
                注意：
                    如果在安装过程中遇到任何问题，那么暂时地关闭杀毒软件，并在安装程序完成之后再打开。
                    如果在安装时选择了“为所有用户安装”，则卸载Anaconda然后重新安装，只为“我这个用户”安装。
            3,选择“Next”。
![](learning syllabus/images\install Anaconda3_1.png)
    
            4,阅读许可证协议条款，然后勾选“I Agree”并进行下一步。
![](learning syllabus/images\install Anaconda3_2.png)
        
            5,除非是以管理员身份为所有用户安装，否则仅勾选“Just Me”并点击“Next”。
![](learning syllabus/images\install Anaconda3_3.png)
            
            6,在“Choose Install Location”界面中选择安装Anaconda的目标路径，然后点击“Next”。
                注意：
                    目标路径中不能含有空格，同时不能是“unicode”编码。
                    除非被要求以管理员权限安装，否则不要以管理员身份安装。
![](learning syllabus/images\install Anaconda3_4.png)
            
![](learning syllabus/images\install Anaconda3_4_2.png)
            
            7,在“Advanced Installation Options”中不要勾选“Add Anaconda to my PATH environment variable.”（“添加Anaconda至我的环境变量。”）。
                因为如果勾选，则将会影响其他程序的使用。
                如果使用Anaconda，则通过打开Anaconda Navigator或者在开始菜单中的“Anaconda Prompt”（类似macOS中的“终端”）中进行使用。
              除非你打算使用多个版本的Anaconda或者多个版本的Python，
              否则便勾选“Register Anaconda as my default Python 3.7”。
![](learning syllabus/images\install Anaconda3_5.png)
            
            8,然后点击“Install”开始安装。如果想要查看安装细节，则可以点击“Show Details”。
![](learning syllabus/images\install Anaconda3_6.png)
            
            9,Next
![](learning syllabus/images\install Anaconda3_7.png)
            
            10,进入“Thanks for installing Anaconda!”界面则意味着安装成功，点击“Finish”完成安装。
                注意：
                    如果你不想了解“Anaconda云”和“Anaconda支持”，则可以不勾选“Learn more about Anaconda Cloud”和“Learn more about Anaconda Support”。
![](learning syllabus/images\install Anaconda3_8.png)
    
            11,验证安装结果。可选以下任意方法：
                1,“开始 → Anaconda3（64-bit）→ Anaconda Navigator”，若可以成功启动Anaconda Navigator则说明安装成功。
                2,“开始 → Anaconda3（64-bit）→ 右键点击Anaconda Prompt → 以管理员身份运行”，
                    在Anaconda Prompt中输入conda list，可以查看已经安装的包名和版本号。若结果可以正常显示，则说明安装成功。
                    
                    或者
                        
                    在Anaconda Prompt中输入python，出现如下信息则表示安装成功。
                        (base) PS C:\Users\h_don> python
                        Python 3.7.3 (default, Mar 27 2019, 17:13:21) [MSC v.1915 64 bit (AMD64)] :: Anaconda, Inc. on win32
                        Type "help", "copyright", "credits" or "license" for more information.
                        >>>
                3,“开始 → cmd →中输入python，
                    3.1，
                        Microsoft Windows [版本 10.0.17763.475]
                        (c) 2018 Microsoft Corporation。保留所有权利。
                        
                        C:\Users\h_don>python
                        'python' 不是内部或外部命令，也不是可运行的程序
                        或批处理文件。
                        
                        C:\Users\h_don>
                        
                        'python' 不是内部或外部命令，也不是可运行的程序，需要配置anaconda环境变量
                            此电脑->右键选择属性->高级系统设置->环境变量->系统变量->path
                                Path
                                    D:\Anaconda3
                                    D:\Anaconda3\Scripts
                    3.2,出现如下信息则表示安装成功。
                            Microsoft Windows [版本 10.0.17763.475]
                            (c) 2018 Microsoft Corporation。保留所有权利。
                            
                            C:\Users\h_don>python
                            Python 3.7.3 (default, Mar 27 2019, 17:13:21) [MSC v.1915 64 bit (AMD64)] :: Anaconda, Inc. on win32
                            
                            Warning:
                            This Python interpreter is in a conda environment, but the environment has
                            not been activated.  Libraries may fail to load.  To activate this environment
                            please see https://conda.io/activation
                            
                            Type "help", "copyright", "credits" or "license" for more information.
                            >>>
                    3.3,出现如下信息则表示安装成功。
                        conda list  可以查看已经安装的包名和版本号。若结果可以正常显示，则说明安装成功
                            Microsoft Windows [版本 10.0.17763.504]
                            (c) 2018 Microsoft Corporation。保留所有权利。
                            
                            C:\Users\h_don>conda list
                            WARNING: The conda.compat module is deprecated and will be removed in a future release.
                            # packages in environment at D:\Anaconda3:
                            #
                            # Name                    Version                   Build  Channel
                            _ipyw_jlab_nb_ext_conf    0.1.0                    py37_0    defaults
                            alabaster                 0.7.12                   py37_0    defaults
                            anaconda                  2019.03                  py37_0    defaults
                            anaconda-client           1.7.2                    py37_0    defaults
                            anaconda-navigator        1.9.7                    py37_0    defaults
                            anaconda-project          0.8.2                    py37_0    defaults
                            asn1crypto                0.24.0                   py37_0    defaults
                            ...
                            C:\Users\h_don>
    
        这里可以使用命令行编写代码，也可以使用python原生的IDE编写，但是编辑的感觉都非常不好。
            在安装完Anaconda后会发现电脑里多出了一个叫做Jupyter Notebook的软件。这是Anaconda自带的python编辑器，非常好用，也是这里推荐的IDE。
            另一个推荐的IDE是JetBrains的Intellij Idea，它不仅仅是java的IDE，还是当今世界大部分主流高级语言的IDE。
                详细设置方法请移步如何用Intellij Idea搭建pythonIDE
                    url https://blog.csdn.net/qq_38188725/article/details/80623710
        二、测试是否安装正确
            
            1，下载安装   
            2，
                1.1,在cmd命令下输入conda info看到如下图表示你已安装成功！
                    C:\Users\h_don>conda info

                     active environment : None
                       user config file : C:\Users\h_don\.condarc
                 populated config files : C:\Users\h_don\.condarc
                          conda version : 4.6.11
                    conda-build version : 3.17.8
                         python version : 3.7.3.final.0
                       base environment : D:\Anaconda3  (writable)
                           channel URLs : http://mirrors.aliyun.com/pypi/simple/win-64
                                          http://mirrors.aliyun.com/pypi/simple/noarch
                                          http://pypi.douban.com/simple/win-64
                                          http://pypi.douban.com/simple/noarch
                                          https://pypi.tuna.tsinghua.edu.cn/simple/win-64
                                          https://pypi.tuna.tsinghua.edu.cn/simple/noarch
                                          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/win-64
                                          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/noarch
                                          https://repo.anaconda.com/pkgs/main/win-64
                                          https://repo.anaconda.com/pkgs/main/noarch
                                          https://repo.anaconda.com/pkgs/free/win-64
                                          https://repo.anaconda.com/pkgs/free/noarch
                                          https://repo.anaconda.com/pkgs/r/win-64
                                          https://repo.anaconda.com/pkgs/r/noarch
                                          https://repo.anaconda.com/pkgs/msys2/win-64
                                          https://repo.anaconda.com/pkgs/msys2/noarch
                          package cache : D:\Anaconda3\pkgs
                                          C:\Users\h_don\.conda\pkgs
                                          C:\Users\h_don\AppData\Local\conda\conda\pkgs
                       envs directories : D:\Anaconda3\envs
                                          C:\Users\h_don\.conda\envs
                                          C:\Users\h_don\AppData\Local\conda\conda\envs
                               platform : win-64
                             user-agent : conda/4.6.11 requests/2.21.0 CPython/3.7.3 Windows/10 Windows/10.0.17763
                          administrator : False
                             netrc file : None
                           offline mode : False
                
                
                C:\Users\h_don>
            or
                1.2，
                    PS D:\Anaconda3\Scripts> conda info

                     active environment : None
                       user config file : C:\Users\h_don\.condarc
                 populated config files : C:\Users\h_don\.condarc
                          conda version : 4.6.11
                    conda-build version : 3.17.8
                         python version : 3.7.3.final.0
                       base environment : D:\Anaconda3  (writable)
                           channel URLs : http://mirrors.aliyun.com/pypi/simple/win-64
                                          http://mirrors.aliyun.com/pypi/simple/noarch
                                          http://pypi.douban.com/simple/win-64
                                          http://pypi.douban.com/simple/noarch
                                          https://pypi.tuna.tsinghua.edu.cn/simple/win-64
                                          https://pypi.tuna.tsinghua.edu.cn/simple/noarch
                                          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/win-64
                                          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/noarch
                                          https://repo.anaconda.com/pkgs/main/win-64
                                          https://repo.anaconda.com/pkgs/main/noarch
                                          https://repo.anaconda.com/pkgs/free/win-64
                                          https://repo.anaconda.com/pkgs/free/noarch
                                          https://repo.anaconda.com/pkgs/r/win-64
                                          https://repo.anaconda.com/pkgs/r/noarch
                                          https://repo.anaconda.com/pkgs/msys2/win-64
                                          https://repo.anaconda.com/pkgs/msys2/noarch
                          package cache : D:\Anaconda3\pkgs
                                          C:\Users\h_don\.conda\pkgs
                                          C:\Users\h_don\AppData\Local\conda\conda\pkgs
                       envs directories : D:\Anaconda3\envs
                                          C:\Users\h_don\.conda\envs
                                          C:\Users\h_don\AppData\Local\conda\conda\envs
                               platform : win-64
                             user-agent : conda/4.6.11 requests/2.21.0 CPython/3.7.3 Windows/10 Windows/10.0.17763
                          administrator : False
                             netrc file : None
                           offline mode : False
                
                PS D:\Anaconda3\Scripts>
            
                注：
                    如果提示conda不是内容命令，说明您在安装时未勾选配置环境变量的选项。接下来手动配置系统环境变量
            3，环境变量配置
                将以下路径添加到系统环境变量中
                D:\Anaconda3\Anaconda3;
                D:\Anaconda3\Anaconda3\Scripts;
                D:\Anaconda3\Library\mingw-w64\bin;
                D:\Anaconda3\Library\usr\bin;
                D:\Anaconda3\Library\bin;
            ...       
            
            参考资料
                url
                    https://www.jianshu.com/p/026a2c43b081   
        三、配置:
            pip是python的强大功能之一，有了它就可以为所欲为地在命令行中下载各种库。
                在Anaconda的安装目录下找到Scripts文件夹并进入D:\Anaconda3\Scripts，然后shift右键，选择在此处打开Powershell窗口，输入以下命令：
                    python -m pip install -U pip 或者 python -m pip install --upgrade pip
                    就可以将pip升级到最新版，然后就可以使用了。
                        PS D:\Anaconda3\Scripts> python -m pip install -U pip
                        pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.
                        Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.")': /simple/pip/
                        Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.")': /simple/pip/
                        Retrying (Retry(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.")': /simple/pip/
                        Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.")': /simple/pip/
                        Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.")': /simple/pip/
                        Could not fetch URL https://pypi.org/simple/pip/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/pip/ (Caused by SSLError("Can't connect to HTTPS URL because the SSL module is not available.")) - skipping
                        Requirement already up-to-date: pip in d:\anaconda3\lib\site-packages (19.0.3)
                        pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.
                        Could not fetch URL https://pypi.org/simple/pip/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/pip/ (Caused by SSLError("Can't connect to HTTPS URL because the SSL module is not available.")) - skipping
                        PS D:\Anaconda3\Scripts>
                    使用方法如下：
                        pip install numpy
                        稍等片刻即可安装成功。
                            PS D:\Anaconda3\Scripts> pip install numpy
                            pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.
                            Requirement already satisfied: numpy in d:\anaconda3\lib\site-packages (1.16.2)
                            pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.
                            Could not fetch URL https://pypi.org/simple/pip/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/pip/ (Caused by SSLError("Can't connect to HTTPS URL because the SSL module is not available.")) - skipping
                            PS D:\Anaconda3\Scripts>
                        有时下载特别慢，是因为Anaconda默认的镜像源在国外，非常不稳定。这里可以换成清华的镜像源，下载速度可以提升将近10倍。
                            首先建立配置文件：
                                windows下的路径为 C:\Users\你的用户名\pip\pip.ini
                                linux下的路径为 ~/.pip/pip.conf
                                内容为：
                                    [global]
                                    index-url = https://pypi.tuna.tsinghua.edu.cn/simple
                                    [install]
                                    trusted-host=pypi.tuna.tsinghua.edu.cn
                                然后在之前提到的Scripts下打开命令行窗口，输入如下命令：
                                    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
                                    conda config --set show_channel_urls yes 
                                镜像源的切换完成。检测方法是在命令行输入命令conda info，如下图：
![](learning syllabus/images\conda info.png)
    
                                    PS D:\Anaconda3\Scripts> conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
                                    PS D:\Anaconda3\Scripts> conda config --set show_channel_urls yes
                                    PS D:\Anaconda3\Scripts> conda info
                                    
                                         active environment : None
                                           user config file : C:\Users\h_don\.condarc
                                     populated config files : C:\Users\h_don\.condarc
                                              conda version : 4.6.11
                                        conda-build version : 3.17.8
                                             python version : 3.7.3.final.0
                                           base environment : D:\Anaconda3  (writable)
                                               channel URLs : https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/win-64
                                                              https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/noarch
                                                              https://repo.anaconda.com/pkgs/main/win-64
                                                              https://repo.anaconda.com/pkgs/main/noarch
                                                              https://repo.anaconda.com/pkgs/free/win-64
                                                              https://repo.anaconda.com/pkgs/free/noarch
                                                              https://repo.anaconda.com/pkgs/r/win-64
                                                              https://repo.anaconda.com/pkgs/r/noarch
                                                              https://repo.anaconda.com/pkgs/msys2/win-64
                                                              https://repo.anaconda.com/pkgs/msys2/noarch
                                              package cache : D:\Anaconda3\pkgs
                                                              C:\Users\h_don\.conda\pkgs
                                                              C:\Users\h_don\AppData\Local\conda\conda\pkgs
                                           envs directories : D:\Anaconda3\envs
                                                              C:\Users\h_don\.conda\envs
                                                              C:\Users\h_don\AppData\Local\conda\conda\envs
                                                   platform : win-64
                                                 user-agent : conda/4.6.11 requests/2.21.0 CPython/3.7.3 Windows/10 Windows/10.0.17763
                                              administrator : False
                                                 netrc file : None
                                               offline mode : False
                                    
                                    PS D:\Anaconda3\Scripts>
    
                                    可以看到镜像源已经指向清华。
                        至此，Anaconda的安装与配置完成，尽情享受python吧！
# Anaconda介绍、安装及使用教程
    url:
            https://www.jianshu.com/p/62f155eb6ac5
        〇、序
            Python是一种面向对象的解释型计算机程序设计语言，其使用，具有跨平台的特点，可以在Linux、macOS以及Windows系统中搭建环境并使用，
                其编写的代码在不同平台上运行时，几乎不需要做较大的改动，使用者无不受益于它的便捷性。
            此外，Python的强大之处在于它的应用领域范围之广，遍及人工智能、科学计算、Web开发、系统运维、大数据及云计算、金融、游戏开发等。
                实现其强大功能的前提，就是Python具有数量庞大且功能相对完善的标准库和第三方库。通过对库的引用，能够实现对不同领域业务的开发。
                然而，正是由于库的数量庞大，对于管理这些库以及对库作及时的维护成为既重要但复杂度又高的事情。
        一、什么是Anaconda
            1，简介
                Anaconda（官方网站）就是可以便捷获取包且对包能够进行管理，同时对环境可以统一管理的发行版本。Anaconda包含了conda、Python在内的超过180个科学包及其依赖项。
            2，特点
                Anaconda具有如下特点：
                    开源
                    安装过程简单
                    高性能使用Python和R语言
                    免费的社区支持
                
                其特点的实现主要基于Anaconda拥有的：
                
                    conda包
                    环境管理器
                    1,000+开源库
                
                如果日常工作或学习并不必要使用1,000多个库，那么可以考虑安装Miniconda（图形界面下载及命令行安装请戳），这里不过多介绍Miniconda的安装及使用。
            3，Anaconda、conda、pip、virtualenv的区别
                ① Anaconda
                    Anaconda是一个包含180+的科学包及其依赖项的发行版本。其包含的科学包包括：conda, numpy, scipy, ipython notebook等。
                ② conda
                    conda是包及其依赖项和环境的管理工具。
                    适用语言：Python, R, Ruby, Lua, Scala, Java, JavaScript, C/C++, FORTRAN。
                    适用平台：Windows, macOS, Linux
                    
                    用途：
                        快速安装、运行和升级包及其依赖项。
                        在计算机中便捷地创建、保存、加载和切换环境。
                        
                如果你需要的包要求不同版本的Python，你无需切换到不同的环境，因为conda同样是一个环境管理器。仅需要几条命令，
                    你可以创建一个完全独立的环境来运行不同的Python版本，同时继续在你常规的环境中使用你常用的Python版本。——conda官方网站
                
                    conda为Python项目而创造，但可适用于上述的多种语言。
                    conda包和环境管理器包含于Anaconda的所有版本当中。
                ③ pip
                    pip
                        是用于安装和管理软件包的包管理器。
                    pip编写语言：
                        Python。
                    Python中默认安装的版本：
                        Python 2.7.9及后续版本：默认安装，命令为pip
                        Python 3.4及后续版本：默认安装，命令为pip3
                    pip名称的由来：pip采用的是递归缩写进行命名的。其名字被普遍认为来源于2处：
                        “Pip installs Packages”（“pip安装包”）
                        “Pip installs Python”（“pip安装Python”）
                ④ virtualenv
                    virtualenv：用于创建一个独立的Python环境的工具。
                    解决问题：
                        当一个程序需要使用Python 2.7版本，而另一个程序需要使用Python 3.6版本，如何同时使用这两个程序？
                        如果将所有程序都安装在系统下的默认路径，如：/usr/lib/python2.7/site-packages，当不小心升级了本不该升级的程序时，将会对其他的程序造成影响。
                        如果想要安装程序并在程序运行时对其库或库的版本进行修改，都会导致程序的中断。
                        在共享主机时，无法在全局site-packages目录中安装包。
                    virtualenv将会为它自己的安装目录创建一个环境，这并不与其他virtualenv环境共享库；同时也可以选择性地不连接已安装的全局库。
                ⑤ pip 与 conda 比较
                    → 依赖项检查
                        pip：
                            不一定会展示所需其他依赖包。
                            安装包时或许会直接忽略依赖项而安装，仅在结果中提示错误。
                        conda：
                            列出所需其他依赖包。
                            安装包时自动安装其依赖项。
                            可以便捷地在包的不同版本中自由切换。
                    → 环境管理
                        pip：维护多个环境难度较大。
                        conda：比较方便地在不同环境之间进行切换，环境管理较为简单。
                    → 对系统自带Python的影响
                        pip：在系统自带Python中包的**更新/回退版本/卸载将影响其他程序。
                        conda：不会影响系统自带Python。
                    → 适用语言
                        pip：仅适用于Python。
                        conda：适用于Python, R, Ruby, Lua, Scala, Java, JavaScript, C/C++, FORTRAN。
                ⑥ conda与pip、virtualenv的关系
                    conda结合了pip和virtualenv的功能。
        二、Anaconda的适用平台及安装条件
            1. 适用平台
                Anaconda可以在以下系统平台中安装和使用：
                    Windows
                    macOS
                    Linux（x86 / Power8）
            2. 安装条件
                系统要求：32位或64位系统均可
                下载文件大小：约500MB
                所需空间大小：3GB空间大小（Miniconda仅需400MB空间即可）
        三、Anaconda的安装步骤
            1. macOS系统安装Anaconda
            2. Windows系统安装Anaconda
            3. Linux系统安装Anaconda
        四、管理conda
            0. 写在前面
            1. 验证conda已被安装
            2. 更新conda至最新版本
            3. 查看conda帮助信息
            4. 卸载conda
        五、管理环境
            0. 写在前面
            1. 创建新环境
            2. 切换环境
            3. 退出环境至root
            4. 显示已创建环境
            5. 复制环境
            6. 删除环境
        六、管理包
            1. 查找可供安装的包版本
            2. 获取当前环境中已安装的包信息
            3. 安装包
            4. 卸载包
            5. 更新包
        七、参考资料
            知乎“初学python者自学anaconda的正确姿势是什么？？
                https://www.zhihu.com/question/58033789/answer/254673663?utm_source=wechat_session&utm_medium=social
            Anaconda Cheat Sheet
                        \          SORRY            /
                         \                         /
                          \    This page does     /
                           ]   not exist yet.    [    ,'|
                           ]                     [   /  |
                           ]___               ___[ ,'   |
                           ]  ]\             /[  [ |:   |
                           ]  ] \           / [  [ |:   |
                           ]  ]  ]         [  [  [ |:   |
                           ]  ]  ]__     __[  [  [ |:   |
                           ]  ]  ] ]\ _ /[ [  [  [ |:   |
                           ]  ]  ] ] (#) [ [  [  [ :===='
                           ]  ]  ]_].nHn.[_[  [  [
                           ]  ]  ]  HHHHH. [  [  [
                           ]  ] /   `HH("N  \ [  [
                           ]__]/     HHH  "  \[__[
                           ]         NNN         [
                           ]         N/"         [
                           ]         N H         [
                          /          N            \
                         /           q,            \
                        /                           \
            Anaconda官方网站
            conda官方网站
            pip官方网站
            pip维基百科
            virtualenv官方网站
            macOS系统安装Anaconda的官方教程
                http://docs.anaconda.com/anaconda/install/mac-os/#macos-graphical-install
            Windows系统安装Anaconda的官方教程
                http://docs.anaconda.com/anaconda/install/windows/
            Linux系统安装Anaconda的官方教程
                http://docs.anaconda.com/anaconda/install/linux/
            
            作者：Raxxie
            链接：https://www.jianshu.com/p/62f155eb6ac5
            来源：简书
            简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。
# Requirement already up-to-date: pip in d:\anaconda3\lib\site-packages (19.0.3)
# 验证pip.exe，查看它的版本号！输入pip -V
    CMD
        C:\Users\h_don>pip -V
        pip 19.0.3 from D:\Anaconda3\lib\site-packages\pip (python 3.7)
# python.exe和pythonw.exe的区别（区分.py、.pyw、.pyc文件）
    url
        https://blog.csdn.net/pythonw/article/details/74430328
    Windows系统搭建好Python的环境后，进入Python的安装目录，大家会发现目录中有python.exe和pythonw.exe两个程序
    它们到底有什么区别和联系呢？概括说明一下：
        python.exe在运行程序的时候，会弹出一个黑色的控制台窗口（也叫命令行窗口、DOS/CMD窗口）；
        pythonw.exe是无窗口的Python可执行程序，意思是在运行程序的时候，没有窗口，代码在后台执行
    .py和.pyw文件
        的区别也来源于python.exe和pythonw.exe的区别：
        安装视窗版 Python 时，扩展名为 .py 的文件被默认为用 python.exe 运行的文件，而 .pyw文件则被默认为用 pythonw.exe 运行。
    
        这里还要解释一个问题，如果.py文件直接用python.exe打开，文件被执行完成之后，视窗会立即关闭，如果想让视窗停留，给大家提供两个方法：
            ①可以在程序中import time模块，加入超长睡眠语句，如time.sleep(1800)，如果你不手动关闭视窗，视窗将会停留30min
            ②可以调用sys和os模块，使用命令行语句pause（个人觉得有些牛刀杀鸡的感觉）。
    .pyw
        格式是被设计用来运行开发的纯图形界面程序的，纯图形界面程序的用户不需要看到控制台窗口。在开发纯图形界面程序的时候，可以暂时把 .pyw 改成 .py ，运行时能调出控制台窗口，方便看到所有错误信息。
    
    .pyc
        至于.pyc文件，是Python解释器运行程序的过程中产生的字节码文件（也就是中间文件）。
        Python什么情况下产生pyc文件？
# Anaconda3：    pip install httplib2 报错
    参考资料
        使用Anaconda中的pip命令报错:pip is configured with locations that require TLS/SSL
            url
                https://blog.csdn.net/JerkSpan/article/details/86599690
    1,安装环境
        win10
    2,执行命令
        pip install httplib2
    3,问题详情
        PS D:\Anaconda3\Scripts> pip install httplib2
        pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.
        Collecting httplib2
          Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.")': /simple/httplib2/
          Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.")': /simple/httplib2/
          Retrying (Retry(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.")': /simple/httplib2/
          Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.")': /simple/httplib2/
          Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.")': /simple/httplib2/
          Could not fetch URL https://pypi.org/simple/httplib2/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/httplib2/ (Caused by SSLError("Can't connect to HTTPS URL because the SSL module is not available.")) - skipping
          Could not find a version that satisfies the requirement httplib2 (from versions: )
        No matching distribution found for httplib2
        pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.
        Could not fetch URL https://pypi.org/simple/pip/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/pip/ (Caused by SSLError("Can't connect to HTTPS URL because the SSL module is not available.")) - skipping
        PS D:\Anaconda3\Scripts>
    
        错误信息：
            1，
                pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.
            2，
                Could not fetch URL https://pypi.org/simple/httplib2/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): 
                    Max retries exceeded with url: /simple/httplib2/ (Caused by SSLError("Can't connect to HTTPS URL because the SSL module is not available.")) - skipping
                Could not find a version that satisfies the requirement httplib2 (from versions: )
            3，
                No matching distribution found for httplib2
                pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.
                Could not fetch URL https://pypi.org/simple/pip/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): 
                    Max retries exceeded with url: /simple/pip/ (Caused by SSLError("Can't connect to HTTPS URL because the SSL module is not available.")) - skipping
        
        CMD验证：发现找不到指定模块
            Microsoft Windows [版本 10.0.17763.504]
            (c) 2018 Microsoft Corporation。保留所有权利。
            
            C:\Users\h_don>python
            Python 3.7.3 (default, Mar 27 2019, 17:13:21) [MSC v.1915 64 bit (AMD64)] :: Anaconda, Inc. on win32
            
            Warning:
            This Python interpreter is in a conda environment, but the environment has
            not been activated.  Libraries may fail to load.  To activate this environment
            please see https://conda.io/activation
            
            Type "help", "copyright", "credits" or "license" for more information.
            >>> import _ssl
            Traceback (most recent call last):
              File "<stdin>", line 1, in <module>
            ImportError: DLL load failed: 找不到指定的模块。
    4,解决方案
        在网上搜索同类问题，大都是说python 的ssl模块未安装，从问题描述来看确实也很像，但是他们的问题大多发生在Linux上，而我的是Windows，
            又联想到Anaconda本来就是一个Python的套件包，包含了许多常用的工具和Python库，不可能犯这种低级错误，
            所以很可能是环境变量未配置全，导致pip无法找到ssl相关模块。
            
            最终参考之前正常的Anaconda的配置，将"[Anaconda安装目录]\Library\bin"加入PATH后，问题解决。
                path
                    D:\Anaconda3\Anaconda3;
                    D:\Anaconda3\Anaconda3\Scripts;
                    D:\Anaconda3\Library\bin;
                如下：
                    pip install httplib2 安装成功
                    
                    
                    Microsoft Windows [版本 10.0.17763.504]
                    (c) 2018 Microsoft Corporation。保留所有权利。
                    
                    C:\Users\h_don>pip install httplib2
                    Collecting httplib2
                      Downloading https://files.pythonhosted.org/packages/e8/b3/b34037575d6d75ff8dcfcf75315f56befbe409952be9f95c9b8cc9ee0499/httplib2-0.12.3-py3-none-any.whl (94kB)
                        100% |████████████████████████████████| 102kB 7.2kB/s
                    Installing collected packages: httplib2
                    Successfully installed httplib2-0.12.3
                    
                    C:\Users\h_don>
    完美解决