
&emsp;
# np.asarray
```python
numpy.asarray(a, dtype = None, order = None)
```
参数说明：

- a	任意形式的输入参数，可以是: list, tuple, (list1, list2), (tup1, tup2), []，多维数组
- dtype: 数据类型，可选
- order: 可选，有"C"和"F"两个选项,分别代表，行优先和列优先，在计算机内存中的存储元素的顺序。

>示例
```python
import numpy as np 

# 示例1：将列表转换为 ndarray
x =  [[1,2,3], [4,5,6]] 
a = np.asarray(x)  
print (a)
'''输出结果为：
[1  2  3]'''

# 示例2：将元组转换为 ndarray:
x =  ((1,2,3), (4,5,6)) 
a = np.asarray(x)  
print (a)
'''输出结果为：
[1  2  3]'''

# 示例3：设置了 dtype 参数：
x =  [1,2,3] 
a = np.asarray(x, dtype=np.float32)  
print (a)
'''输出结果为：
[ 1.  2.  3.]'''
```
