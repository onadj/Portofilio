import os
import datetime
import pymysql

# Get the username from the Cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
     with connection.cursor() as cursor:
                rows = [("oliver", 39, "1981-06-07 23:04:33"),
                        ("ana", 32, "1988-06-07 23:04:33"),
                        ("masa", 6, "2014-06-07 23:04:33")]
                            cursor.executemany("INSERT INTO Friends VALUES (%s,%s,%s);", rows)
                            connection.commit()
finally:
    connection.close()
