import pandas as pd

from scipy import misc
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import matplotlib.pyplot as plt
import os
import random, math
from sklearn import manifold

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')


#
# TODO: Start by creating a regular old, plain, "vanilla"
# python list. You can call it 'samples'.
#
# .. your code here ..
vanilla_samples = []
ALOI_path = "/home/dj/PycharmProjects/ML_DAT201x_MS/Practice/Module4/Datasets/ALOI"
img_folder32 = os.path.join(ALOI_path, "32")
img_folder32i = os.path.join(ALOI_path, "32i")
#
# TODO: Write a for-loop that iterates over the images in the
# Module4/Datasets/ALOI/32/ folder, appending each of them to
# your list. Each .PNG image should first be loaded into a
# temporary NDArray, just as shown in the Feature
# Representation reading.
#
# Optional: Resample the image down by a factor of two if you
# have a slower computer. You can also convert the image from
# 0-255  to  0.0-1.0  if you'd like, but that will have no
# effect on the algorithm's results.
#
# .. your code here .. 
for png_file in os.listdir(img_folder32):
    path_tmp = os.path.join(img_folder32, png_file)
    img = misc.imread(path_tmp).reshape(-1)
    vanilla_samples.append(img)


#
# TODO: Once you're done answering the first three questions,
# right before you converted your list to a dataframe, add in
# additional code which also appends to your list the images
# in the Module4/Datasets/ALOI/32_i directory. Re-run your
# assignment and answer the final question below.
#
# .. your code here .. 
for png_file in os.listdir(img_folder32i):
    path_tmp = os.path.join(img_folder32i, png_file)
    img = misc.imread(path_tmp).reshape(-1)
    vanilla_samples.append(img)

colors = ['b']*72 + ['r']*12  # These magic numbers are 72 files in img_folder32 and 12 files in img_folder32i

#
# TODO: Convert the list to a dataframe
#
# .. your code here .. 

df = pd.DataFrame(vanilla_samples)


#
# TODO: Implement Isomap here. Reduce the dataframe df down
# to three components, using K=6 for your neighborhood size
#
# .. your code here .. 

iso_man = manifold.Isomap(n_neighbors=6, n_components=3)
transf = iso_man.fit_transform(df)

#
# TODO: Create a 2D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker. Graph the first two
# isomap components
#
# .. your code here ..


def plot2d(transformed, title, x, y):

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title(title)
    ax.set_xlabel('Component: {0}'.format(x))
    ax.set_ylabel('Component: {0}'.format(y))
    # It also plots the full scatter:
    ax.scatter(transformed[:, x], transformed[:, y], marker='.', alpha=0.7, c=colors)

#
# TODO: Create a 3D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker:
#
# .. your code here ..


def plot3d(transformed, title, x, y, z):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title(title)
    ax.set_xlabel('Component: {0}'.format(x))
    ax.set_ylabel('Component: {0}'.format(y))
    ax.set_zlabel('Component: {0}'.format(z))
    # It also plots the full scatter:
    ax.scatter(transformed[:, x], transformed[:, y], transformed[:, z], marker='.', alpha=0.7, c=colors)

plot2d(transf, "Isomap data 2D", 0, 1)
plot3d(transf, "Isomap data 3D", 0, 1, 2)

plt.show()

