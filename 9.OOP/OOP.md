&emsp;
# 面向对象 Object Oriented Programming

Python从设计之初就已经是一门面向对象的语言，正因为如此，在Python中创建一个类和对象是很容易的。

&emsp;
# 1面向对象相关概念
- `Class(类)`: 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。

- `Method(方法)`：类中定义的函数。

- `类变量`：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。

- `方法重写`：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
称为实例变量，实例变量就是一个用 self 修饰的变量。

- `继承`：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。

- `实例化`：创建一个类的实例，类的具体对象。

- `对象`：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。

和其它编程语言相比，Python 在尽可能不增加新的语法和语义的情况下加入了类机制。

- Python中的类提供了面向对象编程的所有基本功能：类的继承机制允许多个基类，派生类可以覆盖基类中的任何方法，方法中可以调用基类中的同名方法。

- 对象可以包含任意数量和类型的数据。

&emsp;
# 2 类定义
>语法格式
```python
class ClassName(object): # object 可省略
    <statement-1>
    .
    .
    .
    <statement-N>
```

类实例化后，可以使用其属性，实际上，创建一个类之后，可以通过类名访问其属性。

&emsp;
# 3 类对象
- 类对象支持两种操作：属性引用和实例化。

- 属性引用使用和 Python 中所有的属性引用一样的标准语法：obj.name。

- 类对象创建后，类命名空间中所有的命名都是有效属性名。
>示例
```python
class MNISTDataset():
    images_path = "/datav/MyLesson/Dataset/MNIST/raw/t10k-images-idx3-ubyte"
    labels_path = "/datav/MyLesson/Dataset/MNIST/raw/t10k-labels-idx1-ubyte"
    def func(self):
        return "MNIST"
 
# 实例化类
x = MNISTDataset()
 
# 访问类的属性和方法
print(x.images_path)
print(x.labels_path)
print(x.func())
```

&emsp;
## 3.1 __init__方法
- 类有一个名为 `__init__()` 的特殊方法（构造方法），该方法在类实例化时会自动调用
- \_\_init__() 方法可以有参数，参数通过 \_\_init__() 传递到类的实例化操作上。

>示例
```python
from utils import *

class MNISTDataset():
    def __init__(self, images_path, labels_path):
        self.images = mnist_images(images_path)
        self.labels = mnist_labels(labels_path)


if __name__ == '__main__':
    test_i  = "/datav/MyLesson/Dataset/MNIST/raw/t10k-images-idx3-ubyte"
    test_l  = "/datav/MyLesson/Dataset/MNIST/raw/t10k-labels-idx1-ubyte"

    test_set = MNISTDataset(test_i, test_l)
    print(test_set.images.shape)
    print(test_set.labels.shape)
```

&emsp;
## 3.2 self
self代表类的实例，而类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
```python
class Test:
    def printinfo(self): # self 可以是自己定的变量名称，约定俗成用self
        print(self)
        print(self.__class__)
 
t = Test()
t.printinfo()
print(hex(id(t)))
'''
输出：
<__main__.Test object at 0x7f5299d32e80>
<class '__main__.Test'>
0x7f5299d32e80
'''
```

从执行结果可以很明显的看出，self 代表的是类的实例，代表当前对象的地址，而 self.class 则指向类。

self 不是 python 关键字，我们把他换成 xxx 也是可以正常执行的:
```python
class Test:
    def printinfo(xxx):
        print(xxx)
        print(xxx.__class__)

t = Test()
t.printinfo()
print(hex(id(t)))
```

&emsp;
# 4 类的方法
在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例。


>示例
```python
from utils import *

class MNISTDataset():
    def __init__(self, images_path, labels_path):
        self.images = mnist_images(images_path)
        self.labels = mnist_labels(labels_path)

    def printinfo(self):
        print("images.shape: ", self.images.shape)
        print("labels.shape: ", self.labels.shape)


if __name__ == '__main__':
    test_i  = "/datav/MyLesson/Dataset/MNIST/raw/t10k-images-idx3-ubyte"
    test_l  = "/datav/MyLesson/Dataset/MNIST/raw/t10k-labels-idx1-ubyte"

    test_set = MNISTDataset(test_i, test_l)
    test_set.printinfo()
```

&emsp;
# 5 继承
Python 同样支持类的继承，如果一种语言不支持继承，类就没有什么意义。派生类的定义如下所示:
```python
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```

