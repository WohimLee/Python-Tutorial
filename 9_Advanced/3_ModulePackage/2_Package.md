
&emsp;
# Package 包

- 假设有一套统一处理声音文件和数据的模块（或者称之为一个"包"）。
- 音频文件格式有： .wav，:file:.aiff，:file:.au等，所以你需要有一组不断增加的模块，用来在不同的格式之间转换。
- 针对这些音频数据，有很多操作（比如混音，添加回声，增加均衡器功能，创建人造立体声效果），所以你还需要一组怎么也写不完的模块来处理这些操作。
- 包结构（在分层的文件系统中）大概如下:

```
sound/                          顶层包
      __init__.py               初始化 sound 包
      formats/                  文件格式转换子包
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  声音效果子包
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  filters 子包
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```

&emsp;
# 1 \_\_init__.py 文件

- 在当前目录下有 `__init__.py` 文件的目录即为一个package
    - 空的 \_\_init__.py 文件
    - 包含代码的\_\_init__.py文件
    - 无论空与非空，这个目录都会被认为是一个package
- 在 import package 的时候会执行 \_\_init__.py
- 在导入一个包的时候，Python 会根据 sys.path 中的目录来寻找这个包中包含的子目录

&emsp
## 1.1 \_\_all__

如果使用 from sound.effects import * 
- Python 会进入文件系统，找到这个包里面所有的子模块，然后一个一个的把它们都导入进来 
- `__init__.py` 有 `__all__` 的列表变量，那么在使用 from package import * 的时候就把这个列表中的所有名字作为包内容导入 
- 在更新包函数和变量等内容后，记住 `__all__` 也要更新

>sounds/effects/\_\_init__.py 中代码
```python
__all__ = ["echo", "surround", "reverse"]
# 这表示当你使用from sound.effects import * 这种用法时，你只会导入包里面这三个子模块。
```

&emsp;
# 2 import 语句
## 2.1 import `package`

>示例
```python
import sound
```

&emsp;
## 2.2 import `package.package`
>示例
```python
import sound.effects
import sound.filters # 没有 __init__.py 文件，无法导入
import sound.formats # 没有 __init__.py 文件，无法导入
```

&emsp;
## 2.3 import `package.package.module`
>示例
```python
import sound.effects.echo
import sound.effects.reverse
import sound.effects.surround

# 导入子模块:sound.effects.echo, 但必须使用全名去访问:
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
```


&emsp;
# 3 from ... import ... 语句
&emsp;
## 3.1 from `package` import `package1, package2...`
>示例
```python
from sound import effects, filters, formats 

# 导入子模块:effects, 但必须使用全名去访问:
effects.echo.echofilter(input, output, delay=0.7, atten=4)
```

## 3.1 from `package.package...` import `module1, module2...`
>示例
```python
from sound.effects import echo 

# 导入子模块:sound.effects.echo, 但必须使用全名去访问:
echo.echofilter(input, output, delay=0.7, atten=4)
```

&emsp;
## 3.2 from `package.module` import `classes/functions`

>示例
```python
from sound.effects.echo import echofilter

# 导入子模块:sound.effects.echo 的函数, echofilter
echofilter(input, output, delay=0.7, atten=4)
```



&emsp;
# 总结
（1）不推荐使用 * 这种方法来导入模块，因为这种方法经常会导致代码的可读性降低。不过这样倒的确是可以省去不少敲键的功夫

（2）使用 from Package import specific_submodule 这种方法永远不会有错。这也是推荐的方法。除非是你要导入的子模块有可能和其他包的子模块重名。

