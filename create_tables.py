import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    """
    Description: Drops all tables so new can be created for tests.

    Arguments:
        cur: the cursor object. 
        conn: the database connection object. 

    Returns:
        None
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Description: Creates both staging and facts/dimensions tables.

    Arguments:
        cur: the cursor object. 
        conn: the database connection object. 

    Returns:
        None
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')
    
    print('Redshift connection...')
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    print('Redshift connected.')
    
    print('Dropping tables..')
    drop_tables(cur, conn)
    print('Tables have been dropped')
    
    print('Creating tables..')
    create_tables(cur, conn)
    print('Tables have been created.')

    conn.close()
    print('Connection has been closed.')


if __name__ == "__main__":
    main()