
import struct
import numpy as np

def mnist_labels(path):
    with open(path, "rb") as f:
        data = f.read()
    magic_number, num_of_items = struct.unpack_from(">II", data, 0)
    labels = struct.unpack_from("b"*num_of_items, data, 8)
    return np.array(labels)


def mnist_images(path):
    with open(path, "rb") as f:
        data = f.read()
    magic_num, num_of_items, rows, cols = struct.unpack_from(">IIII", data, 0)
    images = struct.unpack_from("B"*rows*cols*num_of_items, data, 16)
    return np.array(images).reshape(num_of_items, rows, cols)


def one_hot(labels, classes):
    '''
    用途：将 labels 转换成 one hot 编码
    '''
    output = np.zeros((len(labels), classes))
    for row in range(len(labels)):
        index = labels[row]
        output[row, index] = 1
    return output


if __name__ == "__main__":

    train_labels = "/datav/MyLesson/Dataset/MNIST/raw/train-labels-idx1-ubyte"
    train_images = "/datav/MyLesson/Dataset/MNIST/raw/train-images-idx3-ubyte"

    train_labels = mnist_labels(train_labels) # shape = (60000,)
    # train_images = mnist_images(train_images) # shape = (60000, 784)
    # print(train_labels[5])
    # print("MNIST images.shape: ", train_images.shape)

    one_hot_labels = one_hot(train_labels, 10)
    print(train_labels[7])
    print(one_hot_labels[7])






