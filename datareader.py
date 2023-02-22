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







# This Function is used to read the Data from the Folder Path; where the Image Data is stored. Since there are multiple
# files to be read, hence the Path is chosen. 


def reader(FILE_PATH):
    
    # Change Directory of the Kernel
    os.chdir(FILE_PATH) #os.getcwd()
    

    file_paths = [] # To Store Paths of each file within the Folder  
    
    
    for file in os.listdir(): # Check if all files are TXT or not. Read only TXT files
        if file.endswith(".txt"):
            file_paths.append(f"{FILE_PATH}\{file}")
    
    
    a = {}  # A Dictionary to store the Paths with a ID Number
    k = 0
    for ele in file_paths:
        a[k] = ele
        k+=1
    
        
    b = {}   # A Dictionary to store the Data Stored from the Files
    for i in range(len(a)):
        b[i] = pd.read_csv(a[i], delimiter = "\t", header = None)
    
    
    D1, D2 = b[0].shape # Takes the Dimension of the first file. (It is assumed that the Files will have same shape for now)
    
    X = np.random.rand(len(b), D1*D2) # What happens if Data of Different Dimensions are give...? Something to be done in the future.
    
    # Creating the numpy format of the data to be fed into the Clustering Algorithm
    
    for j in range(len(X)):
        X[j] = b[j].to_numpy().reshape(1,-1)
    
    del a#, b 
    
    # returns the RESHAPED Data to be fed to the Clustering Algorithm & the original Data within the File for reference 
    
    return X,b