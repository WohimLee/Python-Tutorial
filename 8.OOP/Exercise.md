&emsp;
# Exercise

## Excercise 1: VOC Dataset

```py
root = ''
voc_dataset = VOCDataset(root)

print(voc_dataset.root)
print(voc_dataset)

print("Length of VOC dataset: ", len(voc_dataset))
index = 0
label, image = voc_dataset[index]
```

&emsp;
## Exercise 2: Bounding Box
<div align=center>
    <image src="./imgs/bbox.png" width=500>
</div>

```py
bbox1 = BBox(5, 2, 20, 12)
bbox2 = BBox(8, 7, 18, 27)
# 求相交的面积
cross = bbox1 & bbox2
# 求合并的面积
union = bbox1 | bbox2
# 求 IoU（cross/union）
iou = bbox1 ^ bbox2
```

&emsp;
## Exercise 3: Toolkit
### 类：Module
```
m = Module()
m.name
m.training
print(x)
m(x)
m.parameters()
```
- 子类： class DerivedClass(Module)
>Linear
$$y = x\times w + b$$
- $w$: weights，权重，用 np.random.randn 初始化
- $b$: bias，噪声，初始化值为 0
```py
linear = Linear()
linear.weights
linear.bias
output = linear(x)
gd = linear.backward()
```

>Sigmoid
$$sigmoid = \frac{1}{1+e^{-x}}$$
```py
sigmoid = Sigmoid()
output = sigmoid(x)
gd = sigmoid.backward()
```


>ReLU
$$ReLU = \begin{cases} 1，if\ x>0\\ 0，otherwise\end{cases}$$

```py
relu = ReLU()
output = relu(x)
gd = relu.backward()
```
>MSELoss
$$MSELoss = \frac{1}{2}(y_{predict} - y_{target})^2$$

```py
mse_loss = MSELoss()
output = mse_loss(y_predict, y_target)
gd = mse_loss.backward()
```



&emsp;
## Exercise 4: Project
- 利用 Exercise 3 实现梯度下降，求出 $w$ 和 $b$
- input: x=1
- label: y_target=0.7502601055951177


### 类：Parameter
```py
param = Parameter()
param.data
param.grad
param.zero_grad() # 梯度清零
```

### 类：Optimizer
- 子类：GD
```py
class GD(Optimizer)
optimizer = GD(params, lr)
optimizer.step()
```




Answer: $w=0.7$，$b=0.4$