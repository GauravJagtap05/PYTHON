import urllib.request

f= urllib.request.urlopen("http://www.google.com")
data = f.read()
print(data)