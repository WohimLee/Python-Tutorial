&emsp;
# OS 文件/目录方法

# 1 os方法
>os.listdir(path)
- 返回path指定的文件夹包含的文件或文件夹的名字的列表。
    ```python
    import os
    annotations = "/datav/MyLesson/Dataset/VOC2007/VOCdevkitTest/VOC2007/Annotations"
    jpgs = "/datav/MyLesson/Dataset/VOC2007/VOCdevkitTest/VOC2007/JPEGImages"

    annotations = os.listdir(annotations)
    jpgs = os.listdir(jpgs)
    print(annotations[0])
    print(jpgs[0])
    ```

&emsp;
>os.makedirs()
- os.makedirs() 方法用于递归创建目录。
- 如果子目录创建失败或者已经存在，会抛出一个 OSError 的异常，
    ```python
    os.makedirs(path, mode=0o777)
    ```
- path -- 需要递归创建的目录，可以是相对或者绝对路径。
- mode -- 权限模式。
    ```python
    import os
    path = "./aaa/bbb/ccc"
    os.makedirs(path)
    ```

&emsp;
>os.remove(path) —— 删文件
- os.remove() 方法用于删除指定路径的文件。如果指定的路径是一个目录，将抛出OSError
```python
os.remove(path)
```
- path -- 要移除的文件路径

```python
import os
os.remove("./aaa/bbb/ccc/test.txt")
```

&emsp;
>os.removedirs(path) —— 删文件夹
- os.removedirs() 方法用于递归删除目录。如果子文件夹成功删除, removedirs()才尝试它们的父文件夹,直到抛出一个error(它基本上被忽略,因为它一般意味着你文件夹不为空)
```python
os.removedirs(path)
```
- path -- 要移除的目录路径

```python
import os
os.removedirs("./aaa/bbb/ccc")
```

&emsp;
>os.rename(src, dst)
- os.rename() 方法用于命名文件或目录，从 src 到 dst,如果dst是一个存在的目录, 将抛出OSError。

```python
os.rename(src, dst)
```
- src -- 要修改的目录名
- dst -- 修改后的目录名

```python
import os

path = "./aaa/bbb/ccc"
os.makedirs(path)
os.rename("./aaa/bbb/ccc", "./aaa/bbb/xxx")
```

&emsp;
>os.walk()
- os.walk() 方法可以创建一个生成器，用以生成所要查找的目录及其子目录下的所有文件
- os.walk() 方法用于通过在目录树中游走输出在目录中的文件名，向上或者向下
- os.walk() 方法是一个简单易用的文件、目录遍历器，可以帮助我们高效的处理文件、目录方面的事情
    ```python
    os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
    ```
- top -- top 目录下的每一个文件夹(包含它自己), 产生(dirpath, dirnames, filenames)【文件夹路径, 文件夹名字, 文件名】
- topdown --可选
    - True: 一个目录的(dirpath, dirnames, filenames)将比它的任何子文件夹的(dirpath, dirnames, filenames)先产生 (目录自上而下)。
    - False: 一个目录的(dirpath, dirnames, filenames)将比它的任何子文件夹的(dirpath, dirnames, filenames)后产生 (目录自下而上)。
- onerror -- 可选，是一个函数; 它调用时有一个参数, 一个OSError实例。报告这错误后，继续walk,或者抛出exception终止walk。
- followlinks -- 设置为 true，则通过软链接访问目录。


```python
import os
for root, dirs, files in os.walk(".", topdown=False):
    # 打印所有【文件】，从 root 开始的路径
    for name in files: 
        print(os.path.join(root, name))
    # 打印所有【文件夹】，从 root 开始的路径
    for name in dirs:  
        print(os.path.join(root, name))
```

&emsp;
# 2 os.path 模块
```py
import os.path as osp
```

&emsp;
>osp.exists
- 判断路径是否存在，路径存在则返回 True，路径损坏返回 False
    ```python
    import os
    if os.path.exists("/datav/MyLesson/1_Python/10_Libraries/4_os/aaa"):
        print("文件夹已存在")
    ```

&emsp;
>osp.join
- 把目录和文件名合成一个路径
    ```python
    import os
    path = os.path.join(".", "aaa", "bbb")
    print(path)
    ```