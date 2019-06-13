# idea安装python sdk
    如果没有python sdk，那么就去安装python sdk
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
                                                    选择python命令路径    D:\Anaconda3\python.exe
                                                    勾选 make available to all projects
                OK
# idea创建python
    创建python项目
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
            or
            
            IntelliJ IDEA
                File
                    New
                        Module
                        项目类型中多了一个Python。点击它
                        Python
                            Module SDK：    Python 3.7
                        Next
                            Project name：    python-example
     
                        Finsh
# idea编辑python脚本
    python项目上右键
        New
            Python File
            magic.py
            
            注意：magic.py页面上提示错误：
                No Python interpreter configured for the module
            解决办法
                File
                    Project Structrue
                        Modules
                            python-example
                                Dependencies
                                    Module SDK: 选择pythonsdk即可
# idea运行python脚本
    在脚本上右键 Run 'main' or Debug 'main'
# 学习关卡 课程介绍
       课程介绍
       Course introduction
![](images\Course introduction.png)

# 学习大纲--learning syllabus
    人工智能Python入门
    	人工智能学习课程
    		DAY1
    			为你推开人工智能的大门
    				人工智能
    					AI 消灭重复性劳动
    					掌握人机合作工具--编程语言--Python--人机合作的入门选项
    		DAY2
    			Python：AI时代的必选项
    		DAY3 
    			Python能帮我们做什么
    		DAY4	
    			规划你的Python学习路径
    	Python电脑实操
    		https://www.pypypy.cn
    		0 pass
    		1 pass
    		2 pass
    		...
    python学习
![](learning syllabus/images\python study.png)