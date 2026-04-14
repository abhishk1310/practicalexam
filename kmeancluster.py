from sklearn.cluster import KMeans 
import numpy as np
arr = np.array([[1,3],[1,2],[1,4],[10,3],[10,2],[10,4]])
kmean = KMeans(n_clusters=2,random_state=0)
model = kmean.fit(arr)
a=kmean.cluster_centers_
b=kmean.labels_
print("Original Array:",arr)
print("Cluster Array:",a,b)