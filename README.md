# Data Warehouse for UAV Traffic Data
Data is like the new oil, it keeps growing and the demand for it is also growing. Machine learning and AI need more data to improve their accuracy. Quality of data and amount of data are essential to creating ai project, hence it's essential to focus on the data structures to store these data. It's like creating a home for your massive data. Most of cloud data warehouses exist, but how much will they charge you? Especially with the large size of drone data. Hence this application shows you how to access this service for free.

For this project, we focus on creating a data warehouse specifically for traffic data collected from drones by Pneuma.(https://open-traffic.epfl.ch/index.php/downloads/#1599047632450-ebe509c8-1330). The data downloaded is a CSV file. Every data instance; i.e one location, in a specific date, at a 30min interval, is approximately 



To view this data follow https://github.com/MegCheppy/travia to visualize the data, as a video, together with the features extracted from the data.

![image](https://user-images.githubusercontent.com/88152028/210540850-2d49de36-0b9d-4bfb-b854-22f92eda7bb4.png)



## To create the warehouse techstack,steps followed;
- Create a DAG-(A DAG is basically a code that does a specific task) in Airflow that uses the bash/python operator to load the data files into your database. Think about a useful separation of Prod, Dev and Staging
3- Connect dbt with your DWH and write transformations codes for the data you can execute via the Bash or Python operator in Airflow. Write proper documentation for your data models and access the dbt docs UI for presentation. 
- Check additional modules of dbt that can support you with data quality monitoring (e.g. great_expectations, dbt_expectations or re-data). 
- Connect the reporting environment and create a dashboard out of this data



Knowledge:
Enterprise-grade data engineering - using Apache and Databricks tools

Skills:
Create and maintain Airflow DAGs
Work with Apache Airflow, dbt, redash  and a DWH
Apply ELT techniques to DWH
Build data pipelines and orchestration workflows


