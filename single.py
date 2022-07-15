import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt

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

merged_df = df_brick.merge(df_db, on="metric").merge(df_haystack, on="metric").merge(df_recore,on="metric")
print(tabulate(merged_df, headers='keys'))

# merged_df = merged_df[(merged_df.metric == "abox_axiom_count")|(merged_df.metric == "tbox_axiom_count")]
# merged_df.set_index('metric', inplace=True)
# merged_df['metric_value_brick']=merged_df['metric_value_brick'].astype(float)
# merged_df['metric_value_db']=merged_df['metric_value_db'].astype(float)
# merged_df['metric_value_haystack']=merged_df['metric_value_haystack'].astype(float)
# merged_df['metric_value_core']=merged_df['metric_value_core'].astype(float)
# ax = merged_df.plot(kind="bar")
# for container in ax.containers:
#     ax.bar_label(container)
# plt.xticks(rotation=0, horizontalalignment="center")
# plt.show()

# merged_df = merged_df[(merged_df.metric == "assert_n_subclass_avg")|(merged_df.metric == "assert_n_superclass_avg")]
# merged_df.set_index('metric', inplace=True)
# merged_df['metric_value_brick']=merged_df['metric_value_brick'].astype(float)
# merged_df['metric_value_db']=merged_df['metric_value_db'].astype(float)
# merged_df['metric_value_haystack']=merged_df['metric_value_haystack'].astype(float)
# merged_df['metric_value_core']=merged_df['metric_value_core'].astype(float)
# ax = merged_df.plot(kind="bar",figsize=(12,5))
# for container in ax.containers:
#     ax.bar_label(container)
# plt.xticks(rotation=0, horizontalalignment="center")
# ax.legend(loc='upper center')
# plt.show()

# merged_df = merged_df[(merged_df.metric == "class_count")|(merged_df.metric == "class_sgl_subcl_count")]
# merged_df.set_index('metric', inplace=True)
# merged_df['metric_value_brick']=merged_df['metric_value_brick'].astype(float)
# merged_df['metric_value_db']=merged_df['metric_value_db'].astype(float)
# merged_df['metric_value_haystack']=merged_df['metric_value_haystack'].astype(float)
# merged_df['metric_value_core']=merged_df['metric_value_core'].astype(float)
# ax = merged_df.plot(kind="bar")
# for container in ax.containers:
#     ax.bar_label(container)
# plt.xticks(rotation=0, horizontalalignment="center")
# ax.legend(loc='upper center')
# plt.show()

# merged_df = merged_df[(merged_df.metric == "dataproperty_count")|(merged_df.metric == "datatypes_count")]
# merged_df.set_index('metric', inplace=True)
# merged_df['metric_value_brick']=merged_df['metric_value_brick'].astype(float)
# merged_df['metric_value_db']=merged_df['metric_value_db'].astype(float)
# merged_df['metric_value_haystack']=merged_df['metric_value_haystack'].astype(float)
# merged_df['metric_value_core']=merged_df['metric_value_core'].astype(float)
# ax = merged_df.plot(kind="bar")
# for container in ax.containers:
#     ax.bar_label(container)
# plt.xticks(rotation=0, horizontalalignment="center")
# plt.show()

# merged_df = merged_df[(merged_df.metric == "obj_property_count")]
# merged_df.set_index('metric', inplace=True)
# merged_df['metric_value_brick']=merged_df['metric_value_brick'].astype(float)
# merged_df['metric_value_db']=merged_df['metric_value_db'].astype(float)
# merged_df['metric_value_haystack']=merged_df['metric_value_haystack'].astype(float)
# merged_df['metric_value_core']=merged_df['metric_value_core'].astype(float)
# ax = merged_df.plot(kind="bar")
# for container in ax.containers:
#     ax.bar_label(container)
# plt.xticks(rotation=0, horizontalalignment="center")
# plt.show()







