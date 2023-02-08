&emsp;
# 错误和异常

Python 有两种错误很容易辨认：语法错误和异常。


&emsp;
# 1 异常
运行期检测到的错误被称为异常。

大多数的异常都不会被程序处理，都以错误信息的形式展现出来

&emsp;
# 2 异常处理

&emsp;
## 2.1 try/except

>示例
```python
import os
def mkdirs(directory):
    try:
        os.makedirs(directory)
    except Exception as e:
        ...
```