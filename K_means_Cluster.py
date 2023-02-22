import os
import math
import seaborn as sns
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt 
from matplotlib.pyplot import figure

# Presets for Plots 
sns.set(style="darkgrid")
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 100

import cv2
from skimage.io import imread, imshow
from skimage.color import rgb2hsv, rgb2gray, rgb2yuv
from skimage import color, exposure, transform
from skimage.exposure import equalize_hist

from sklearn.cluster import KMeans




def K_MEANS(input_data, cluster):
    
    Kmean = KMeans(n_clusters = cluster)#, n_init = 100)
    
    Kmean.fit(input_data)
    
    #return Kmean.labels_, cluster

    kk = {}
    temp = []

    for k in range(cluster):
        kk[k] = []

    tt = list(kk.keys())

    for t in range(len(tt)):
        for i in range(len(Kmean.labels_)):
            if Kmean.labels_[i] == tt[t]:            #print("for cluster ", t, " elements are =", i)
                kk[t]+=[i]

    return kk

    