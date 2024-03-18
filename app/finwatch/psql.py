import psycopg2

conn = psycopg2.connect(database="postgres", user=psql_user, password=psql_pass, host=psql_ip, port=psql_port)
conn.autocommit = True
cursor = conn.cursor()

def init_databases(databases: list, psql_user, psql_pass, psql_ip, psql_port):
    conn = psycopg2.connect(database="postgres", user=psql_user, password=psql_pass, host=psql_ip, port=psql_port)
    
    conn.autocommit = True
    cursor = conn.cursor()

    for database_name in databases:
        try:
            sql = f'''CREATE database {database_name};'''
            cursor.execute(sql)
            print(f"Database {database_name} has been created successfully !!")   
        except (psycopg2.OperationalError, psycopg2.errors.DuplicateDatabase) as e:
            print(e)
    
    conn.close()