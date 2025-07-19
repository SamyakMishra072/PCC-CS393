# Write a script in Python for Normal Data Point clustering.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
n_samples = 300
n_features = 2
n_clusters = 3
X, _ = make_blobs(n_samples=n_samples, centers=n_clusters, n_features=n_features, cluster_std=1.0, random_state=42)
kmeans = KMeans(n_clusters=n_clusters)
kmeans.fit(X)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=200, linewidths=3, color='r', label='Centroids')
plt.legend()
plt.title('K-Means Clustering')
plt.show()
