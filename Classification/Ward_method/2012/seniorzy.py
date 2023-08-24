import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
from sklearn.cluster import AgglomerativeClustering

# loading data from an Excel sheet
seniorzy = pd.read_excel('data.xlsx', sheet_name = "Seniorzy 2012", index_col = 0 )


# data normalisation
seniorzy_norm = (seniorzy - seniorzy.mean()) / seniorzy.std()


# determination of the distance matrix
dist_matrix_seniorzy = linkage(seniorzy_norm, 'ward')


# dendogram generation
plt.figure(figsize=(10, 7))
plt.title("Metoda Warda dla grupy seniorów dla 2012 roku")
dend_seniorzy = dendrogram(dist_matrix_seniorzy, labels = seniorzy.index, orientation = 'right')

# show results
plt.show()

# Determination of the number of clusters
k = 4

# Cluster designation
clustering = AgglomerativeClustering(n_clusters=k, affinity='euclidean', linkage='ward')
clusters = clustering.fit_predict(seniorzy)

# Determination of the most important variables for each cluster
for i in range(k):
    print('Cluster {}:'.format(i+1))
    cluster_vars = seniorzy.loc[clusters == i]
    cluster_mean = cluster_vars.mean()
    cluster_mean = cluster_mean.sort_values(ascending=False)
    print(cluster_mean.head(2)) # display of the 2 most important variables for the cluster