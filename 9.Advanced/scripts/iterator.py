import numpy as np
from utils import *

class MNISTDataset():
    def __init__(self, images, labels):
        self.images = mnist_images(images)
        self.labels = one_hot(mnist_labels(labels),10)
    
    def __getitem__(self, index):
        return self.images[index], self.labels[index]

    def __len__(self):
        return len(self.labels)

class DataLoader():
    def __init__(self, dataset, batch_size, shuffle):
        self.dataset = dataset
        self.batch_size = batch_size
        self.shuffle = shuffle

    def __iter__(self):
        return DataLoaderIterator(self, self.dataset, self.batch_size, self.shuffle)

    def __len__(self):
        return len(self.dataset)

class DataLoaderIterator():
    def __init__(self, dataloader, dataset, batch_size, shuffle):
        self.dataloader = dataloader
        self.dataset = dataset
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.cursor = 0
        self.indices = list(range(len(self.dataloader)))
        if self.shuffle :
            np.random.shuffle(self.indices)
    
    def __next__(self):
        if self.cursor >= (n := len(self.dataset)):
            raise StopIteration()
        
        batch_data = []
        batch_size = min(self.batch_size, n - self.cursor)
        for i in range(batch_size):
            index = self.indices[self.cursor]
            data = self.dataset[index]
            if len(batch_data) == 0:
                batch_data = [[] for i in range(len(data))]

            for index, item in enumerate(data):
                batch_data[index].append(item)
            self.cursor += 1
        
        for index in range(len(batch_data)):
            if index ==0:
                a = np.array(batch_data[index]).reshape(16,28,28)
                batch_data[index] = np.expand_dims(a,1)
                print(batch_data[index].shape)
               # batch_data[index] = np.vstack()
            batch_data[index] = np.vstack(batch_data[index])
        return batch_data


if __name__ == '__main__':
    test_images  = "/datav/MyLesson/Dataset/MNIST/raw/t10k-images-idx3-ubyte"
    test_labels  = "/datav/MyLesson/Dataset/MNIST/raw/t10k-labels-idx1-ubyte"
    train_images = "/shigaohui/class/7_Function/MNIST/train-images-idx3-ubyte"
    train_labels = "/shigaohui/class/7_Function/MNIST/train-labels-idx1-ubyte"

    test_dataset = MNISTDataset(test_images, test_labels)
    # train_dataset = MNISTDataset(train_images, train_labels)
    dataLoader = DataLoader(test_dataset,16,True)
    for images, labels in dataLoader:
        print(labels.shape)
        print(images.shape)
        break
    