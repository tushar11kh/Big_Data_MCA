import seaborn as sns
import pandas as pd

df = pd.read_csv('https://github.com/AnjulaMehto/MCA/blob/main/company_sales_data.csv?raw=true')
df['total_profit'] = df.iloc[:, 1:].sum(axis=1)
sns.lineplot(x=df.index, y='total_profit', data=df)

sns.lineplot(data=df.iloc[:, :-2])
df.iloc[:, :-2].plot(kind='bar')

import plotly.express as px

fig = px.scatter(df, x='month_number', y='total_profit')
fig.show()

fig = px.bar(df, x='month_number', y='total_profit')
fig.show()

fig = px.histogram(df, x='total_profit')
fig.show()
