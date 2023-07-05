import cv2
import os
import re

image_folder = '/home/nerf/datav/Dataset/vMAP/apt_2/isdf/02/rgb'
video_name = 'iSDF-apt2.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
images.sort(key=lambda x: int(re.search(r'\d+', x).group()))

frame = cv2.imread(os.path.join(image_folder, images[0]))
frameSize = (frame.shape[1], frame.shape[0])


# video = cv2.VideoWriter(video_name, 0, 1, (width,height))
video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), 30, frameSize)

for i, image in enumerate(images):
    video.write(cv2.imread(os.path.join(image_folder, image)))
    if i % 100 == 0:
        print(f"The {i}/{len(images)} is done.")

video.release()