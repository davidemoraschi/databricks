# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC # Load data from MySQL to Delta Lake
# MAGIC
# MAGIC This notebook shows you how to import data from JDBC MySQL databases into a Delta Lake table using Python.

# COMMAND ----------

def import_mysql_table(table_name):
  # import from MySql and recreate into data store
  driver = "org.mariadb.jdbc.Driver"
  database_host = "relational.fit.cvut.cz"
  database_port = "3306"
  database_name = "tpcds"
  table = table_name
  user = "guest"
  password = "relational"
  url = f"jdbc:mysql://{database_host}:{database_port}/{database_name}"
  print(table_name)
  remote_table = (spark.read
    .format("jdbc")
    .option("driver", driver)
    .option("url", url)
    .option("dbtable", table)
    .option("user", user)
    .option("password", password)
    .load()
  )
  target_table_name = "relational_fit_cvut_cz." + table_name
  remote_table.write.mode("overwrite").saveAsTable(target_table_name)
  return

# COMMAND ----------

import_mysql_table("call_center")
import_mysql_table("catalog_page")
import_mysql_table("catalog_returns")
import_mysql_table("catalog_sales")
import_mysql_table("customer")
import_mysql_table("customer_address")
import_mysql_table("customer_demographics")
import_mysql_table("date_dim")
import_mysql_table("household_demographics")
import_mysql_table("income_band")
import_mysql_table("inventory")
import_mysql_table("item")
import_mysql_table("promotion")
import_mysql_table("reason")
import_mysql_table("ship_mode")
import_mysql_table("store")
import_mysql_table("store_returns")
import_mysql_table("store_sales")
import_mysql_table("time_dim")
import_mysql_table("warehouse")
import_mysql_table("web_page")
import_mysql_table("web_returns")
import_mysql_table("web_sales")
import_mysql_table("web_site")
