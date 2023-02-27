import http.client

conn = http.client.HTTPSConnection("myhealthbox.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "62d9f14f36msha35d67bf114aaf5p197fa8jsn6d56b128e3a5",
    'X-RapidAPI-Host': "myhealthbox.p.rapidapi.com"
    }

conn.request("GET", "/search/updatedDocuments?sd=2020-06-01&c=us&l=en", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))