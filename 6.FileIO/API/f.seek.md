&emsp;
# f.seek
seek() 方法用于移动文件读取指针到指定位置。

>语法
```py
fileObject.seek(offset, from_what)
```
>参数
- offset -- 开始的偏移量，也就是代表需要移动偏移的字节数，如果是负数表示从倒数第几位开始。
- from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾

>返回值
如果操作成功，则返回新的文件位置，如果操作失败，则函数返回 -1。


```python
f = open('./files/foo2.txt', 'rb+')
f.write(b'0123456789abcdef')
f.seek(5)     # 移动到文件的第六个字节
f.read(1)
f.seek(-3, 2) # 移动到文件的倒数第三字节
f.read(1)
f.close()
```

