# ai-webapi

## 项目介绍：

fastapi的工程模版，web api接口接收请求

## 一些遇到的问题：

**async关键字:** Python语言中的一个关键字，意在声明一个函数为“异步”。

> 参考
>
> https://blog.csdn.net/Franciz777/article/details/129193928

**environs库：**帮助用户轻松自定义各种类型的环境变量。

> 参考：
>
> https://cuiqingcai.com/8947.html

**logging库：**定义日志。

> 参考：
>
> https://zhuanlan.zhihu.com/p/445411809

在自定义日志时，主要关注到日志级别、日志保存路径、日志名称、日志格式。

代码使用注释：

> 代码路径：AI-WEIBAPI/common/logger.py/line:19-37
>
> 另外，logging.handlers可自定义日志处理器。一个是`TimedRotatingFileHandler`，一个是`StreamHandler`。每个处理器都定义了日志消息如何处理和存储。
>
> 1. `TimedRotatingFileHandler`是用于将日志消息写入到磁盘文件，并且会根据一定的时间间隔自动创建新的日志文件。新的日志文件每天午夜创建(`when='MIDNIGHT'`)，每次创建新的日志文件都会保留最近的30个旧文件 (`backupCount=30`)。
>    - `f_handler.suffix = '%Y-%m-%d.log'` 定义了旧日志文件的日期格式后缀，这里指定为'年-月-日.log'格式。
>    - `f_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}.log$")` 为这些旧日志文件设置一个匹配日期格式后缀的正则表达式。
>    - `f_handler.setFormatter(logging.Formatter(format))` 设置了日志文件的格式。
>    - `logger.addHandler(f_handler)` 将此处理器添加到 logger 上。
> 2. `StreamHandler`将日志消息输出到sys.stderr, sys.stdout 或者类文件对象。默认情况下，`StreamHandler`向控制台输出日志信息。
>    - `c_handler.setLevel(config['log']['level'])` 设置这个处理器的日志级别。
>    - `c_handler.setFormatter(logging.Formatter(format))` 设置控制台输出的日志格式。
>    - `logger.addHandler(c_handler)` 将此处理器添加到 logger 上。
>
> 这样的配置同时让程序的日志信息输出到控制台并写入到日志文件中，并且每天都会创建一个新的日志文件，最多保留 30 个旧日志文件。

**构造函数：__new__**：与`__init__`不同的地方在于，`__new__`才是构造函数。当我们创建一个实例的时候，实际上是**先调用的`__new__`函数创建实例，然后再调用`__init__`对实例进行的初始化**。

> 参考：
>
> https://mp.weixin.qq.com/s?__biz=Mzg5NTYyMDgyNg==&mid=2247489147&idx=1&sn=ebfcc0c8ddde7345cc79b224934d02f8&source=41#wechat_redirect
>
> 个人理解：
>
> `__new__` 用于创建（分配内存）一个新实例，`__init__` 用于初始化（赋初值）这个新实例。



**元类type：**元类是类的类，换句话说，元类的实例是类。Python当中的每一个类都是type的实例。

> 参考：
>
> https://zhuanlan.zhihu.com/p/149126959
>
> 其他：
>
> 在重写`__new__`函数时关注四个参数：
>
> ```python
> class AddInfo(type):
>     def __new__(cls, name, bases, attr):
>         attr['info'] = 'add by metaclass'
>         return super().__new__(cls, name, bases, attr)
>     
> ...
> cls：这个参数表示元类本身。
> 
> name：这个参数是准备创建的类的名字，这个名字是一个字符串。
> 
> bases：是准备创建的类的父类集合。这是一个元组，其中包含了所有的父类。
> 
> attr：这个字典包含了类的属性和方法。键是属性或方法的名字，值是属性的值或方法对象。
> 
> Metaclass.__new__ 的 task 是通过这四个参数创建并返回一个新的类（它是一个真正的类，是 type 的实例）。
> ...
> ```
>
> 
>
> 