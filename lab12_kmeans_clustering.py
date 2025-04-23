from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from kneed import KneeLocator

features, true_labels = make_blobs(n_samples=200, centers=3, cluster_std=2.75, random_state=42)
plt.scatter(features[:, 0], features[:, 1], s=50)
plt.show()

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)
plt.scatter(scaled_features[:, 0], scaled_features[:, 1], s=50)
plt.show()

kmeans = KMeans(init="random", n_clusters=3, n_init=10, max_iter=300, random_state=42)
kmeans.fit(scaled_features)
y_pred = kmeans.predict(scaled_features)

plt.scatter(scaled_features[:, 0], scaled_features[:, 1], c=y_pred, s=50, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
plt.show()

kmeans_kwargs = {"init": "random", "n_init": 10, "max_iter": 300, "random_state": 42}
sse = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, **kmeans_kwargs)
    kmeans.fit(scaled_features)
    sse.append(kmeans.inertia_)

plt.style.use("fivethirtyeight")
plt.plot(range(1, 11), sse)
plt.xticks(range(1, 11))
plt.xlabel("Number of Clusters")
plt.ylabel("SSE")
plt.show()

kl = KneeLocator(range(1, 11), sse, curve="convex", direction="decreasing")
print("Optimal number of clusters:", kl.elbow)