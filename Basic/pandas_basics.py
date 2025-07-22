import pandas as pd
df = pd.read_csv('/Users/nthombre/Desktop/Test2.csv')
print(df)
#print(df.columns)
df.columns=['sepal_length','sepal_width','petal_length','petal_width','species']
#print(df[df['petal_length']>6.0])
#df.column=['sepal_length,sepal_width,petal_length,petal_width,species']
#print(df.head())
#print(df[['sepal_length','species']])
#print(df.iloc[0])
#print(df.loc[0])
print(df.values)
print(df[['sepal_length','sepal_width']].values)