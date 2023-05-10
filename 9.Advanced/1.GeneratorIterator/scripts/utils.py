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


def one_hot(labels, classes):
    '''
    用途：将 labels 转换成 one hot 编码
    '''
    output = np.zeros((len(labels), classes))
    for row in range(len(labels)):
        index = labels[row]
        output[row, index] = 1
    return output