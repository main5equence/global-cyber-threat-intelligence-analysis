import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

conn = sqlite3.connect("cyber_threats.db")

df = pd.read_sql_query("SELECT * FROM threats", conn)

plt.figure(figsize=(10,6))

loss_by_actor = df.groupby("Attack Source")["Financial Loss (in Million $)"].sum()

sns.barplot(
    x=loss_by_actor.values,
    y=loss_by_actor.index
)

plt.title("Financial Loss by Threat Actor")
plt.xlabel("Total Financial Loss (Million $)")
plt.ylabel("Attack Source")

plt.tight_layout()
plt.show()