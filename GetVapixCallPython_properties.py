import requests
from requests.auth import HTTPDigestAuth

url = "http://192.168.1.192/axis-cgi/param.cgi"

querystring = {"action":"list", "responseformat":"rfc"}


response = requests.request('GET',url,params=querystring, auth=HTTPDigestAuth('root','pass'))

print(response.text)

