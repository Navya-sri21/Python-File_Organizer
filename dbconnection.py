import mysql.connector

def connection_db():
    dbconnect=mysql.connector.connect(
        host="localhost",
        user="root",
        password="2118",
        database="file_organizer_db"
    )
    return dbconnect