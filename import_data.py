import pandas as pd
import sqlite3

df = pd.read_csv("Global_Cybersecurity_Threats_2015-2024.csv")

conn = sqlite3.connect(r"C:\Users\jakub\Desktop\global cyber threats\cyber_threats.db")

df.to_sql("threats", conn, if_exists="replace", index=False)

conn.close()

print("Data imported successfully!")