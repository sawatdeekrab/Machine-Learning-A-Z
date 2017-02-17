# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 19:33:56 2017

@author: Nott
"""
#%reset -f

#K-Mean

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Mall_customers.csv')
X = dataset.iloc[:, [3,4]].values

#Using Elbow medthod to optimizing number of cluster
from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i,
                    init = 'k-means++',
                    max_iter = 300,
                    n_init = 10,
                    random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('Elbow medthod')
plt.xlabel('Number of Cluster')
plt.ylabel('WCSS')
plt.show()

#Apply K-Means to the mall dataset
kmeans = KMeans(n_clusters=5,
                init = 'k-means++',
                max_iter = 300,
                n_init = 10,
                random_state=0)
y_kmeans = kmeans.fit_predict(X)

#Visualising the Cluster
plt.scatter(X[y_kmeans==0,0],X[y_kmeans==0,1], s = 10,c = 'red', label = 'Careful')
plt.scatter(X[y_kmeans==1,0],X[y_kmeans==1,1], s = 10,c = 'blue', label = 'Standard')
plt.scatter(X[y_kmeans==2,0],X[y_kmeans==2,1], s = 10,c = 'green', label = 'Target')
plt.scatter(X[y_kmeans==3,0],X[y_kmeans==3,1], s = 10,c = 'cyan', label = 'Careless')
plt.scatter(X[y_kmeans==4,0],X[y_kmeans==4,1], s = 10,c = 'magenta', label = 'Sensible')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 10, c = 'yellow', label = 'Centroids')
plt.title('Cluster of Clients')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1 - 100)')
plt.legend()
plt.show()