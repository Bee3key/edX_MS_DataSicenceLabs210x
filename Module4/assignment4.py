import pandas as pd
import numpy as np
import scipy.io
import random, math


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn import manifold


def Plot2D(T, title, x, y, num_to_plot=40):
    # This method picks a bunch of random samples (images in your case)
    # to plot onto the chart:
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title(title)
    ax.set_xlabel('Component: {0}'.format(x))
    ax.set_ylabel('Component: {0}'.format(y))
    x_size = (max(T[:,x]) - min(T[:,x])) * 0.08
    y_size = (max(T[:,y]) - min(T[:,y])) * 0.08
    for i in range(num_to_plot):
        img_num = int(random.random() * num_images)
        x0, y0 = T[img_num,x]-x_size/2., T[img_num,y]-y_size/2.
        x1, y1 = T[img_num,x]+x_size/2., T[img_num,y]+y_size/2.
        img = df.iloc[img_num,:].reshape(num_pixels, num_pixels)
        ax.imshow(img, aspect='auto', cmap=plt.cm.gray, interpolation='nearest', zorder=100000, extent=(x0, x1, y0, y1))

    # It also plots the full scatter:
    ax.scatter(T[:,x],T[:,y], marker='.',alpha=0.7)



# A .MAT file is a .MATLAB file. The faces dataset could have came
# in through .png images, but we'll show you how to do that in
# anither lab. For now, you'll see how to import .mats:
mat = scipy.io.loadmat('Datasets/face_data.mat')
df = pd.DataFrame(mat['images']).T
num_images, num_pixels = df.shape
num_pixels = int(math.sqrt(num_pixels))

# Rotate the pictures, so we don't have to crane our necks:
for item in range(num_images):
    df.loc[item, :] = df.loc[item, :].reshape(num_pixels, num_pixels).T.reshape(-1)


#
# TODO: Implement PCA here. Reduce the dataframe df down
# to THREE components. Once you've done that, call Plot2D.
#
# The format is: Plot2D(T, title, x, y, num_to_plot=40):
# T is your transformed data, NDArray.
# title is your chart title
# x is the principal component you want displayed on the x-axis, Can be 0 or 1
# y is the principal component you want displayed on the y-axis, Can be 1 or 2
#
# .. your code here ..
pca = PCA(n_components=3)
pca_transform = pca.fit_transform(df)
Plot2D(pca_transform, "Data is transformed using PCA. 2D", 1, 2)


#
# TODO: Implement Isomap here. Reduce the dataframe df down
# to THREE components. Once you've done that, call Plot2D using
# the first two components.
#
# .. your code here ..
isomap = manifold.Isomap(n_neighbors=3, n_components=3)
iso_transform = isomap.fit_transform(df)
Plot2D(iso_transform, "Data is transformed using Isomap. 2D", 1, 2)

#
# TODO: If you're up for a challenge, draw your dataframes in 3D
# Even if you're not, just do it anyway.
#
# .. your code here ..
# We just take Plot2D function add one more dimension, and also make sure
# that code be more readable and PEP don't cry more


def plot3D(transform, title, x, y, z, num_to_plot=40):

    # This method picks a bunch of random samples (images in your case)
    # to plot onto the chart:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection= '3d')
    ax.set_title(title)
    ax.set_xlabel('Component: {0}'.format(x))
    ax.set_ylabel('Component: {0}'.format(y))
    ax.set_ylabel('Component: {0}'.format(z)) # added z

    x_size = (max(transform[:, x]) - min(transform[:, x])) * 0.08
    y_size = (max(transform[:, y]) - min(transform[:, y])) * 0.08
    z_size = (max(transform[:, y]) - min(transform[:, z])) * 0.08  # added

    for i in range(num_to_plot):
        img_num = int(random.random() * num_images)
        x0, y0, z0 = transform[img_num, x] - x_size / 2., transform[img_num, y] - y_size / 2.,\
                     transform[img_num, z] - z_size / 2.
        x1, y1, z1 = transform[img_num, x] + x_size / 2., transform[img_num, y] + y_size / 2.,\
                     transform[img_num, z] - z_size / 2.

        img = df.iloc[img_num, :].reshape(num_pixels, num_pixels)
        ax.imshow(img, aspect='auto', cmap=plt.cm.gray, interpolation='nearest',
                  zorder=100000, extent=(x0, x1, y0, y1))

    # It also plots the full scatter:
    ax.scatter(transform[:, x], transform[:, y], transform[:, z], marker='.', alpha=0.7)

plot3D(pca_transform, "Data is transformed using PCA. 3D", 0, 1, 2)
plot3D(iso_transform, "Data is transformed using Isomap. 3D", 0, 1, 2)
plt.show()
