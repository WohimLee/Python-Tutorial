&emsp;
# Exercise

## Exercise 1: Bounding Box
<div align=center>
    <image src="./imgs/bbox.png" width=500>
</div>

```py
bbox1 = BBox(5, 2, 20, 12)
bbox2 = BBox(8, 7, 18, 27)
print(bbox1.height)
print(bbox1.width)
print(bbox1.area)

# 求相交的面积
cross = bbox1 & bbox2
# 求合并的面积
union = bbox1 | bbox2
# 求 IoU（cross/union）
iou = bbox1 ^ bbox2
```

&emsp;
## Exercise 2: Project
- 利用 Toolkit 实现梯度下降，求出 $w$ 和 $b$
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