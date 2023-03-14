from urllib import request as request_lib, parse
import ssl
from urllib.error import URLError

context = ssl._create_unverified_context()

url = "https://biihu.cc//account/ajax/login_process/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36"
}

dict = {
    "return_url": "https://biihu.cc/",
    "username": "xiaoshuaib@gmail.com",
    "password": "123456789",
    "_post_type": "ajax"
}

data = bytes(parse.urlencode(dict), 'UTF-8')

req = request_lib.Request(url, data=data, headers=headers, method='POST')

try:
    response = request_lib.urlopen(req, context=context)
    print(response.read().decode('utf-8'))
except URLError as err:
    print(err.reason)

