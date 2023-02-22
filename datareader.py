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


def reader(FILE_PATH):
    
    # Change Directory of the Kernel
    os.chdir(FILE_PATH) #os.getcwd()
    

    file_paths = [] # To Store Paths of each file    
    
    
    for file in os.listdir(): # Check if all files are TXT or not. Read only TXT files
        if file.endswith(".txt"):
            file_paths.append(f"{FILE_PATH}\{file}")
    
    
    a = {}
    k = 0
    for ele in file_paths:
        a[k] = ele
        k+=1
    
        
    b = {}
    for i in range(len(a)):
        b[i] = pd.read_csv(a[i], delimiter = "\t", header = None)
    
    
    D1, D2 = b[0].shape
    
    X = np.random.rand(len(b), D1*D2) # What happens if Data of Different Dimensions are give...?
    
    for j in range(len(X)):
        X[j] = b[j].to_numpy().reshape(1,-1)
    
    del a#, b 
    
    return X,b