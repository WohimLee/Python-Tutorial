&emsp;
# FileIO

```py
import os
path = ''
files = os.listdir(path)
```


# 1 基本操作
>open
- open() 将会返回一个 file 对象，基本语法格式如下:
```python
open(filename, mode)
```
- filename：包含了你要访问的文件名称的字符串值。
- mode：这个参数是非强制的，默认文件访问模式为只读(r)。决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表：


  模式	|描述
  :--|:--
  r	|以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式
  r+	|打开一个文件用于读写。文件指针将会放在文件的开头
  w	|打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件
  w+	|打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件
  a	|打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入
  a+	|打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写
  rb	|以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头
  rb+	|以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头
  wb	|以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件
  wb+	|以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件
  ab	|以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入
  ab+	|以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写


&emsp;
>f.close()
- 当你处理完一个文件后, 调用 f.close() 来关闭文件并释放系统的资源



&emsp;
>f.read()
- 用 f.read(size) 可以读取 size 个数据, 然后作为字符串或字节对象返回
- size 是一个可选的数字类型的参数。 当 size 被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回
  ```python
  # 假定文件 foo1.txt 已存在
  # 打开一个文件
  f = open("./files/foo1.txt", "r")
  str = f.read()
  print(str)
  # 关闭打开的文件
  f.close()
  '''执行以上程序，输出结果为：
  Python 是一个非常好的语言。
  是的，的确非常好!!'''
  ```

&emsp;
>f.write()
- f.write(string) 将 string 写入到文件中, 然后返回写入的字符数。
  ```python
  # 将字符串写入到文件 foo1.txt 中：
  # 打开一个文件
  f = open("./files/foo1.txt", "w")
  f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
  # 关闭打开的文件
  f.close()
  ```


&emsp;
# 2 上下文管理器
当处理一个文件对象时, 使用 with 关键字是非常好的方式。在结束后, 它会帮你正确的关闭文件。 而且写起来也比 try - finally 语句块要简短:

```python
with open('./files/foo.txt', 'r') as f:
  read_data = f.read()
```

>示例
```python
with open(savepath, "w") as f:
        f.write("Configuration: \n"+str(cfg)+"\n")
        f.write("Number of parameters: "+str(num_parameters)+"\n")
        f.write("Test accuracy: "+str(acc))
```


&emsp;
# 3 YMAL
- 本质就是字典
```py
import yaml

# Specify the path to your YAML file
file_path = './data/yolov5s.yaml'

# Open the file and load its contents
with open(file_path, 'r') as file:
    yaml_data = yaml.load(file, Loader=yaml.FullLoader)

# Access the data from the YAML file
print(type(yaml_data))
print(yaml_data)
```


&emsp;
# 4 JSON

```py
import json

# Specify the path to your JSON file
file_path = './data/transforms_train.json'

# Open the file and load its contents
with open(file_path, 'r') as file:
    json_data = json.load(file)

# Access the data from the JSON file
print(type(json_data))
print(len(json_data))
print(json_data.keys())
```
