# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "d8a912bd-d31a-462e-9cfe-7de913517d57",
# META       "default_lakehouse_name": "bronze_lakehouse",
# META       "default_lakehouse_workspace_id": "d4e907ea-42ae-48ec-80ab-9dc1c38bdd65",
# META       "known_lakehouses": [
# META         {
# META           "id": "d8a912bd-d31a-462e-9cfe-7de913517d57"
# META         }
# META       ]
# META     }
# META   }
# META }

# MARKDOWN ********************

# %%html
# # **Data Engineering**

# CELL ********************

df = spark.read.format("csv").option("header","true").load("Files/Raw_Data_ADLS/returns.csv")
# df now is a Spark DataFrame containing CSV data from "Files/Raw_Data_ADLS/returns.csv".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import pandas as pd
# Load data into pandas DataFrame from "/lakehouse/default/Files/Raw_Data_ADLS/returns.csv"
df = pd.read_csv("/lakehouse/default/Files/Raw_Data_ADLS/returns.csv")
display(df)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.sql("SELECT * FROM Lakehouse1.dbo.adls LIMIT 1000")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
