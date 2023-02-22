# This Function performs PLotting of the Generated Clusters

import seaborn as sns
import matplotlib.pyplot as plt 
from matplotlib.pyplot import figure
from skimage.io import imread, imshow

# Presets for Plots 
sns.set(style="darkgrid")
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 100


# The function takes 2 fields of input, 
# 1. Data = The Results of Clustering in the format of A dictionary with Lists
# 2. Original = the original data as attained from Reader.py

def plotter(data, original):
    
    # Generation of Plot areas with Appropriate Cluster numbering
    for i in range(len(data)):
        
        fig = plt.figure(figsize=(12, 10), dpi = 100) # Size & DPI of Plot
        
        fig.suptitle("Cluster "+str(i+1), fontsize=20) # Cluster Numbering
    
        # Orientation of the Plots within the Figure
        rows = len(data[i]) 
        columns = 2
        
        # Generation of plots
        for j in range(len(data[i])):
            
            fig.add_subplot(rows,columns, j+1) # Adding Plots within 
            
            plt.imshow(original[data[i][j]], aspect = "equal", cmap = "gray")
            plt.axis('off')
            plt.title("Sample Number = "+str(data[i][j]))
        
        plt.tight_layout()
