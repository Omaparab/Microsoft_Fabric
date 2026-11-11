# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "f6ec0869-28ed-4a68-a157-d1418c24f04e",
# META       "default_lakehouse_name": "silver_lakehouse",
# META       "default_lakehouse_workspace_id": "d4e907ea-42ae-48ec-80ab-9dc1c38bdd65",
# META       "known_lakehouses": [
# META         {
# META           "id": "f6ec0869-28ed-4a68-a157-d1418c24f04e"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

from pyspark.sql.functions import *
from pyspark.sql.types import *

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# # **Reading Shortcuts**

# MARKDOWN ********************


# CELL ********************

df1 = spark.read.format("csv").option("header",True).load("Files/Raw_Data_ADLS")
display(df1)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# # **Reading Bronze Lakehouse product data**


# CELL ********************

df1 = spark.read.format("csv")\
            .option("header",True)\
            .option("inferSchema",True)\
            .load("abfss://Fabric_Learn@onelake.dfs.fabric.microsoft.com/bronze_lakehouse.Lakehouse/Files/Raw_DataAdventureWorks_Products")

df1.printSchema()
display(df1)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df1 = df1.withColumn("ActualProductCost",split("ProductSKU","-")[0])
display(df1)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# # **Writing product data in Files**

# CELL ********************

df1.write.format("delta")\
            .mode("append")\
            .option("path","Files/products")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df1.write.format("delta")\
            .mode("append")\
            .saveAsTable("products")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# # **Sales Data**

# CELL ********************

df2 = spark.read.format("csv")\
            .option("header",True)\
            .option("inferSchema",True)\
            .load("abfss://Fabric_Learn@onelake.dfs.fabric.microsoft.com/bronze_lakehouse.Lakehouse/Files/Raw_DataAdventureWorks_Sales_2016")

df2.printSchema()
display(df2)



df3 = spark.read.format("csv")\
            .option("header",True)\
            .option("inferSchema",True)\
            .load("abfss://Fabric_Learn@onelake.dfs.fabric.microsoft.com/bronze_lakehouse.Lakehouse/Files/Raw_DataAdventureWorks_Sales_2017")

df3.printSchema()
display(df3)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df4 = df2.union(df3)
display(df4)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df4.write.format("delta")\
            .mode("append")\
            .option("path","Files/sales")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df4.write.format("delta")\
            .mode("append")\
            .saveAsTable("sales")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# # **Calendar Data**

# CELL ********************

df = spark.read.format("csv")\
            .option("header",True)\
            .option("inferSchema",True)\
            .load("abfss://Fabric_Learn@onelake.dfs.fabric.microsoft.com/bronze_lakehouse.Lakehouse/Files/Raw_DataAdventureWorks_Calendar")

df.printSchema()
display(df)


df.write.format("delta")\
            .mode("append")\
            .option("mergeSchema", "true")\
            .option("path","Files/calendar")\
            .save()


df.write.format("delta")\
            .mode("append")\
            .option("mergeSchema", "true")\
            .saveAsTable("calendar")            

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.format("delta")\
            .load("abfss://Fabric_Learn@onelake.dfs.fabric.microsoft.com/bronze_lakehouse.Lakehouse/Tables/dbo/Merge")

for col_name in df.columns:
    if "." in col_name:
        df = df.withColumnRenamed(col_name, col_name.replace(".", "_"))

df.printSchema()
display(df)

df.write.format("delta")\
            .mode("append")\
            .option("mergeSchema", "true")\
            .option("path", "Files/category")\
            .save()

df.write.format("delta")\
            .mode("append")\
            .option("mergeSchema", "true")\
            .saveAsTable("category")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.format("csv")\
            .option("header",True)\
            .option("inferSchema",True)\
            .load("abfss://Fabric_Learn@onelake.dfs.fabric.microsoft.com/bronze_lakehouse.Lakehouse/Files/Raw_DataAdventureWorks_Territories")

df.printSchema()
display(df)


df.write.format("delta")\
            .mode("append")\
            .option("mergeSchema", "true")\
            .option("path","Files/territories")\
            .save()


df.write.format("delta")\
            .mode("append")\
            .option("mergeSchema", "true")\
            .saveAsTable("territories")            

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.format("csv")\
            .option("header",True)\
            .option("inferSchema",True)\
            .load("abfss://Fabric_Learn@onelake.dfs.fabric.microsoft.com/bronze_lakehouse.Lakehouse/Files/Raw_Data_ADLS")

df.printSchema()
display(df)


df.write.format("delta")\
            .mode("append")\
            .option("mergeSchema", "true")\
            .option("path","Files/returns")\
            .save()


df.write.format("csv")\
            .mode("append")\
            .option("mergeSchema", "true")\
            .saveAsTable("returns")            

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