- DerivedClassName(子类或者说派生类) 会继承父类（基类 BaseClassName）的属性和方法。
- BaseClassName（实例中的基类名）必须与派生类定义在一个作用域内。
>示例
```python
class Module:
    def __init__(self, name):
        self.name = name
    
    def printinfo(self):
        print(f"这是 {self.name} 模块")

class Linear(Module):
    pass

linear = Linear("Linear")
# 子类并没有写 name 但是继承了，函数printinfo()同理
print(linear.name)
linear.printinfo()
```


&emsp;
# 6 方法重写
- 如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法

>示例
```python
class Module:
    def __init__(self, name):
        self.name = name
    
    def printinfo(self):
        print(f"这是 {self.name} 模块")

class Linear(Module):
    def printinfo(self):
        print(f"这是 {self.name} 模块，也就是线性层")

linear = Linear("Linear")
print(linear.name)
linear.printinfo()
```

&emsp;
## 6.1 子类继承父类构造函数
子类继承父类构造函数的3种方法：
- 不重写 \_\_init__，实例化子类时，会自动调用父类定义的 \_\_init__。
- 重写 \_\_init__，显式地调用父类的构造方法
- 重写 \_\_init__，用 super 关键字 

注意：
- 如果重写了__init__ 时，实例化子类，就不会调用父类已经定义的 \_\_init__

>示例：重写 \_\_init__ 会覆盖父类  \_\_init__
```python
class Module:
    def __init__(self, name):
        self.name = name
        print("父类构造")
    
    def printinfo(self):
        print("这是 {self.name} 模块")

class Linear(Module):
    def __init__(self, name, layers):
        self.name = name
        self.layers = layers
        print("子类构造")

    def printinfo(self):
        print("这是 {self.name} 模块，也就是线性层")

linear = Linear("Linear", 16)
print(linear.name)
linear.printinfo()
```


>示例：子类继承父类构造函数的3种方法
```python
class Module:
    def __init__(self, name):
        self.name = name
    
    def printinfo(self):
        print("这是 {self.name} 模块")

# 方法一：直接不重写 __init__() 函数
class Linear(Module):
    def printinfo(self):
        print("这是 {self.name} 模块，也就是线性层")

# 方法二：显示调用父类__init__函数
class Linear(Module):
    def __init__(self, name, layers): 
        Module.__init__(self, name)

    def printinfo(self):
        print("这是 {self.name} 模块，也就是线性层")

# 方法三：用 super 关键字
class Linear(Module):
    def __init__(self, name):
        super().__init__(name)

linear = Linear("Linear")
print(linear.name)
linear.printinfo()
```

&emsp;
## 6.2 super()函数
&emsp;
### (1) 描述
- super() 函数是用于调用父类的一个方法。


&emsp;
### (2) 语法
```python
super(ClassName, Object)
```

&emsp;
### (3) 参数
- ClassName -- 类。
- Object -- 对象或实例，一般是 self
Python3.x 和 Python2.x 的一个区别是: Python 3 可以使用直接使用 super().xxx 代替 super(Class, self).xxx :


&emsp;
### (4) 实例
>用 super 关键字继承父类构造函数
```python
super(子类，self).__init__(参数1，参数2，....)
```

>示例：super 的 2 种写法
```python
class Module:
    def __init__(self, name):
        self.name = name
    
    def printinfo(self):
        print("这是 {self.name} 模块")

# 写法一：super(子类，self).__init__(参数1，参数2，....)
class Linear(Module):
    def __init__(self, name):
        super(Linear, self).__init__(name)
        print(type(super(Linear, self)))

# 写法二：Python3 可以使用直接使用 super().xxx 代替 super(Class, self).xxx
class Linear(Module):
    def __init__(self, name):
        super().__init__(name)

linear = Linear("Linear")
print(linear.name)
linear.printinfo()
```


&emsp;
# 7 类属性与方法
- xx: 公有变量
- _x: 单前置下划线,私有化属性或方法，from somemodule import 禁止导入,类对象和子类可以访问
- __xx: 双前置下划线,避免与子类中的属性命名冲突，无法在外部直接访问(名字重整所以访问不到)
- \_\_xx__: 双前后下划线,用户名字空间的魔法对象或属性。例如:\_\_init__, 不要自己发明这样的名字
- xx_: 单后置下划线,用于避免与Python关键词的冲突

