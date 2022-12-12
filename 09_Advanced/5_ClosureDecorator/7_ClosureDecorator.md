python 闭包，装饰器

&emsp;
# 1 闭包
如果在一个函数的内部定义了另一个函数，外部的函数叫它外函数，内部的函数叫它内函数。

&emsp;
## 1.1 闭包条件
- 在一个外函数中定义了一个内函数。
- 内函数里运用了外函数的临时变量。
- 并且外函数的返回值是内函数的引用。

一般情况下，如果一个函数结束，函数的内部所有东西都会释放掉，还给内存，局部变量都会消失。但是闭包是一种特殊情况，如果外函数在结束的时候发现有自己的临时变量将来会在内部函数中用到，就把这个临时变量绑定给了内部函数，然后自己再结束。

>示例
```python
# outer是外部函数 a和b都是外函数的临时变量
def outer(a):
        b = 10
        def inner():
                print(a+b)
        return inner

if __name__ == '__main__':
        test = outer(5) # 这里相当于 test = inner
        test()          # 相当于 inner()，里面的 a b 保存了下来，输出结果是 15
```

&emsp;
## 1.2 闭包用途
装饰器！

装饰器是做什么的？其中一个应用就是，我们工作中写了一个功能，我们想统计这个功能执行花了多长时间，我们可以用装饰器装饰这个登录模块，装饰器帮我们完成登录函数执行之前和之后取时间。



&emsp;
# 2 装饰器
&emsp;
## 2.1 装饰器的使用
>示例1：统计时间装饰器
```python
import time
def showtime(func):
    def wrapper():
        start = time.time()
        func()
        end   = time.time()
        print(f'time cost {end - start}')
    return wrapper

# 第一种使用方法
def func1():
    print("func1...")
    time.sleep(3)

test = showtime(func1)
test()

# 第二种使用方法, 用 @
@showtime
def func2():
    print("func2...")
    time.sleep(2)
func2()
```


>示例2：被装饰的函数有参数
```python
import time
def showtime(func):
    def wrapper(a, b):
        start = time.time()
        func(a, b)
        end   = time.time()
        print(f'time cost {end - start}')
    return wrapper

@showtime
def func(a, b):
    print(a+b)
    time.sleep(1)

func(1, 2)
```
&emsp;
## 2.2 常用的内置装饰器:

&emsp;
## (1) staticmethod
- 不用传入self参数
- 调用：只能使用 类名.方法或属性 的方式调用
>说明

- 静态方法，就像一个在类里面的普通函数，没有self(代表对象自身)参数。
```python
class A:
    def func1(self, a, b):
        print(a + b)

    @staticmethod
    def func2(a, b):
        print(a + b)

    def func3(a, b): # 这里 a 被当成了 self
        print(a + b)

a = A()
a.func1(1, 2)
a.func2(1, 2)
# a.func3(1) # a 被当成了 self，实例对象就不能用这个函数了
print("------------------")
A.func1(None, 1, 2)
A.func2(1, 2)
A.func3(1, 2)
```

&emsp;
## (2) classmethod
- 至少有一个参数cls(代表类本身)，cls代表类本身，不需要传入self参数

- 调用：类名.方法或属性、cls.方法或属性
>说明
- 在一个类中，要调用方法或属性，一般都要创建实例，才能调用，但是有时候会觉得创建实例比较麻烦

- 使用@classmethod，可用不创建实例就能调用此类方法。相比于@staticmethod 在调用方面会显得更加自由、灵活
- 与静态类不一样的就是它可以传进来一个当前类作为第一个参数

```python
class A:
    def func1(self, a, b):
        print(a + b)

    @classmethod
    def func2(cls, a, b):
        print(a + b)

a = A()
a.func1(1, 2)
a.func2(1, 2)
print("------------------")
A.func1(None, 1, 2)
A.func2(1, 2)
```

&emsp;
## (3) property
- 经过property装饰过的函数 不再是一个函数,而是一个property,可以直接类名.property
```python
class BBox:
    def __init__(self, l, t, r, b):
        self.l = l
        self.t = t
        self.r = r
        self.b = b
    
    @property
    def center(self):
        return (self.l + self.r) * 0.5, (self.t + self.b) * 0.5
    
    @property
    def width(self):
        return self.r - self.l + 1
    
    @property
    def height(self):
        return self.b - self.t + 1
```

