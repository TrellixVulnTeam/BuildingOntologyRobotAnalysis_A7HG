import pandas as pd
from tabulate import tabulate

df_brick = pd.read_csv('metrics/metrics_brick.csv')
df_db = pd.read_csv('metrics/metrics_db.csv')
df_haystack = pd.read_csv('metrics/metrics_haystack.csv')
df_recore = pd.read_csv('metrics/metrics_recore.csv')

df_brick = df_brick[(df_brick.metric_type == "single_value")]
df_db = df_db[(df_db.metric_type == "single_value")]
df_haystack = df_haystack[(df_haystack.metric_type == "single_value")]
df_recore = df_recore[(df_recore.metric_type == "single_value")]

df_brick = df_brick[['metric', 'metric_value']]
df_brick.set_index('metric', inplace=True)
df_brick.rename(columns={'metric_value':'metric_value_brick'}, inplace=True)

df_db = df_db[['metric', 'metric_value']]
df_db.set_index('metric', inplace=True)
df_db.rename(columns={'metric_value':'metric_value_db'}, inplace=True)

df_haystack = df_haystack[['metric', 'metric_value']]
df_haystack.set_index('metric', inplace=True)
df_haystack.rename(columns={'metric_value':'metric_value_haystack'}, inplace=True)

df_recore = df_recore[['metric', 'metric_value']]
df_recore.set_index('metric', inplace=True)
df_recore.rename(columns={'metric_value':'metric_value_core'}, inplace=True)

merged_df = df_brick.merge(df_db, on="metric").merge(df_haystack, on="metric").merge(df_recore,on="metric")
print(tabulate(merged_df, headers='keys'))





