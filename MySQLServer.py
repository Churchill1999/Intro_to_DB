#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # CONNECT TO MYSQL SERVER
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""  # add your MySQL password if you have one
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # CREATE DATABASE (NO SELECT OR SHOW)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # CLOSE CONNECTION
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
