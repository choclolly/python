# ModuleNotFoundError: No module named 'pip'
    0
        参考资料
            https://blog.csdn.net/haihonga/article/details/100168691
    1,
        错误
            C:\Users\h_don>pip --version
            Traceback (most recent call last):
              File "d:\python\python38-32\lib\runpy.py", line 194, in _run_module_as_main
                return _run_code(code, main_globals, None,
              File "d:\python\python38-32\lib\runpy.py", line 87, in _run_code
                exec(code, run_globals)
              File "D:\Python\Python38-32\Scripts\pip.exe\__main__.py", line 4, in <module>
            ModuleNotFoundError: No module named 'pip'
        解决
            C:\Users\h_don>pip --version
            Traceback (most recent call last):
              File "d:\python\python38-32\lib\runpy.py", line 194, in _run_module_as_main
                return _run_code(code, main_globals, None,
              File "d:\python\python38-32\lib\runpy.py", line 87, in _run_code
                exec(code, run_globals)
              File "D:\Python\Python38-32\Scripts\pip.exe\__main__.py", line 4, in <module>
            ModuleNotFoundError: No module named 'pip'
            
            C:\Users\h_don>python -m ensurepip
            Looking in links: c:\Users\h_don\AppData\Local\Temp\tmpq3q3jk8v
            Requirement already satisfied: setuptools in d:\python\python38-32\lib\site-packages (47.1.0)
            Processing c:\users\h_don\appdata\local\temp\tmpq3q3jk8v\pip-20.1.1-py2.py3-none-any.whl
            Installing collected packages: pip
            Successfully installed pip-20.1.1
            
            C:\Users\h_don>python -m pip install --upgrade pip
            Collecting pip
              Using cached pip-20.2-py2.py3-none-any.whl (1.5 MB)
            Installing collected packages: pip
              Attempting uninstall: pip
                Found existing installation: pip 20.1.1
                Uninstalling pip-20.1.1:
                  Successfully uninstalled pip-20.1.1
            Successfully installed pip-20.2
            
            C:\Users\h_don>pip --version
            pip 20.2 from d:\python\python38-32\lib\site-packages\pip (python 3.8)
            
            C:\Users\h_don>
    2,
        pip升级
            python -m pip install --upgrade pip