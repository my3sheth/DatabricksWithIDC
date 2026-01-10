# Databricks notebook source
# MAGIC %md
# MAGIC ##DAY 0

# COMMAND ----------

!pip install kaggle

# COMMAND ----------

import os

os.environ["KAGGLE_USERNAME"] = "my3sheth"
os.environ["KAGGLE_KEY"] = "KGAT_0daf1c5f3e9ab021571cb8a8e91780ee"

print("Kaggle credentials configured!")

# COMMAND ----------

spark.sql("""
CREATE SCHEMA IF NOT EXISTS workspace.ecommerce
""")

# COMMAND ----------

spark.sql("""
CREATE VOLUME IF NOT EXISTS workspace.ecommerce.ecommerce_data
""")

# COMMAND ----------

# MAGIC %restart_python

# COMMAND ----------

!pip install kagglehub

import kagglehub

# Download latest version
path = kagglehub.dataset_download("mkechinov/ecommerce-behavior-data-from-multi-category-store")

print("Path to dataset files:", path)

# COMMAND ----------

import shutil

path = "/home/spark-51af5c84-6847-4d06-870d-91/.cache/kagglehub/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store/versions/8"

src_path = f"{path}/2019-Nov.csv"
dst_path1 = "/Volumes/workspace/ecommerce/ecommerce_data/2019-Nov.csv"

shutil.copy(src_path, dst_path1)

dst_path2 = "/Volumes/workspace/ecommerce/ecommerce_data/2019-Oct.csv"

shutil.copy(src_path, dst_path2)

# COMMAND ----------

df_n = spark.read.csv("/Volumes/workspace/ecommerce/ecommerce_data/2019-Nov.csv")

# COMMAND ----------

df = spark.read.csv("/Volumes/workspace/ecommerce/ecommerce_data/2019-Oct.csv")

# COMMAND ----------

print(f"October 2019 - Total Events: {df.count():,}")
print("\n" + "="*60)
print("SCHEMA:")
print("="*60)
df.printSchema()

# COMMAND ----------

print("\n" + "="*60)
print("SAMPLE DATA (First 5 rows):")
print("="*60)
df.show(5, truncate=False)
