import pandas as pd
from tabulate import tabulate

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
print (df_brick)

df_db = df_db[df_db.metric == "axiom_type_count"]
print (df_db)

df_haystack = df_haystack[df_haystack.metric == "axiom_type_count"]
print (df_haystack)

df_recore = df_recore[df_recore.metric == "axiom_type_count"]
print (df_recore)