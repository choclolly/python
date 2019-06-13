# scipy的积累和anaconda的一些安装、环境配置知识
    url:
        https://blog.csdn.net/zouzou0301/article/details/81096766
        
    1.
        SciPy函数库在NumPy库的基础上增加了众多的数学、科学以及工程计算中常用的库函数。
            例如：线性代数、常微分方程数值求解、信号处理、图像处理、稀疏矩阵等等。
    2.
        Scipy库是基于python生态的一款开源数值计算，科学与工程应用的开源软件，包括常用的NumPy，pandas，matplotlib等库。
    3.
        SciPy是一款方便、易于使用、专为科学和工程设计的Python工具包。它包括统计,优化,整合,线性代数模块,傅里叶变换,信号和图像处理,常微分方程求解器等等。
    
        SciPy科学计算工具集，而不是完整的包含NumPy、Matplotlib的SciPy技术栈。
            Scipy库构建于NumPy之上，提供了一个用于在Python中进行科学计算的工具集，如数值计算的算法和一些功能函数，可以方便的处理数据。主要包含以下内容
               
                特殊函数 (scipy.special)
                积分 (scipy.integrate)
                最优化 (scipy.optimize)
                插值 (scipy.interpolate)
                傅立叶变换 (scipy.fftpack)
                信号处理 (scipy.signal)
                线性代数 (scipy.linalg)
                稀疏特征值 (scipy.sparse)
                统计 (scipy.stats)
                多维图像处理 (scipy.ndimage)
                文件 IO (scipy.io)
                
                 url：
                    https://scipy.org/
                
    4.用conda list 或者 pip list可以查看已安装的库，看有没有matplotlib/ jupyter/ notebook/ numpy/ scipy/ scikit-learn等包
    5.no module named ‘scipy’问题解决方法 
        解决方法一： 
        打开Anaconda Prompt，输入命令： 
        conda install scipy 
        解决方法二： 
        如果上述方法提示PackagesNotFoundError，那么就用pip安装，命令是： 
        pip install scipy
        
        注意！！！！如果在conda中创建了tensorflow，那么需要进入对应环境进行安装。以scipy为例，操作如下： 
        打开Anaconda Prompt 
        激活tensorflow：
            activate tensorflow 
        安装scipy： 
            conda install scipy
        
    6.查看pip版本
        打开Anaconda Prompt，
        输入命令： pip --version 
    7.
        Anaconda Navigator：
            管理工具包和环境的图形用户界面。
        Anaconda Prompt：
            终端，可以使用命令行来管理包和环境。
        Jupyter Notebook ：
            基于web的交互式计算环境，可以编辑易于人们阅读的文档，用于展示数据分析的过程。
        Spyder：
            一个使用Python语言、跨平台、科学运算的集成开发环境。
    
    8.
        进入环境：
            activate env_name（如：tensorflow ）
                example：activate tensorflow
    
        离开环境：
            deactivate
        列出环境：
            conda env list   
        删除环境：
            conda remove --name env_name --all
            其中，env_name 是环境的名称。
            example：
                删除环境 python36，在 Anaconda Prompt（终端）中输入： 
                    conda remove --name python36 --all
                也可以使用以下命令删除环境python36：  
                    conda env remove -n python36
        安装包
            conda install package_name
            package_name为包的名称
            
            example：
                要安装 numpy，在 Anaconda Prompt（终端）中输入：conda install numpy
        
        移除包
            conda remove package_name
            
            example：
                要移除 numpy，在 Anaconda Prompt（终端）中输入：conda remove numpy
        更新包
            conda update package_name
            要更新环境中的所有包，在 Anaconda Prompt（终端）中输入：
                conda update --all
            也可以指定环境更新包，可以输入以下命令更新 numpy
                conda update -n python36 numpy
        查询包的信息
            conda search package_name
            
            example：
                下面是查询包 numpy 的信息
                    conda search numpy
        --------------------- 
        作者：zouzou0301 
        来源：CSDN 
        原文：https://blog.csdn.net/zouzou0301/article/details/81096766 
        版权声明：本文为博主原创文章，转载请附上博文链接！
    --------------------- 
    作者：zouzou0301 
    来源：CSDN 
    原文：https://blog.csdn.net/zouzou0301/article/details/81096766 
    版权声明：本文为博主原创文章，转载请附上博文链接！                       