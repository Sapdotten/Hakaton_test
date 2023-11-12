import http.client
import json

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



