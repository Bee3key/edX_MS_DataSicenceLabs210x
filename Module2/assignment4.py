import pandas as pd
import csv


# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
#
# .. your code here ..

#df = pd.read_html('ESPN.html')

c_names = ['RK', 'PLAYER', 'TEAM', 'GP', 'G', 'A', 'PTS', '+/-', 'PIM',
           'PTS/G', 'SOG', 'PCT', 'GWG', 'G', 'A', 'G', 'A']
#'http://espn.go.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2'
df = pd.read_html('ESPN.html', skiprows=1)[0]

df.columns = c_names

df = df.drop(labels=['RK', ], axis=1)



df.GP = pd.to_numeric(df.GP, errors='coerce')
#df.G = pd.to_numeric(df.G, errors='coerce')
#df.A = pd.to_numeric(df.A, errors='coerce')
df.PTS = pd.to_numeric(df.PTS, errors='coerce')
df.PIM = pd.to_numeric(df.PIM, errors='coerce')
df.SOG = pd.to_numeric(df.SOG, errors='coerce')
df.PCT = pd.to_numeric(df.PCT, errors='coerce')
df.GWG = pd.to_numeric(df.GWG, errors='coerce')

df = df.dropna(axis=1, thresh=4)
df = df.dropna(axis=0)

print df.GP[15] + df.GP[16]
#print len(df.PCT.unique())

# TODO: Rename the columns so that they are similar to the
# column definitions provided to you on the website.
# Be careful and don't accidentially use any names twice.
#
# .. your code here ..


# TODO: Get rid of any row that has at least 4 NANs in it,
# e.g. that do not contain player points statistics
#
# .. your code here ..


# TODO: At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
#
# .. your code here ..


# TODO: Get rid of the 'RK' column
#
# .. your code here ..


# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
#
# .. your code here ..



# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric
#
# .. your code here ..



# TODO: Your dataframe is now ready! Use the appropriate 
# commands to answer the questions on the course lab page.
#
# .. your code here ..

