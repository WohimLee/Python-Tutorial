&emsp;
# f.readline

- f.readline() 会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。

>示例
```python
# 打开一个文件
f = open("./data/foo1.txt", "r")
str = f.readline()
print(str)
# 关闭打开的文件
f.close()
'''执行以上程序，输出结果为：
Python 是一个非常好的语言。'''
```



&emsp;
# f.readlines
- f.readlines() 将返回该文件中包含的所有行
- 如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割

  ```python
  # 打开一个文件
  f = open("./files/foo1.txt", "r")
  str = f.readlines()
  print(str)
  # 关闭打开的文件
  f.close()
  '''执行以上程序，输出结果为：
  ['Python 是一个非常好的语言。\n', '是的，的确非常好!!\n']'''

  # 另一种方式是迭代一个文件对象然后读取每行
  # 打开一个文件
  f = open("./files/foo1.txt", "r")
  for line in f:
      print(line, end='')
  # 关闭打开的文件
  f.close()
  '''执行以上程序，输出结果为：

  Python 是一个非常好的语言。
  是的，的确非常好!!'''
  ```


