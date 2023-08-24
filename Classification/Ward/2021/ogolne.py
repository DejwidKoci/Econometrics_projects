import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
from sklearn.cluster import AgglomerativeClustering

# loading data from an Excel sheet
df = pd.read_excel('data.xlsx', index_col = 0, sheet_name = '2021')

# data normalisation
df_norm = (df - df.mean()) / df.std()

# determination of the distance matrix
dist_matrix = linkage(df_norm, 'ward')

# dendogram generation
plt.figure(figsize=(10, 7))
plt.title("Metoda Warda dla grupy ogólnej dla 2021 roku")
dend = dendrogram(dist_matrix, labels = df.index, orientation='right')

# show results
plt.show()

# Determination of the number of clusters
k = 5

# Cluster designation
clustering = AgglomerativeClustering(n_clusters=k, affinity='euclidean', linkage='ward')
clusters = clustering.fit_predict(df)

# Determination of the most important variables for each cluster
for i in range(k):
    print('Cluster {}:'.format(i+1))
    cluster_vars = df.loc[clusters == i]
    cluster_mean = cluster_vars.mean()
    cluster_mean = cluster_mean.sort_values(ascending=False)
    print(cluster_mean.head(2)) # display of the 2 most important variables for the cluster