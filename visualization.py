import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.close('all')

conn = sqlite3.connect("cyber_threats.db")
df = pd.read_sql_query("SELECT * FROM threats", conn)

sns.set(style="darkgrid")

fig, axes = plt.subplots(2, 2, figsize=(16,10))

# 1 Attack types
attack_counts = df["Attack Type"].value_counts()

sns.barplot(
    x=attack_counts.values,
    y=attack_counts.index,
    ax=axes[0,0]
)

axes[0,0].set_title("Most Common Cyber Attack Types")


loss_country = df.groupby("Country")["Financial Loss (in Million $)"].sum().sort_values(ascending=False).head(10)

sns.barplot(
    x=loss_country.values,
    y=loss_country.index,
    ax=axes[0,1]
)

axes[0,1].set_title("Top Countries by Financial Loss")


# 3 Attacks over time
attacks_year = df.groupby("Year").size()

sns.lineplot(
    x=attacks_year.index,
    y=attacks_year.values,
    ax=axes[1,0]
)

axes[1,0].set_title("Cyber Attacks Over Time")


# 4 Industries targeted
industry_counts = df["Target Industry"].value_counts().head(10)

sns.barplot(
    x=industry_counts.values,
    y=industry_counts.index,
    ax=axes[1,1]
)

axes[1,1].set_title("Industries Most Targeted")

plt.tight_layout()
plt.show()


# 2. financial losses by country
plt.figure(figsize=(10,6))
loss_country = df.groupby("Country")["Financial Loss (in Million $)"].sum().sort_values(ascending=False).head(10)

sns.barplot(x=loss_country.values, y=loss_country.index)

plt.title("Top Countries by Cybercrime Financial Loss")
plt.xlabel("Total Loss (Million $)")
plt.ylabel("Country")

plt.show()


# 3. attacks over time
plt.figure(figsize=(10,6))
attacks_year = df.groupby("Year").size()

sns.lineplot(x=attacks_year.index, y=attacks_year.values)

plt.title("Cyber Attacks Over Time")
plt.xlabel("Year")
plt.ylabel("Number of Incidents")

plt.show()


# 4. attacks by industry
plt.figure(figsize=(10,6))
industry_counts = df["Target Industry"].value_counts().head(10)

sns.barplot(x=industry_counts.values, y=industry_counts.index)

plt.title("Industries Most Targeted by Cyber Attacks")
plt.xlabel("Number of Incidents")
plt.ylabel("Industry")

plt.show()