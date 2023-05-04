import os
import torch
import time
import rewriteutils


class VOCDataset:
    def __init__(self, root, overwrite=False):
        self.root = root
        self.overwrite = overwrite
        self.all_labels = []
        self.label_map = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
        cache_name = rewriteutils.get_md5(root)
        cache_file = f"runs/dataset_cache/{cache_name}"
        self.initialize_VOC(cache_file)

    def initialize_VOC(self, cache_file):
        if self.overwrite:
            self.build_VOC(cache_file)
        else:
            if os.path.exists(cache_file):
                self.load_VOC(cache_file)
            else:
                self.build_VOC(cache_file)

    def build_VOC(self, cache_file):
        annotations = os.listdir(os.path.join(self.root, "Annotations"))
        jpegimages  = [item[:-3] + 'jpg' for item in annotations]

        annotations = [os.path.join(self.root, "Annotations", item) for item in annotations]
        jpegimages  = [os.path.join(self.root, "JPEGImages", item) for item in jpegimages]

        annotations = [rewriteutils.xml_parse(item, self.label_map) for item in annotations]
        self.all_labels = list(zip(jpegimages, annotations))
        self.all_labels[0]
        rewriteutils.mkparents(cache_file)
        torch.save(self.all_labels, cache_file)

    def load_VOC(self, cache_file):
        self.all_labels = torch.load(cache_file)

    def __getitem__(self, index):
        return self.all_labels[index]



if __name__ == "__main__":
    train_root = "/datav/MyLesson/Dataset/VOC2007/VOCdevkitTrain/VOC2007"
    test_root  = "/datav/MyLesson/Dataset/VOC2007/VOCdevkitTest/VOC2007"
    
    # start = time.time()
    test_set = VOCDataset(test_root)
    print(test_set[0])
    # end = time.time()
    # print("Time Cost: ", end - start)