import struct
import time
import re
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


def xml_parse(file, label_map):
    import re
    with open(file) as f:
        data = f.read().replace("\t", "").replace("\n", "")
    objs = re.findall(r"<object>(.*?)</object>", data)
    obj_bboxes = []
    for obj in objs:
        xmin = re.findall(r"<xmin>(.*?)</xmin>", obj)[0]
        ymin = re.findall(r"<ymin>(.*?)</ymin>", obj)[0]
        xmax = re.findall(r"<xmax>(.*?)</xmax>", obj)[0]
        ymax = re.findall(r"<ymax>(.*?)</ymax>", obj)[0]
        name = re.findall(r"<name>(.*?)</name>", obj)[0]
        obj_bboxes.append((xmin, ymin, xmax, ymax, label_map.index(name)))
    res = np.zeros((0, 5), dtype = np.float32)
    if len(obj_bboxes) > 0:
        res = np.array(obj_bboxes, dtype=np.float32)
    return res

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
    test_images = mnist_images(test_images).reshape(-1, 28, 28)

    # print()
    plt.imshow(test_images[0])
    plt.show()

