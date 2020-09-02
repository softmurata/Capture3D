import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage import io

dataset_dir = '../rgbd_dataset/RGBD/Nami1/'
rgb_dir = dataset_dir + 'rgb/'
depth_dir = dataset_dir + 'depth/'
target_number = 30

rgb = io.imread(rgb_dir + '{}.png'.format(target_number))
depth = io.imread(depth_dir + '{}.png'.format(target_number))

maxdepth = 370
good = depth < maxdepth

rgb0, rgb1, rgb2 = [], [], []
for h in range(rgb.shape[0]):
    u0, u1, u2 = [], [], []
    for w in range(rgb.shape[1]):
        if good[h, w] == True:
            u0.append(rgb[h, w, 0])
            u1.append(rgb[h, w, 1])
            u2.append(rgb[h, w, 2])
        else:
            u0.append(0)
            u1.append(0)
            u2.append(255)
    rgb0.append(u0)
    rgb1.append(u1)
    rgb2.append(u2)

rgb[:, :, 0] = rgb0
rgb[:, :, 1] = rgb1
rgb[:, :, 2] = rgb2

plt.imshow(rgb)
plt.show()


