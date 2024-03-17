import pandas as pd
df = pd.read_csv('C:\workspace\python\PyrePython\\renkode.csv')
# fjerne en rad fra csv
df = df.drop(df.index[2])
print(df)


