import pandas as pd
import os


path = os.path.join('/home', 'dj', 'PycharmProjects', 'ML_DAT201x_MS', 'DAT210x', 'Module2', 'Datasets', 'tutorial.csv')
# TODO: Load up the 'tutorial.csv' dataset
#
# .. your code here ..

df = pd.read_csv(path, sep=',')
print "df raw\n"
print df

print "\n df describe\n"
print df.describe()




# TODO: Print the results of the .describe() method
#
# .. your code here ..



# TODO: Figure out which indexing method you need to
# use in order to index your dataframe with: [2:4,'col3']
# And print the results
#
# .. your code here ..
print "\n df 2 -4 col3 \n"
print df.loc[2:4, 'col3']

