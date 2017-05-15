import pandas as pd
import matplotlib.pyplot as plt


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
# .. your code here ..
wheat_df = pd.read_csv("/home/dj/PycharmProjects/ML_DAT201x_MS/DAT210x/Module3/Datasets/wheat.data",
                       index_col=0, sep=',')

#
# TODO: Drop the 'id' feature, if you included it as a feature
# (Hint: You shouldn't have)
# 
# .. your code here ..


#
# TODO: Compute the correlation matrix of your dataframe
# 
# .. your code here ..
corr = wheat_df.corr()

#
# TODO: Graph the correlation matrix using imshow or matshow
# 
# .. your code here ..
plt.matshow(corr, cmap=plt.cm.Blues, interpolation='nearest')
plt.colorbar()
tick_marks = [i for i in range(len(wheat_df.columns))]
plt.xticks(tick_marks, wheat_df.columns, rotation='vertical')
plt.yticks(tick_marks, wheat_df.columns)

plt.show()


plt.show()


