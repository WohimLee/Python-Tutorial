
from utils import *

class Dataset():
    def __init__(self, labels, images):
        self.labels = one_hot(mnist_labels(labels), 10)
        self.images = mnist_images(images)

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, index):
        return self.labels[index], self.images[index]

class DataLoader():
    def __init__(self, dataset, batch_size, shuffle = False):
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
        if self.cursor > len(self.dataset):
            raise StopIteration

        batch_data = []
        for i in range(self.batch_size):
            index = self.indices[self.cursor]
            data = self.dataset[index]

            if len(batch_data) == 0:
                batch_data = [[] for i in range(len(data))]

            for index, item in enumerate(data):
                batch_data[index].append(item)

            self.cursor += 1

        for index in range(len(batch_data)):
            batch_data[index] = np.vstack(batch_data[index])
        return batch_data




if __name__ == "__main__":
    train_labels = "/datav/MyLesson/Dataset/MNIST/raw/train-labels-idx1-ubyte"
    train_images = "/datav/MyLesson/Dataset/MNIST/raw/train-images-idx3-ubyte"
    test_labels  = "/datav/MyLesson/Dataset/MNIST/raw/t10k-labels-idx1-ubyte"
    test_images  = "/datav/MyLesson/Dataset/MNIST/raw/t10k-images-idx3-ubyte"

    test_set = Dataset(test_labels, test_images)
    test_loader = DataLoader(test_set, 16, True)
    it = iter(test_loader)
    # print(it.indices)

    for batch_labels, batch_images in test_loader:
        print(batch_labels.shape)
        print(batch_images.shape)
        break

    # (样本数， 类别)
    # (样本数，channels, height, width)
    # (batch_size, 10)
    # (batch_size, 1, 28, 28)
