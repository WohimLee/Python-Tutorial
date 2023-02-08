import re
import os
import datetime
import hashlib 
import logging
import numpy as np

from pathlib import Path

def get_md5(data):
    return hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()

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


def build_default_logger():
    '''
    只作输出的logger
    '''
    logger = logging.getLogger("DefaultLogger")
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('[%(levelname)s][%(filename)s:%(lineno)d][%(asctime)s]: %(message)s')
    s_handler = logging.StreamHandler()
    s_handler.setFormatter(formatter)
    logger.addHandler(s_handler)
    return logger


# 单例模式
class SingleInstanceLogger:
    def __init__(self):
        self.logger = build_default_logger()

    def __getattr__(self, name):
        return getattr(self.logger, name)

_single_instance_logger = SingleInstanceLogger()

def build_logger(path):
    '''
    用于训练时记录日志，每天记录，保持一周7天的记录
    '''
    logger = logging.getLogger("NewLogger")
    logger.setLevel(logging.INFO)
    mkparents(path)

    trf_handler = logging.handlers.TimedRotatingFileHandler(path, when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
    formatter = logging.Formatter('[%(levelname)s][%(filename)s:%(lineno)d][%(asctime)s]: %(message)s')
    trf_handler.setFormatter(formatter)
    logger.addHandler(trf_handler)

    s_handler = logging.StreamHandler()
    s_handler.setFormatter(formatter)
    logger.addHandler(s_handler)
    return logger

# 训练时记录日志 
def setup_single_instance_logger(path):
    global _single_instance_logger
    _single_instance_logger.logger = build_logger(path)


if __name__ == "__main__":
    annotations_path = "/datav/MyLesson/Dataset/VOC2007/VOCdevkitTrain/VOC2007/Annotations/000005.xml"
    label_map = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
    annotations = xml_parse(annotations_path, label_map)
    print(annotations)