&emsp;
## 7.1 类的私有属性
__private_attrs
- 两个下划线开头，声明该属性为私有
- 不能在类的外部被使用或直接访问
- 在类内部的方法中使用时 self.__private_attrs。

&emsp;
## 7.2 类的方法
在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self，且为第一个参数，self 代表的是类的实例。

self 的名字并不是规定死的，也可以使用 this，但是最好还是按照约定使用 self。

&emsp;
## 7.3 类的私有方法
__private_method
- 两个下划线开头，声明该方法为私有方法
- 只能在类的内部调用 ，不能在类的外部调用。self.__private_methods。

&emsp;
## 7.4 实例
>类的私有属性
```python
class A():
    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    def printinfo(self):
        print(self.name)
        print(self._age)
        print(self.__weight)

a = A("Tom", 12, 40)
a.printinfo()

print(a.name)
print(a._age)
print(a.__weight)
```


>类的私有方法
```python
class A():
    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    def printinfo(self):
        print(self.name)
        print(self._age)
        print(self.__weight)

    def __private_method(self):
        print("私有方法")

a = A("Tom", 12, 40)
a.printinfo()
# a.__private_method() # 报错
```

&emsp;
## 7.5 类的专有方法（魔术方法）
- `__init__` : 构造函数，在生成对象时调用
- `__len__`: 获得长度
- `__getitem__`: 按照索引获取值
- `__call__`: 函数调用
- `__repr__` : 打印，转换
- `__getattr__`: 定义当用户试图获取一个不存在的属性时的行为
- `__iter__`: 定义当迭代容器中的元素的行为
- `__next__`: 定义迭代返回的内容
- `__dict__`: 类的静态函数、类函数、普通函数、全局变量以及一些内置的属性都放在类__dict__里
- `__and__`: 与（&）运算
- `__or__`: 或（|）运算
- `__xor__`: 异或（^）运算
>示例：len getiem repr iter next
```python
from utils import *
class MNISTDataset():
    def __init__(self, images, labels):
        self.images = mnist_images(images)
        self.labels = mnist_labels(labels)
    
    def __len__(self):
        return len(self.labels)

    def __getitem__(self, index):
        return self.labels[index], self.images[index]

    def __repr__(self):
        return "MNIST手写数据集"

class DataLoader():
    def __init__(self, dataset):
        self.dataset = dataset

    def __iter__(self):
        return DataLoaderIterator(self)

    def __len__(self):
        return len(self.dataset)

class DataLoaderIterator():
    def __init__(self, dataloader):
        self.dataloader = dataloader
        self.cursor = 0

    def __next__(self):
        if self.cursor > len(self.dataloader):
            raise StopIteration()
        data = self.dataloader.dataset[self.cursor]
        self.cursor += 1
        return data

train_images = "/datav/MyLesson/Dataset/MNIST/raw/train-images-idx3-ubyte"
train_labels = "/datav/MyLesson/Dataset/MNIST/raw/train-labels-idx1-ubyte"

train_set = MNISTDataset(train_images, train_labels)
train_loader = DataLoader(train_set)

i = 0
for item in train_loader:
    print(item[0])
    print(item[1].shape)
    i += 1
    if i > 3:
        break
```

>示例：call
```python
import numpy as np

class Sigmoid():
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def __call__(self, x):
        return self.sigmoid(x)

s = Sigmoid()
print(s(5))
```

&emsp;
## 7.6 运算符重载
Python同样支持运算符重载，我们可以对类的专有方法进行重载，实例如下：

>示例
```python
class BBox:
    def __init__(self, l, t, r, b):
        self.l = l
        self.t = t
        self.r = r
        self.b = b
    
    # 交集, 重载 &，不是 +，+是__add__
    def __and__(self, other):
        cross_l = max(self.l, other.l)
        cross_t = max(self.t, other.t)
        cross_r = min(self.r, other.r)
        cross_b = min(self.b, other.b)
        cross_box = BBox(cross_l, cross_t, cross_r, cross_b)
        if cross_box.width <= 0 or cross_box.height <= 0:
            return 0
        return cross_box.area
    
    # 并集
    def __or__(self, other):
        cross = self & other
        union = self.area + other.area - cross
        return union
    
    #IoU
    def __xor__(self, other):
        cross = self & other
        union = self | other
        return cross / (union + 1e-6)
```