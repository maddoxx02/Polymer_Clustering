# https://towardsdatascience.com/density-based-clustering-dbscan-vs-hdbscan-39e02af990c7
# https://pypi.org/project/hdbscan/
# https://hdbscan.readthedocs.io/en/latest/basic_hdbscan.html 
# pip install hdbscan 
# conda install -c conda-forge hdbscan


import hdbscan
import numpy as np

def HDBSCAN_Cluster(input_data):

    clusterer = hdbscan.HDBSCAN(min_cluster_size = 2)

    clusterer.fit(input_data)

    # A Dictionary to Store the Cluster IDs & the Respective Data with IDs
    kk = {}
    temp = []

    # Creating the Key for the number of Clusters as mentioned
    for k in range(len(np.unique(clusterer.labels_))):
        kk[k] = []

    # Stores the Cluster ID's for Reference & Assignment 
    tt = list(kk.keys())

    # Assigning Data elements to their respective Clusters 
    for t in range(len(tt)):
        for i in range(len(clusterer.labels_)):
            if clusterer.labels_[i] == tt[t]:
                kk[t]+=[i]

    clusterer = hdbscan.RobustSingleLinkage(cut=0.125, k=3)
    cluster_labels = clusterer.fit_predict(input_data)

    hierarchy = clusterer.cluster_hierarchy_
    alt_labels = hierarchy.get_clusters(0.100, 5)
    hierarchy.plot()

    # Returning a Dictionary with The Number of Clusters and respective Elements within
    return kk

    