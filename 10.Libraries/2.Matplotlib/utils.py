import struct
import time
import numpy as np
import os.path as osp
import matplotlib.pyplot as plt


def mnist_labels(path):
    with open(path, "rb") as f:
        data = f.read()
    _, num_item = struct.unpack_from(">II", data, 0)
    labels = struct.unpack_from("B"*num_item, data, 8)
    return np.array(labels)
    
def mnist_images(path):
    with open(path, "rb") as f:
        data = f.read()
    _, num_item, rows, cols = struct.unpack_from(">iiii", data, 0)
    images = struct.unpack_from("B"*num_item*rows*cols, data, 16)
    return np.array(images).reshape(num_item, -1)

def showtime(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print("Time cost: ", time.time() - start)
    return wrapper


def one_hot(labels, classes=10):
    res  = np.zeros((len(labels), classes))
    rows = res.shape[0]
    for row in range(rows):
        label = labels[row]
        res[row, label] = 1
    return res

if __name__ == '__main__':
    root = "/Users/azen/Desktop/myAir/Work/Workspace/Others/Dataset/MNIST"
    train_images = osp.join(root, "train-images-idx3-ubyte")
    train_lables = osp.join(root, "train-labels-idx1-ubyte")

    test_images  = osp.join(root, "t10k-images-idx3-ubyte")
    test_labels  = osp.join(root, "t10k-labels-idx1-ubyte")
    
    test_labels = mnist_labels(train_lables)
    test_images = mnist_images(test_images).reshape(-1, 28, 28)

    print(test_images.shape)
    sample = test_images[np.random.choice(10000)]
    plt.imshow(sample, cmap='gray')
    plt.show()
