&emsp;
# 数据结构高级

&emsp;
# 1 列表
Python中列表是可变的，这是它区别于字符串和元组的最重要的特点，一句话概括即：列表可以修改，而字符串和元组不能。

&emsp;
## 1.1 列表推导式
&emsp;&emsp;列表推导式创建列表很优雅。

&emsp;&emsp;每个列表推导式都在 for 之后跟一个表达式，然后有零到多个 for 或 if 子句。返回结果是一个根据表达从其后的 for 和 if 上下文环境中生成出来的列表。如果希望表达式推导出一个元组，就必须使用括号。

>示例
```python
import os

root = "/datav/MyLesson/Dataset/VOC2007/VOCdevkitTrain/VOC2007"
annotations_path = os.path.join(root, "Annotations")
annotations = os.listdir(annotations_path)
jpegs = [item[:-3] + "jpg" for item in annotations]

print(jpegs[0])
```

&emsp;
## 1.2 嵌套列表

```python
from utils import *

class Dataset():
    def __init__(self, images, labels):
        self.images = mnist_images(images)
        self.labels = one_hot(mnist_labels(labels), 10)

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, index):
        return self.labels[index], self.images[index]


class DataLoader():
    def __init__(self, dataset, batch_size, shuffle):
        self.dataset = dataset
        self.batch_size = batch_size
        self.shuffle = shuffle

    def __iter__(self):
        return DataLoaderIterator(self)

class DataLoaderIterator():
    def __init__(self, dataloader):
        self.dataset = dataloader.dataset
        self.batch_size = dataloader.batch_size
        self.shuffle = dataloader.shuffle
        self.indices = list(range(len(self.dataset)))
        self.cursor = 0

        if self.shuffle:
            np.random.shuffle(self.indices)

    def __next__(self):
        if self.cursor > (n := len(self.dataset)):
            raise StopIteration
        
        batch_data = []
        batch_size = min(self.batch_size, n - self.cursor)

        for i in range(batch_size):
            
            index = self.indices[self.cursor]
            data = self.dataset[index]
            # 每次调用__next__都会执行
            if len(batch_data) == 0: 
                batch_data = [[] for i in range(len(data))]
            # labels 和 images 对应的 list 分别 append 进去
            for index, item in enumerate(data):
                batch_data[index].append(item)
            
            self.cursor += 1
        # labels 和 images 对应的 list 分别做 vstack
        for index in range(len(batch_data)):
            batch_data[index] = np.vstack(batch_data[index])
        return batch_data

if __name__ == "__main__":
    train_images = "/datav/MyLesson/Dataset/MNIST/raw/train-images-idx3-ubyte"
    train_labels = "/datav/MyLesson/Dataset/MNIST/raw/train-labels-idx1-ubyte"
    test_images  = "/datav/MyLesson/Dataset/MNIST/raw/t10k-images-idx3-ubyte"
    test_labels  = "/datav/MyLesson/Dataset/MNIST/raw/t10k-labels-idx1-ubyte"

    # train_set =
    test_set  = Dataset(test_images, test_labels)
    test_loader = DataLoader(test_set, 16, True)
    for batch_labels, batch_images in test_loader:
        print(batch_labels.shape)
        print(batch_images.shape)
        break
```

