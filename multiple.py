import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt

df_brick = pd.read_csv('Metrics/metrics_brick.csv')
df_db = pd.read_csv('Metrics/metrics_db.csv')
df_haystack = pd.read_csv('Metrics/metrics_haystack.csv')
df_recore = pd.read_csv('Metrics/metrics_recore.csv')

df_brick = df_brick[(df_brick.metric_type == "map_value") | (df_brick.metric_type == "list_value")]
df_db = df_db[(df_db.metric_type == "map_value") | (df_db.metric_type == "list_value")]
df_haystack = df_haystack[(df_haystack.metric_type == "map_value") | (df_haystack.metric_type == "list_value")]
df_recore = df_recore[(df_recore.metric_type == "map_value") | (df_recore.metric_type == "list_value")]

df_brick = df_brick[['metric', 'metric_value']]
df_brick.set_index('metric', inplace=True)
df_brick.rename(columns={'metric_value':'metric_value_brick'}, inplace=True)
df_brick = df_brick.reset_index()
print(tabulate(df_brick, headers='keys'))

df_db = df_db[['metric', 'metric_value']]
df_db.set_index('metric', inplace=True)
df_db.rename(columns={'metric_value':'metric_value_db'}, inplace=True)
df_db = df_db.reset_index()

df_haystack = df_haystack[['metric', 'metric_value']]
df_haystack.set_index('metric', inplace=True)
df_haystack.rename(columns={'metric_value':'metric_value_haystack'}, inplace=True)
df_haystack = df_haystack.reset_index()

df_recore = df_recore[['metric', 'metric_value']]
df_recore.set_index('metric', inplace=True)
df_recore.rename(columns={'metric_value':'metric_value_core'}, inplace=True)
df_recore = df_recore.reset_index()

df_brick = df_brick[df_brick.metric == "axiom_type_count"]
df_brick[['axiom_type', 'brick']] = df_brick['metric_value_brick'].str.split(' ', expand=True)
df_brick = df_brick[['axiom_type', 'brick']]
df_brick.set_index('axiom_type', inplace=True)
print(tabulate(df_brick, headers='keys'))
# df_brick['brick']=df_brick['brick'].astype(float)
# df_brick = df_brick.sort_values(by=['brick'], ascending=False).head(5)
# df_brick.groupby(['axiom_type']).sum().plot(kind='pie', y='brick', autopct='%1.2f%%', legend=None)
# plt.show()

df_db = df_db[df_db.metric == "axiom_type_count"]
df_db[['axiom_type', 'db']] = df_db['metric_value_db'].str.split(' ', expand=True)
df_db = df_db[['axiom_type', 'db']]
df_db.set_index('axiom_type', inplace=True)
print(tabulate(df_db, headers='keys'))
# df_db['db']=df_db['db'].astype(float)
# df_db = df_db.sort_values(by=['db'], ascending=False).head(4)
# df_db.groupby(['axiom_type']).sum().plot(kind='pie', y='db', autopct='%1.2f%%', legend=None)
# plt.show()

df_haystack = df_haystack[df_haystack.metric == "axiom_type_count"]
df_haystack[['axiom_type', 'haystack']] = df_haystack['metric_value_haystack'].str.split(' ', expand=True)
df_haystack = df_haystack[['axiom_type', 'haystack']]
df_haystack.set_index('axiom_type', inplace=True)
print(tabulate(df_haystack, headers='keys'))
# df_haystack['haystack']=df_haystack['haystack'].astype(float)
# df_haystack = df_haystack.sort_values(by=['haystack'], ascending=False).head(5)
# df_haystack.groupby(['axiom_type']).sum().plot(kind='pie', y='haystack', autopct='%1.2f%%', legend=None)
# plt.show()

df_recore = df_recore[df_recore.metric == "axiom_type_count"]
df_recore[['axiom_type', 'core']] = df_recore['metric_value_core'].str.split(' ', expand=True)
df_recore = df_recore[['axiom_type', 'core']]
df_recore.set_index('axiom_type', inplace=True)
print(tabulate(df_recore, headers='keys'))
df_recore['core']=df_recore['core'].astype(float)
df_recore = df_recore.sort_values(by=['core'], ascending=False).head(5)
df_recore.groupby(['axiom_type']).sum().plot(kind='pie', y='core', autopct='%1.2f%%', legend=None)
plt.show()

# merged_df = pd.concat([df_brick, df_db, df_haystack, df_recore], axis=1)
# merged_df['brick']=merged_df['brick'].astype(float)
# merged_df['db']=merged_df['db'].astype(float)
# merged_df['haystack']=merged_df['haystack'].astype(float)
# merged_df['core']=merged_df['core'].astype(float)
# merged_df = merged_df.fillna(0)
# merged_df = merged_df.sort_values(by=['brick'], ascending=False)
# print(tabulate(merged_df, headers='keys'))
#
# ax = merged_df.plot(kind="bar",figsize=(20,20))
# for container in ax.containers:
#     ax.bar_label(container)
# plt.show()