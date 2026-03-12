# Global Cyber Threat Intelligence Analysis

## Project Overview
This project analyzes global cybersecurity incidents to identify patterns in cyber attacks, financial losses, targeted industries, and threat actors.
The analysis combines **SQL, Python, and Power BI** to explore the dataset, perform data analysis, and create an interactive cyber threat intelligence dashboard.
The goal of this project is to demonstrate how data analytics can be applied to cybersecurity data to uncover insights about global cyber threats.

---

# Dataset

The dataset contains global cybersecurity incidents between **2015 and 2024**.
Source: https://www.kaggle.com/datasets/atharvasoundankar/global-cybersecurity-threats-2015-2024

Each record includes:

- Country
- Year
- Attack Type
- Target Industry
- Financial Loss (in Million $)
- Number of Affected Users
- Attack Source
- Security Vulnerability Type
- Defense Mechanism Used
- Incident Resolution Time

The dataset contains **3000 cybersecurity incidents** across multiple industries and countries.

---

# Tools & Technologies

This project uses multiple tools to simulate a real-world data analysis workflow.

### Data Analysis
- SQL (SQLite)

### Data Processing & Visualization
- Python
- Pandas
- Matplotlib
- Seaborn

### Dashboard
- Power BI
  
---

## Project Workflow

CSV Dataset → SQLite Database → SQL Analysis → Python Visualization → Power BI Dashboard

---

## Project Structure

```
global-cyber-threat-analysis
│
├── data
│   └── Global_Cybersecurity_Threats_2015-2024.csv
│
├── sql
│   └── analysis.sql
│
├── python
│   ├── import_data.py
│   ├── visualization.py
│   └── visualization_attacksourcedist.py
│
├── dashboard
│   └── cyber-threats.pbix
│
├── requirements.txt
├── README.md
└── LICENSE
```


# SQL Analysis

SQL was used to explore and analyze the cybersecurity dataset stored in SQLite.

---

## Preview Data

```sql
SELECT *
FROM threats
LIMIT 10;
```
<img width="1701" height="883" alt="Zrzut ekranu 2026-03-11 203328" src="https://github.com/user-attachments/assets/c15fad4f-cc2c-43ef-8cf1-1777665cd3f6" />
This query previews the first rows of the dataset.

---

## Most Common Cyber Attack Types

```sql
SELECT "Attack Type", COUNT(*) as attacks
FROM threats
GROUP BY "Attack Type"
ORDER BY attacks DESC;
```
This query identifies the most frequent types of cyber attacks.

---

## Top Countries by Cybercrime Financial Loss

```sql
SELECT Country,
SUM("Financial Loss (in Million $)") as losses
FROM threats
GROUP BY Country
ORDER BY losses DESC;
```
Shows which countries experience the highest financial losses caused by cyber attacks.

---

## Financial Loss by Attack Type

```sql
SELECT "Attack Type",
SUM("Financial Loss (in Million $)") as total_loss
FROM threats
GROUP BY "Attack Type"
ORDER BY total_loss DESC;
```

Analyzes which attack types generate the largest financial damage.

---

## Most Common Cyber Attack Sources

```sql
SELECT "Attack Source",
COUNT(*) as incidents
FROM threats
GROUP BY "Attack Source"
ORDER BY incidents DESC;
```

Identifies the main threat actors responsible for cyber incidents.

---

## Industries Most Targeted by Cyber Attacks

```sql
SELECT "Target Industry",
COUNT(*) as attacks
FROM threats
GROUP BY "Target Industry"
ORDER BY attacks DESC;
```

Shows which industries are most frequently targeted.

---

## Cyber Attacks Over Time

```sql
SELECT Year,
COUNT(*) as incidents
FROM threats
GROUP BY Year
ORDER BY Year;
```

Analyzes how the number of cyber attacks changes over time.

---

## Largest Individual Cyber Incidents

```sql
SELECT Country,
Year,
"Attack Type",
"Target Industry",
"Financial Loss (in Million $)"
FROM threats
ORDER BY "Financial Loss (in Million $)" DESC
LIMIT 10;
```

Identifies the cyber incidents with the highest financial losses.

## Dashboard Preview

<img width="1254" height="674" alt="cyber1powerbi" src="https://github.com/user-attachments/assets/5986c6e4-26d6-4317-99f6-9ab58fbed545" />
<img width="1182" height="635" alt="cyber2powerbi" src="https://github.com/user-attachments/assets/215be0f5-1ca3-4db4-a760-e0ca5b38fb86" />



## How to Run the Project

1. Clone the repository

```
git clone https://github.com/yourusername/global-cyber-threat-analysis.git
```

2. Import the dataset into SQLite

```
python import_data.py
```

This script loads the CSV dataset into a SQLite database (`cyber_threats.db`).

3. Run SQL analysis queries

Open the database using the **SQLite extension in VS Code** and run queries from:

```
analysis.sql
```

4. Run Python visualizations

```
python visualization.py
```

5. Open the Power BI dashboard

Open the file:

```
cyber-threats.pbix
```

to explore the interactive cybersecurity dashboard.


## Key Insights
- **DDoS and phishing attacks** are the most frequent cyber threats.
- **DDoS attacks generate the highest financial losses** among the analyzed attack types.
- **Nation-state actors and unknown attackers** are responsible for the largest share of cyber incidents.
- **IT, banking, and healthcare sectors** are among the most frequently targeted industries.
- Cyber incidents remain **consistently high across the years analyzed (2015–2024)**.
- Large-scale cyber attacks can result in **financial losses approaching 100 million USD per incident**.


## Future Improvements

• Add machine learning models to predict cyber attack trends  
• Build automated ETL pipeline for cybersecurity datasets  
• Integrate threat intelligence APIs  
• Deploy dashboard using Power BI Service


