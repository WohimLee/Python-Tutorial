&emsp;
# np.mean

- numpy.mean() 函数返回数组中元素的算术平均值。 如果提供了轴，则沿其计算
- 算术平均值是沿轴的元素的总和除以元素的数量

```python
import numpy as np 
 
a = np.arange(24).reshape(3, 2, 4)
print('我们的数组是：')
print(a)
print('调用 mean() 函数：')
print(np.mean(a)) 
print('沿轴 0 调用 mean() 函数：')
print(np.mean(a, axis =  0)) # shape (2, 4)
print('沿轴 1 调用 mean() 函数：')
print(np.mean(a, axis =  1)) # shape (3, 4)
```

&emsp;
# np.average
- numpy.average() 函数根据在另一个数组中给出的各自的权重计算数组中元素的加权平均值
- 该函数可以接受一个轴参数。 如果没有指定轴，则数组会被展开
- 加权平均值即将各数值乘以相应的权数，然后加总求和得到总体值，再除以总的单位数

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
# np.sqrt
- 开平方

&emsp;
# np.var
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
# np.std
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

