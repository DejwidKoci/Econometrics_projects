import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
from sklearn.cluster import AgglomerativeClustering

# loading data from an Excel sheet
single = pd.read_excel('data.xlsx', sheet_name = "Single 2017", index_col = 0 )


# data normalisation
single_norm = (single - single.mean()) / single.std()


# determination of the distance matrix
dist_matrix_single = linkage(single_norm, 'ward')


# dendogram generation
plt.figure(figsize=(10, 7))
plt.title("Metoda Warda dla grupy singlów dla 2017 roku")
dend_single = dendrogram(dist_matrix_single, labels = single.index, orientation = 'right')

# show results
plt.show()

# Determination of the number of clusters
k = 3

# Cluster designation
clustering = AgglomerativeClustering(n_clusters=k, affinity='euclidean', linkage='ward')
clusters = clustering.fit_predict(single)

# Determination of the most important variables for each cluster
for i in range(k):
    print('Cluster {}:'.format(i+1))
    cluster_vars = single.loc[clusters == i]
    cluster_mean = cluster_vars.mean()
    cluster_mean = cluster_mean.sort_values(ascending=False)
    print(cluster_mean.head(2)) # display of the 2 most important variables for the cluster