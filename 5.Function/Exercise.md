&emsp;
# Exercise

## Exercise 1
>求均值、方差（母体方差）
$$\sigma^2 = \frac{\sum\limits^N_{i=1}(x_i - \mu)^2}{N}$$
- 输入:
    ```
    x = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]
    ```
- 输出: $\mu$、 $\sigma^2$


&emsp;
## Exercise 2

$$y=x\times w + b$$
- 参数：$w=0.5$、$b=1$
- 输入：x
- 输出：y


&emsp;
## Exercise 3
>MSE Loss
$$Loss = \frac{1}{n}\sum\limits^{N}_{i=1}(Y_{predict} - Y_{target})^2$$

- 输入：
    ```
    y_target  = [1.8, 2.1, 2.3, 2.3, 2.85, 3.0, 3.3, 4.9, 5.45, 5.0]
    y_predict = [-1.5666989, -1.2185436, -0.87038827, -0.52223295, -0.17407766,0.17407766, 0.52223295, 0.87038827, 1.2185436, 1.5666989]
    ```
- 输出：Loss

&emsp;
## Exercise 4
>梯度下降
- 函数 $f(x)$
$$f(x) = y = 3x^2 + 6x + 5 = 3(x+1)^2 + 2$$

<div align=center>
    <image src="imgs/function.png" width=400/>
</div>

- $f(x)$ 导数
$$f'(x) = 6x + 6$$

- 利用下面公式，不断更新 $x$ 并打印 $x$ 和 $y$ 的值观察
$$x = x - lr*gradient$$
- gradient 为在 $x$ 处的导数
- 参数：
  - x: 初始化值为 2
  - lr= 0.01
