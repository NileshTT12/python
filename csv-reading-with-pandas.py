import pandas as pd
df =pd.read_csv('/Users/nthombre/Desktop/fiber.csv')
#print(df.head(10))
#print(df.columns)
df.columns=['Source', 'Severity', 'Description', 'Status', 'Failure Source',
       'Last Updated', 'Received', 'Device Timestamp', 'Owner', 'Category',
       'Condition', 'Location', 'Service Affecting', 'Satellite Id']
print(df[df['Condition'] == 'AUTORESET'])
