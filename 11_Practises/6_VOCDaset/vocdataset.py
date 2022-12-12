import os
from typing_extensions import Annotated
import cv2
import time
import utils
import torch
import numpy as np

from utils import _single_instance_logger as logger, mkparents, xml_parse

class VOCDataset():
    def __init__(self, root, overwrite = False):
        self.root = root
        self.overwrite = overwrite
        self.label_map = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
        self.num_classes = len(self.label_map)
        self.all_labels = []

        cache_name = utils.get_md5(root)
        # self.cache_file = 
        self.initialize_VOC(f"runs/dataset_cahe/{cache_name}.cache")

    def initialize_VOC(self, cache_file):
        if self.overwrite:
            logger.info(f"Build labels and save to cache: {cache_file}")
            self.build_VOC(cache_file)
        else: 
            if os.path.exists(cache_file):
                logger.info(f"Load labels from cache: {cache_file}")
                self.load_VOC(cache_file)
            else:
                logger.info(f"Build labels and save to cache: {cache_file}")
                self.build_VOC(cache_file)

    def build_VOC(self, cache_file):
        annotations = os.listdir(os.path.join(self.root, "Annotations"))
        jpegimages  = [item[:-3] + "jpg" for item in annotations]

        annotations = [os.path.join(self.root, "Annotations", item) for item in annotations]
        jpegimages  = [os.path.join(self.root, "JPEGImages", item) for item in jpegimages]
        
        annotations = [xml_parse(item, self.label_map) for item in annotations]
        self.all_labels =  list(zip(jpegimages, annotations))
        utils.mkparents(cache_file)
        torch.save(self.all_labels, cache_file)

    def load_VOC(self, cache_file):
        self.all_labels = torch.load(cache_file)

    def __getitem__(self, index):
        image, annotations = self.all_labels[index]
        image = cv2.imread(image).transpose(2, 0, 1)
        return image, annotations



if __name__ == '__main__':
    train_root = "/datav/MyLesson/Dataset/VOC2007/VOCdevkitTrain/VOC2007"
    test_root  = "/datav/MyLesson/Dataset/VOC2007/VOCdevkitTest/VOC2007"
    # train_set = VOCDataset(train_root)
    
    test_set = VOCDataset(test_root)
    image, annotations = test_set[0]
    print(image.shape)
    print(annotations)
    