

&emsp;
# np.arange
```python
numpy.arange(start, stop, step, dtype)
```
- 根据 start 与 stop 指定的范围以及 step 设定的步长，生成一个 ndarray。

参数说明：
- start	起始值，默认为0
- stop	终止值（不包含）
- step	步长，默认为1
- dtype	返回 ndarray 的数据类型，如果没有提供，则会使用输入数据的类型

>示例
```python
import numpy as np

# 示例1：生成 0 到 5 的数组:
x = np.arange(5)  
print (x)
'''输出结果如下：
[0  1  2  3  4]'''

# 示例2：设置返回类型位 float:
# 设置了 dtype
x = np.arange(5, dtype=np.float32)  
print (x)
'''输出结果如下：
[0.  1.  2.  3.  4.]'''

# 示例3：设置了起始值、终止值及步长：
x = np.arange(10,20,2)  
print (x)
'''输出结果如下：
[10  12  14  16  18]'''
```
