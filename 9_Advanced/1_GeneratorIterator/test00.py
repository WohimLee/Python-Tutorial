from utils import *

class Dataset():
    def __init__(self, images, labels):
        self.images = mnist_images(images)
        self.labels = one_hot(mnist_labels(labels), 10)

    def __getitem__(self, index):
        return self.labels[index], self.images[index]

    def __len__(self):
        return len(self.labels)


def DataLoader(dataset):
    cursor = 0
    while True:
        if cursor > len(dataset):
            raise StopIteration
        label = dataset.labels[cursor]
        image = dataset.images[cursor]
        cursor += 1
        yield label, image


if __name__ == '__main__':
    test_labels = "/datav/MyLesson/Dataset/MNIST/raw/t10k-labels-idx1-ubyte"
    test_images = "/datav/MyLesson/Dataset/MNIST/raw/t10k-images-idx3-ubyte"

    test_set = Dataset(test_images, test_labels)
    test_loader = DataLoader(test_set)

    for label, image in test_loader:
        print(label, image.shape)
        break