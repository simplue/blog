### 配置文件
[pip / User Guide / Config File](https://pip.pypa.io/en/stable/user_guide/#config-file)
> Per-user:
>
> On Unix the default configuration file is: $HOME/.config/pip/pip.conf which respects the XDG_CONFIG_HOME environment variable.
On macOS the configuration file is $HOME/Library/Application Support/pip/pip.conf if directory $HOME/Library/Application Support/pip exists else $HOME/.config/pip/pip.conf.
On Windows the configuration file is %APPDATA%\pip\pip.ini.
There are also a legacy per-user configuration file which is also respected, these are located at:
>
> On Unix and macOS the configuration file is: $HOME/.pip/pip.conf
On Windows the configuration file is: %HOME%\pip\pip.ini
You can set a custom path location for this config file using the environment variable PIP_CONFIG_FILE.
>
> On Unix the default configuration file is: $HOME/.config/pip/pip.conf which respects the XDG_CONFIG_HOME environment variable.
On macOS the configuration file is $HOME/Library/Application Support/pip/pip.conf.
On Windows the configuration file is %APPDATA%\pip\pip.ini.


### 配置
```
[global]
timeout = 30

index-url = https://mirrors.aliyun.com/pypi/simple/

[install]
extra-index-url =
    https://mirrors.ustc.edu.cn/pypi/web/simple/
    https://pypi.doubanio.com/simple/
    https://pypi.shuosc.org/simple/
    https://pypi.tuna.tsinghua.edu.cn/simple/
    https://mirrors.163.com/pypi/simple/
    https://pypi.pubyun.com/simple/
    https://pypi.python.org/simple/

[list]
format = freeze
```
https://www.cnblogs.com/kimyeee/p/7250560.html
https://github.com/pypa/pipenv

[pypi官方](https://pypi.org/)

[pip文档 install options](https://pip.pypa.io/en/stable/reference/pip_install/#options)

[pip文档 install examples](https://pip.pypa.io/en/stable/reference/pip_install/#examples)

[非官方 Windows 二进制安装包](https://www.lfd.uci.edu/~gohlke/pythonlibs/)（由加州大学欧文分校荧光动力学实验室维护）
