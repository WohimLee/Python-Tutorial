&emsp;
# 1 NumPy 数学函数

## 1.1 三角函数
NumPy 提供了标准的三角函数：sin()、cos()、tan()。

>示例
```python
import numpy as np
 
a = np.array([0,30,45,60,90])
print ('不同角度的正弦值：')
# 通过乘 pi/180 转化为弧度  
print (np.sin(a*np.pi/180))
print ('\n')
print ('数组中角度的余弦值：')
print (np.cos(a*np.pi/180))
print ('\n')
print ('数组中角度的正切值：')
print (np.tan(a*np.pi/180))
```

&emsp;
## 1.2 舍入函数
### (1) numpy.around() 
- 函数返回指定数字的四舍五入值。
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
### (2) numpy.floor()
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
### (3) numpy.ceil()
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

&emsp;
# 2 NumPy 统计函数

&emsp;
## 2.1 numpy.mean()

- numpy.mean() 函数返回数组中元素的算术平均值。 如果提供了轴，则沿其计算。

- 算术平均值是沿轴的元素的总和除以元素的数量。

```python
import numpy as np 
 
a = np.arange(24).reshape(3, 2, 4)
print ('我们的数组是：')
print (a)
print ('调用 mean() 函数：')
print (np.mean(a)) 
print ('沿轴 0 调用 mean() 函数：')
print (np.mean(a, axis =  0)) # shape (2, 4)
print ('沿轴 1 调用 mean() 函数：')
print (np.mean(a, axis =  1)) # shape (3, 4)
```

&emsp;
# 2.2 numpy.average()
- numpy.average() 函数根据在另一个数组中给出的各自的权重计算数组中元素的加权平均值。

- 该函数可以接受一个轴参数。 如果没有指定轴，则数组会被展开。

- 加权平均值即将各数值乘以相应的权数，然后加总求和得到总体值，再除以总的单位数。

>示例
```python
import numpy as np 
# 考虑数组[1,2,3,4]和相应的权重[4,3,2,1]
# 通过将相应元素的乘积相加，并将和除以权重的和，来计算加权平均值。
# 加权平均值 = (1*4+2*3+3*2+4*1)/(4+3+2+1)

# 1. 不指定权重时相当于 mean 函数
a = np.array([1,2,3,4])  
print ('我们的数组是：')
print (a)
print ('调用 average() 函数：')
print (np.average(a))

# 2. 加权平均
wts = np.array([4,3,2,1])  
print ('再次调用 average() 函数：')
print (np.average(a, weights = wts))
# 如果 returned 参数设为 true，则返回权重的和  
print ('权重的和：')
print (np.average([1,2,3,4], weights = [4,3,2,1], returned = True))
```

&emsp;
# 3 方差
- 统计中的方差（样本方差）是每个样本值与全体样本值的平均数之差的平方值的平均数，即 mean((x - x.mean())** 2)。

- 换句话说，标准差是方差的平方根。

>示例
```python
import numpy as np
 
print (np.var([1,2,3,4]))
输出结果为：

1.25
```



&emsp;
# 4 标准差
- 标准差是一组数据平均值分散程度的一种度量。

- 标准差是方差的算术平方根。

>标准差公式如下：
```
std = sqrt(mean((x - x.mean())**2))
```

>示例
```python
import numpy as np 
# 如果数组是 [1，2，3，4]，则其平均值为 2.5。 
# 因此，差的平方是 [2.25,0.25,0.25,2.25]，并且再求其平均值的平方根除以 4，即 sqrt(5/4) 
# 结果为 1.1180339887498949。

print (np.std([1,2,3,4]))
'''输出结果为：
1.1180339887498949'''
```

