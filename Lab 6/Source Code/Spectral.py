import numpy as np
import matplotlib.pyplot as plt

from sklearn.feature_extraction import image
from sklearn.cluster import spectral_clustering

l = 100
x, y = np.indices((l, l))

cen1 = (28, 24)
cen2 = (40, 50)
cen3 = (67, 58)
cen4 = (24, 70)

radius1, radius2, radius3, radius4 = 16, 14, 15, 14

cir1 = (x - cen1[0]) ** 2 + (y - cen1[1]) ** 2 < radius1 ** 2
cir2 = (x - cen2[0]) ** 2 + (y - cen2[1]) ** 2 < radius2 ** 2
cir3 = (x - cen3[0]) ** 2 + (y - cen3[1]) ** 2 < radius3 ** 2
cir4 = (x - cen4[0]) ** 2 + (y - cen4[1]) ** 2 < radius4 ** 2


figure = cir1 + cir2 + cir3 + cir4


mask = figure.astype(bool)

img = figure.astype(float)
img += 1 + 0.2 * np.random.randn(*img.shape)


graph = image.img_to_graph(img, mask=mask)


graph.data = np.exp(-graph.data / graph.data.std())


labels = spectral_clustering(graph, n_clusters=4, eigen_solver='arpack')
label_im = -np.ones(mask.shape)
label_im[mask] = labels

plt.matshow(img)
plt.matshow(label_im)


img = cir1 + cir2
mask = img.astype(bool)
img = img.astype(float)

img += 1 + 0.2 * np.random.randn(*img.shape)

graph = image.img_to_graph(img, mask=mask)
graph.data = np.exp(-graph.data / graph.data.std())

labels = spectral_clustering(graph, n_clusters=2, eigen_solver='arpack')
label_im = -np.ones(mask.shape)
label_im[mask] = labels

plt.matshow(img)
plt.matshow(label_im)

plt.show()
