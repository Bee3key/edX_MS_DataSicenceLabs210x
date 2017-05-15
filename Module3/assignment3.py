import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
# .. your code here ..
wheat_df = pd.read_csv("/home/dj/PycharmProjects/ML_DAT201x_MS/DAT210x/Module3/Datasets/wheat.data",
                       index_col=0, sep=',')
fig = plt.figure()
fig2 = plt.figure()

#
# TODO: Create a new 3D subplot using fig. Then use the
# subplot to graph a 3D scatter plot using the area,
# perimeter and asymmetry features. Be sure to use the
# optional display parameter c='red', and also label your
# axes
# 
# .. your code here ..
freedi1 = fig.add_subplot(111, projection='3d')

freedi1.set_xlabel('area')
freedi1.set_ylabel('perimeter')
freedi1.set_zlabel('asymmetry')

freedi1.scatter(wheat_df.area, wheat_df.perimeter, wheat_df.asymmetry, c='red', marker='.')


#
# TODO: Create a new 3D subplot using fig. Then use the
# subplot to graph a 3D scatter plot using the width,
# groove and length features. Be sure to use the
# optional display parameter c='green', and also label your
# axes
# 
# .. your code here ..


freedi2 = fig2.add_subplot(111, projection='3d')

freedi2.set_xlabel('width')
freedi2.set_ylabel('groove')
freedi2.set_zlabel('length')

freedi2.scatter(wheat_df.width, wheat_df.groove, wheat_df.length, c='green', marker='.')

plt.show()


