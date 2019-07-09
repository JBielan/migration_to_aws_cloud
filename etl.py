import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')
    
    print('Redshift connection...')
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    print('Redshift connected.')
    
    print('Loading staging tables from S3.. It can take about 2 hours.')
    load_staging_tables(cur, conn)
    print('Staging tables loaded.')
    
    print('Insert data from staging tables to fact and dimension tables')
    insert_tables(cur, conn)
    print('Data has been inserted.')

    conn.close()
    print('Connection has been closed.')


if __name__ == "__main__":
    main()