import os
import urllib.parse as up
import psycopg2

conn = psycopg2.connect(database='bvpzpagm',
                        user='bvpzpagm',
                        password='m8iAJHQshv9I-_ka_hzbZFGLYTlnsd4-',
                        host='kiouni.db.elephantsql.com',
                        port='5432'
                        )
cursor = conn.cursor()
cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'users'")
print(cursor.fetchall())
