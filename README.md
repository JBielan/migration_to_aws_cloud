# Migration from on-premise to AWS Cloud

## Table of contents
* [Problem to Solve](#Problem)
* [Solution](#Solution)
* [Concrete Steps](#Steps)
* [Schema](#Schema)
* [ETL(Extract, Transform, Load) Process](#ETL)
* [Security](#Security)
* [Suggestions](#Suggestions)
* [Let's see the proof](#Proof)
--------------------------------------------

#### Problem to Solve
Audio streaming start-up after successful scaling period needs to switch from local servers to cloud. The company doesn't want to invest more in in-house hardware and is going to test multiple solutions on AWS cloud. 

#### Solution
Data from on-premise databases has been moved in json files to S3 (AWS Simple Storage Service). Right now the only job to do is puting it into Redshift (Data Warehouse with columnar storage).

#### Concrete Steps
1. Staging tables are created to store the data from S3. 
2. Data is transfered to staging tables.
3. Fact and Dimension tables are created to be prepared for handy analysis.
4. Data from staging tables is moved to Fact and Dimension tables.

#### Schema
Image
Legend:
- fields with black bullets are set as NOT NULL
- underlined fields are primary keys

#### ETL(Extract, Transform, Load) Pocess
Python has been used as a bridge between SQL queries and AWS Services. Using simple SQL queries data has been moved from S3 to staging tables and then directly to Facts and Dimensions tables.

#### Security
Taking into account that the whole process is not production ready but rather proof of concept, no major prerequisites have been made. It's safe enough to set everything to default with `AmazonS3ReadOnlyAccess` for Redshift cluster. 

#### Suggestions
While running the whole proccess be prepared for 2 hours+ waiting time. The more nodes you choose the faster it will be. Recommended configuration of Redshift is `dc2.large` with at least 4 nodes. It should take a little bit less than 2 hours. 

#### Let's see the proof
Create Redshift `dc2.large` cluster with minimum of 4 nodes (it's 0.25USD/h but you need it for less then 2 hours). Fill `dwh.cfg` configuration file with appropriate parameters for your cluster.

From command line on computer with internet connection:
    python create_tables.py
    python etl.py
    
There you go! You can log into your AWS account and see the data using `Query editor` in your `Redshift dashboard`.