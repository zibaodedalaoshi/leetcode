import requests

url='http://localhost:8075/webroot/decision/view/report?op=fr_dialog&cmd=parameters_d'
body={
"__parameters__":"{\"A\":\"[534e][4e1c]\",\"LABEL1\":\"[5730][533a]:\"}",
"_":1648386610015}
headers={

"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.52"


}
res=requests.get(url=url,headers=headers,auth=)
#res2=requests.get(url=url)
print(res.text)
