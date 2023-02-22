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





def plotter(data, original):
    
    for i in range(len(data)):
        
        fig = plt.figure(figsize=(12, 10), dpi = 100)
        
        fig.suptitle("Cluster "+str(i+1), fontsize=20)
    
        rows = len(data[i])
        columns = 2
        
        for j in range(len(data[i])):
            
            fig.add_subplot(rows,columns, j+1)
            
            plt.imshow(original[data[i][j]], aspect = "equal", cmap = "gray")
            plt.axis('off')
            plt.title("Sample Number = "+str(data[i][j]))
        
        plt.tight_layout()
        