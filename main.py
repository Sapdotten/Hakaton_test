import http.client
import json
import os
import urllib.parse as up
import psycopg2


connection = http.client.HTTPSConnection('parseapi.back4app.com', 443)
connection.connect()
connection.request('GET', '/schemas/_Session', '', {
    "X-Parse-Application-Id": "bjoIcJFXfuwVRVDvjFOW5DXG931cVWj7TvezpzcU",
    "X-Parse-Master-Key": "kVSXIzLhcx3rRXKwj4aLi18okIxLiL3P8egROR9u"
})

# "X-Parse-REST-API-Key": "evZga6ZDf4sIoydxICnJ1DZPOcgs5BQyCQYlDKXg"
# "X-Parse-Master-Key": "kVSXIzLhcx3rRXKwj4aLi18okIxLiL3P8egROR9u"
result = json.loads(connection.getresponse().read())
print(result)


conn = psycopg2.connect(database='bvpzpagm',
                        user='bvpzpagm',
                        password='m8iAJHQshv9I-_ka_hzbZFGLYTlnsd4-',
                        host='kiouni.db.elephantsql.com',
                        port='5432'
                        )
cursor = conn.cursor()
cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'users'")
print(cursor.fetchall())
