&emsp;
# Matplotlib 柱形图
- 我们可以使用 pyplot 中的 bar() 方法来绘制柱形图

>语法
```python
matplotlib.pyplot.bar(x, height, width=0.8, bottom=None, *, align='center', data=None, **kwargs)
```
>参数

- x：浮点型数组，柱形图的 x 轴数据
- height：浮点型数组，柱形图的高度
- width：浮点型数组，柱形图的宽度
- bottom：浮点型数组，底座的 y 坐标，默认 0
- align：柱形图与 x 坐标的对齐方式，'center' 以 x 位置为中心，这是默认值。 'edge'：将柱形图的左边缘与 x 位置对齐。要对齐右边缘的条形，可以传递负数的宽度值及 align='edge'
- **kwargs：：其他参数

>示例 1
```python 
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Test-1", "Test-2", "Test-3", "C-TEST"])
y = np.array([12, 22, 6, 18])

plt.bar(x,y)
plt.savefig("./imgs/test27.jpg")
```
显示结果如下：
<div align=center>
    <image src='imgs/test27.jpg' width=400>
</div>


>示例 2：使用 barh() 方法来画垂直方向的柱形图
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Test-1", "Test-2", "Test-3", "C-TEST"])
y = np.array([12, 22, 6, 18])

plt.barh(x,y)
plt.savefig("./imgs/test28.jpg")
```
显示结果如下：
<div align=center>
    <image src='imgs/test28.jpg' width=400>
</div>



>示例 3：设置柱形图颜色：
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Test-1", "Test-2", "Test-3", "C-TEST"])
y = np.array([12, 22, 6, 18])

plt.bar(x, y, color = "#4CAF50")
plt.savefig("./imgs/test29.jpg")
```
显示结果如下：
<div align=center>
    <image src='imgs/test29.jpg' width=400>
</div>



>示例 3：自定义各个柱形的颜色
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Test-1", "Test-2", "Test-3", "C-TEST"])
y = np.array([12, 22, 6, 18])

plt.bar(x, y,  color = ["#4CAF50","red","hotpink","#556B2F"])
plt.savefig("./imgs/test30.jpg")
```
显示结果如下：
<div align=center>
    <image src='imgs/test30.jpg' width=400>
</div>



>示例 4：设置柱形图宽度，bar() 方法使用 width 设置，barh() 方法使用 height 设置 height
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Test-1", "Test-2", "Test-3", "C-TEST"])
y = np.array([12, 22, 6, 18])

plt.bar(x, y, width = 0.1)
plt.savefig("./imgs/test31.jpg")
```
显示结果如下：
<div align=center>
    <image src='imgs/test31.jpg' width=400>
</div>


>示例 5：
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Test-1", "Test-2", "Test-3", "C-TEST"])
y = np.array([12, 22, 6, 18])

plt.barh(x, y, height = 0.1)
plt.savefig("./imgs/test32.jpg")
```
显示结果如下：
<div align=center>
    <image src='imgs/test32.jpg' width=400>
</div>
