import pandas as pd
import os

path = os.path.join('/home', 'dj', 'PycharmProjects', 'ML_DAT201x_MS', 'DAT210x', 'Module2', 'Datasets', 'servo.data')

collumn_names = ['motor', 'screw', 'pgain', 'vgain', 'class']

# TODO: Load up the dataset
# Ensuring you set the appropriate header column names
#
# .. your code here ..

df = pd.read_csv(path, sep=',', names=collumn_names, float_precision='high')



# TODO: Create a slice that contains all entries
# having a vgain equal to 5. Then print the 
# length of (# of samples in) that slice:
#
# .. your code here ..
print len(df[df.vgain == 5])

# TODO: Create a slice that contains all entries
# having a motor equal to E and screw equal
# to E. Then print the length of (# of
# samples in) that slice:
#
# .. your code here ..
print len(df[(df.motor == 'E') & (df.screw == 'E')])



# TODO: Create a slice that contains all entries
# having a pgain equal to 4. Use one of the
# various methods of finding the mean vgain
# value for the samples in that slice. Once
# you've found it, print it:
#
# .. your code here ..

print df[df.pgain == 4].describe()



# TODO: (Bonus) See what happens when you run
# the .dtypes method on your dataframe!
print df.dtypes



