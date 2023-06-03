&emsp;
# np.around / round
- 函数返回指定数字的四舍五入值
```python
numpy.around(a,decimals)
```
参数说明：

- a: 数组
- decimals: 舍入的小数位数。 默认值为0, 保留原数据。 
>示例

```python
import numpy as np
 
a = np.array([1.0, 5.55, 123, 0.567, 25.532])  
print  ('原数组：')
print (a)
print ('舍入后：')
print (np.around(a))
print (np.around(a, decimals = 1))
print (np.around(a, decimals = 2))
```


&emsp;
# np.floor
- numpy.floor() 向下取整。

>示例
```python
import numpy as np
 
a = np.array([-1.7,  1.5,  -0.2,  0.6,  10])
print ('提供的数组：')
print (a)
print ('修改后的数组：')
print (np.floor(a))
```

&emsp;
# np.ceil
- numpy.ceil() 向上取整。

>示例
```python
import numpy as np
 
a = np.array([-1.7,  1.5,  -0.2,  0.6,  10])  
print  ('提供的数组：')
print (a)
print ('修改后的数组：')
print (np.ceil(a))
```