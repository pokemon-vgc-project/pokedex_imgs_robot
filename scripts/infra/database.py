import mysql.connector

def connect_to_mysql(config):
    try:
        connection = mysql.connector.connect(**config)
        return connection
    except mysql.connector.Error as err:
        print(f"Connect error: {err}")

def close_connection(connection):
    connection.close()