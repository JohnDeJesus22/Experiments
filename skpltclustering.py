# Absenteeism Clustering

# load libraries
import pandas as pd
import numpy as np
import scikitplot as skplt
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.cluster import MeanShift
import os

# load data
os.chdir('D:\\')
absentees=pd.read_csv('Absenteeism_at_work.csv',sep=';')

# correlation heatmap
corr = absentees.corr()
sns.heatmap(corr, annot = True, vmin = -1, vmadata_to_cluster = 1)
plt.show()

# data to cluster
data_to_cluster = absentees.loc[:,['Transportation expense','Distance from Residence to Work']].values

# clustering
kmeans = KMeans(random_state = 1)
clusters = kmeans.fit_predict(data_to_cluster)

# plot elbow curve
skplt.cluster.plot_elbow_curve(clf=kmeans,X= data_to_cluster, cluster_ranges=range(1, 30))
plt.show()

# plot silhouette plot
skplt.metrics.plot_silhouette(data_to_cluster,clusters)
plt.show()

# visualize clusters
plt.scatter(data_to_cluster[clusters==0,0],data_to_cluster[clusters==0,1],s=100,c='red')
plt.scatter(data_to_cluster[clusters==1,0],data_to_cluster[clusters==1,1],s=100,c='blue')
plt.scatter(data_to_cluster[clusters==2,0],data_to_cluster[clusters==2,1],s=100,c='green')
plt.scatter(data_to_cluster[clusters==3,0],data_to_cluster[clusters==3,1],s=100,c='brown')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=300,c='yellow',label='Centroids')
plt.title('Cluster of Clients')
plt.xlabel('Transportation Expense')
plt.ylabel('Distance from Work')
plt.legend()
plt.show()
