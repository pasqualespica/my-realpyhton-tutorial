
# Parsing CSV Files With the pandas Library
#  pip install panda


import pandas
df = pandas.read_csv('hrdata.csv')
print(type(df), df, sep="\n")

print(df["Hire Date"][2], type(df["Hire Date"][2]))

# Let’s tackle these issues one at a time. To use a different column as 
# the DataFrame index, add the index_col optional parameter:
df = pandas.read_csv('hrdata.csv', index_col='Name')
print(df)

# Next, let’s fix the data type of the Hire Date field. 
# You can force pandas to read data as a date with the parse_dates 
# optional parameter, which is defined as a list of column names 
# to treat as dates:

df = pandas.read_csv('hrdata.csv', index_col='Name', parse_dates=['Hire Date'])
print(df)
print(df["Hire Date"][2], type(df["Hire Date"][2]))

