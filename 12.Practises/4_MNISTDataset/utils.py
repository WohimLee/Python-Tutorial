import struct
import numpy as np

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






if __name__ == '__main__':
    test_i  = "/datav/MyLesson/Dataset/MNIST/raw/t10k-images-idx3-ubyte"
    test_l  = "/datav/MyLesson/Dataset/MNIST/raw/t10k-labels-idx1-ubyte"
    train_i = "/datav/MyLesson/Dataset/MNIST/raw/train-images-idx3-ubyte"
    train_l = "/datav/MyLesson/Dataset/MNIST/raw/train-labels-idx1-ubyte"

    test_labels = mnist_labels(test_l)
    test_images = mnist_images(test_i)
    print(test_labels.shape)
    print(test_images.shape)

