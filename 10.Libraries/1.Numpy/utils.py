import struct
import time
import numpy as np
import os.path as osp


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

@showtime
def one_hot1(label, classes=10):
    n = len(label)
    res = np.zeros((n, classes))
    res[np.arange(n), label] = 1
    return res

@showtime
def one_hot2(labels, classes=10):
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
    print(len(test_labels))
    
    one_hot1(test_labels)
    
    one_hot2(test_labels)
    

