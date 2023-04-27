import hashlib
import numpy as np
from pathlib import Path
import re
import os
from hashlib import md5



def mkdirs(path):
    try:
        os.makedirs(path)
    except Exception as e:
        ...


def mkparents(path):
    parents = Path(path).parent
    if not os.path.exists(parents):
        mkdirs(parents)




def xml_parse(file, label_map):
    with open(file) as f:
        data = f.read().replace("\t", "").replace("\n", "")

    objs = re.findall(r"<object>(.*?)</object>", data)
    annotations = []
    for obj in objs:
        name = re.findall(r"<name>(.*?)</name>", obj)[0]
        xmin = re.findall(r"<xmin>(.*?)</xmin>", obj)[0]
        ymin = re.findall(r"<ymin>(.*?)</ymin>", obj)[0]
        xmax = re.findall(r"<xmax>(.*?)</xmax>", obj)[0]
        ymax = re.findall(r"<ymax>(.*?)</ymax>", obj)[0]
        annotations.append((xmin, ymin, xmax, ymax, label_map.index(name)))
    
    if len(annotations) == 0:
        annotations = np.zeros((0, 5))
    return np.array(annotations, dtype=np.float32)


def get_md5(data):
    return hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()




if __name__ == "__main__":
    label_map = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]

    annotations = xml_parse("/datav/MyLesson/Dataset/VOC2007/VOCdevkitTrain/VOC2007/Annotations/000005.xml", label_map)
    print(annotations)