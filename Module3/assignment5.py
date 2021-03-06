import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

from pandas.tools.plotting import andrews_curves

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

#
# TODO: Drop the 'id' feature, if you included it as a feature
# (Hint: You shouldn't have)
# Also get rid of the 'area' and 'perimeter' features
# 
# .. your code here ..
#wheat_df = wheat_df.drop(labels=['area', 'perimeter'], axis=1)

#
# TODO: Plot a parallel coordinates chart grouped by
# the 'wheat_type' feature. Be sure to set the optional
# display parameter alpha to 0.4
# 
# .. your code here ..
plt.figure()

#df = pd.DataFrame(wheat_df, columns=wheat_df.wheat_types)

#df['wheat_types'] = [df.wheat_types[i] for i in wheat_df.wheat_type]

andrews_curves(wheat_df, 'wheat_type', alpha=0.4)


plt.show()


