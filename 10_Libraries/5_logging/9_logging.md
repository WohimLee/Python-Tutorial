&emsp;
# logging

官方文档：https://docs.python.org/3/library/logging.html

# 日志级别


级别|数值
:--|:--
CRITICAL|50
ERROR|40
WARNING|30
INFO|20
DEBUG|10
NOTSET|0



&emsp;
# 1 Logger 记录器对象
## class logging.Logger

- setLevel(level)：给记录器设置阈值为 level 

- info(msg, *args, **kwargs)：在此记录器上记录 INFO 级别的消息

- warning(msg, *args, **kwargs)：在此记录器上记录 WARNING 级别的消息

- error(msg, *args, **kwargs)：在此记录器上记录 ERROR 级别的消息

- critical(msg, *args, **kwargs)：在此记录器上记录 CRITICAL 级别的消息

- addHandler(hdlr)：将指定的处理器 hdlr 添加到此记录器。

```python
import logging

logger = logging.getLogger("Test") # logger.name = "Test"
logger.setLevel(logging.INFO) 
logger.info("aaaaaaaa") # 终端无输出
```


&emsp;
# 2 Handler 处理器对象
Source code: Lib/logging/handlers.py

## class logging.Handler

- setLevel(level)：给处理器设置阈值为 level 。
- setFormatter(fmt)：将此处理器的 Formatter 设置为 fmt。

&emsp;
## 2.1 StreamHandler
- 将日志信息输出到终端
```py
import logging

logger = logging.getLogger("Test") # logger.name = "Test"
logger.setLevel(logging.INFO)
s_handler = logging.StreamHandler()
logger.addHandler(s_handler)
logger.info("aaaaaaaa")
```

&emsp;
## 2.2 TimedRotatingFileHandler
跑了一个训练脚本，每天生成的日志文件都写在了一个文件中。但是日志信息不可能输出到单一的一个文件中。
原因有二：
- 日志文件越来越大会影响系统的性能。
- 日志文件格式不够清晰，比如我想看今天的日志，不太方便找到的今天的日志信息(即使对日志输出做了时间提示)

>TimedRotatingFileHandler原型
```py
class logging.handlers.TimedRotatingFileHandler(filename, 
    when='h', interval=1, backupCount=0, 
    encoding=None, delay=False, utc=False, 
    atTime=None, errors=None)
```

>参数
- filename：是输出日志的文件名称前缀

- when 参数

Value|Type of interval|If/how atTime is used
:--|:--|:--
'S'|Seconds|Ignored
'M'|Minutes|Ignored
'H'|Hours|Ignored
'D'|Days|Ignored
'W0'-'W6'|Weekday (0=Monday)|Used to compute initial rollover time
'midnight'|Roll over at midnight, if atTime not specified, else at time atTime|Used to compute initial rollover time

- interval：是间隔时间单位的个数，指等待多少个 when 的时间后 Logger 会自动重建新闻继续进行日志记录。
这里需要注意的一点是，如果创建的文件和已有文件存在重名的情况，则会对历史的文件进行覆盖操作，所以使用好 suffix 避免文件名称重复

- backupCount：保留日志的文件个数。
默认的参数是0，这种设置下是不会自动删除文件的。如果设置为 N（正整数），则会在创建新的日志文件时会检查日志文件个数是否到达 N，达到了的话就会从最先创建的开始删除，从而达到维持日志文件个数为 N 个的目标

- atTime：使用atTime作为过渡的时间点。如果atTime不是None，则它必须是datetime.time实例，该实例指定发生翻转的一天中的时间，对于将翻转设置为“在午夜”发生的情况或“在特定工作日”。请注意，在这些情况下，atTime值可有效地用于计算初始过渡，随后的过渡将通过正常间隔计算来计算。



>示例
```py
import logging
import datetime
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger("Test") # logger.name = "Test"
logger.setLevel(logging.INFO)
trf_handler = TimedRotatingFileHandler(filename="./logs/xxx.txt",
    when="midnight", 
    interval=1, 
    backupCount=7,
    atTime=datetime.time(0,0,0,0))
logger.addHandler(trf_handler)
logger.info("aaaaaaaa")
```


&emsp;
# 3 Fomatter 格式器对象
Formatter 负责将 LogRecord 转换为可由人或外部系统解释的字符串。基础的 Formatter 允许指定格式字符串。如果未提供任何值，则使用默认值 '%(message)s' ，它仅将消息包括在日志记录调用中。要在格式化输出中包含其他信息（如时间戳）

## class logging.Formatter(fmt=None, datefmt=None, style='%', validate=True)

属性名称|格式|描述
:--|:--|:--
asctime|%(asctime)s|表示 LogRecord 何时被创建的供人查看时间值。 默认形式为 '2003-07-08 16:49:45,896' （逗号之后的数字为时间的毫秒部分）。
created|%(created)f|LogRecord 被创建的时间（即 time.time() 的返回值）。
filename|%(filename)s|pathname 的文件名部分。
levelname|%(levelname)s|消息文本记录级别（'DEBUG'，'INFO'，'WARNING'，'ERROR'，'CRITICAL'）。
lineno|%(lineno)d|发出日志记录调用所在的源行号（如果可用）。
message|%(message)s|记入日志的消息，即 msg % args 的结果。 这是在发起调用 Formatter.format() 时设置的。
name|%(name)s|用于记录调用的日志记录器名称。
pathname|%(pathname)s|发出日志记录调用的源文件的完整路径名（如果可用）。

>示例
```py
import logging

logger = logging.getLogger("Test") # logger.name = "Test"
logger.setLevel(logging.INFO)
s_handler = logging.StreamHandler()
formatter = logging.Formatter('[%(levelname)s][%(filename)s:%(lineno)d][%(asctime)s]:%(message)s')
s_handler.setFormatter(formatter)
logger.addHandler(s_handler)
logger.info("aaaaaaaa")
```

&emsp;
# 4 封装运用

```python
import logging
import datetime
from logging.handlers import TimedRotatingFileHandler
from utils import mkparents

def build_default_logger():
    '''
    只作输出的logger
    '''
    logger = logging.getLogger("DefaultLogger")
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('[%(levelname)s][%(filename)s:%(lineno)d][%(asctime)s]: %(message)s')
    s_handler = logging.StreamHandler()
    s_handler.setFormatter(formatter)
    logger.addHandler(s_handler)
    return logger


# 单例模式
class SingleInstanceLogger:
    def __init__(self):
        self.logger = build_default_logger()

    def __getattr__(self, name):
        return getattr(self.logger, name)

_single_instance_logger = SingleInstanceLogger()

def build_logger(path):
    '''
    用于训练时记录日志，每天记录，保持一周7天的记录
    '''
    logger = logging.getLogger("NewLogger")
    logger.setLevel(logging.INFO)
    mkparents(path)

    trf_handler = logging.handlers.TimedRotatingFileHandler(path, when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
    formatter = logging.Formatter('[%(levelname)s][%(filename)s:%(lineno)d][%(asctime)s]: %(message)s')
    trf_handler.setFormatter(formatter)
    logger.addHandler(trf_handler)

    s_handler = logging.StreamHandler()
    s_handler.setFormatter(formatter)
    logger.addHandler(s_handler)
    return logger

# 训练时记录日志 
def setup_single_instance_logger(path):
    global _single_instance_logger
    _single_instance_logger.logger = build_logger(path)
```