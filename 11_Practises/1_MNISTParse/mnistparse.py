import struct
import numpy as np


def mnist_labels(directory):
    with open(directory, "rb") as f:
        data = f.read()
    # MNIST 的label文件前面2个32bit（4字节）分别是
    # magic number, number of images
    magic_num, num_of_item = struct.unpack_from(">II", data, 0)
    labels = struct.unpack_from("B"*num_of_item, data, 8)
    return np.array(labels)

def mnist_images(directory):
    with open(directory, "rb") as f:
        data = f.read()
    # MNIST 的label文件前面8个32bit（4字节）分别是
    # magic number, number of images
    # number of rows, number of columns
    magic_num, num_of_item, rows, cols = struct.unpack_from('>IIII', data, 0)
    images = struct.unpack_from("B"*rows*cols*num_of_item, data, 16)
    return np.array(images).reshape(num_of_item, -1)
    
def onehot(labels, classes):
    res  = np.zeros((len(labels), classes))
    rows = res.shape[0]
    for row in range(rows):
        label = labels[row]
        res[row, label] = 1
    return res

if __name__ == "__main__":
    test_labels = mnist_labels("/datav/MyLesson/Dataset/MNIST/raw/t10k-labels-idx1-ubyte")
    test_images = mnist_images("/datav/MyLesson/Dataset/MNIST/raw/t10k-images-idx3-ubyte")
    onehot_label = onehot(test_labels, 10)
    print(test_labels[0])
    print(onehot_label[0])