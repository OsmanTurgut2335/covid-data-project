# -- coding: utf-8 --
"""
Created on Wed Jan  5 14:29:22 2022

@author: Osman
"""
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns
sns.set()
from sklearn.cluster import KMeans
from sklearn import cluster
pd.options.mode.chained_assignment = None  # default='warn




data={  'Perakende':[-38.9538,-55.1591,-49.7867,-25.911,-16.201,-16.201,-15.201,-13.232,-17.455,-13.301],'Market':[-10.0442,-18.8975,-10.0347,6.65749,8.06773,8.76556,11.4938,9.135,11.231,8.0723],
      'Park':[-23.1451,-36.0649,-25.1772,13.2504,29.5799,30.432,-28.343,13.2123,23.565,5.2343],'Vaka':[541.35,3313.14,1179.77,1248.31,1021.95,1476.7,1585.73,2118.3,1223.81,1699.95]
        
      }

df = pd.DataFrame(data)

'''
numClusters = [1,2,3,4,5,6,7,8,9,10]
SSE = []
for k in numClusters:
    k_means = cluster.KMeans(n_clusters=k)
    k_means.fit(df)
    SSE.append(k_means.inertia_)
    
 

plt.plot(numClusters, SSE)
plt.xlabel('Number of Clusters')
plt.ylabel('SSE')
 '''
 
X = df[['Perakende','Market','Park','Vaka']].copy()
kmeans = KMeans(3)
kmeans.fit(X)

identified_clusters = kmeans.fit_predict(X)
identified_clusters

data_with_clusters = data.copy()
data_with_clusters['Clusters'] = identified_clusters 
#plt.scatter(data_with_clusters['Vaka'],data_with_clusters['Market'] ,c=data_with_clusters['Clusters'],cmap='rainbow')
plt.scatter(data_with_clusters['Vaka'],data_with_clusters['Perakende'] ,c=data_with_clusters['Clusters'],cmap='rainbow')
#plt.scatter(data_with_clusters['Vaka'],data_with_clusters['Park'] ,c=data_with_clusters['Clusters'],cmap='rainbow')