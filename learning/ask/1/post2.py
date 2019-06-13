"""
很多时候你想要发送的数据并非编码为表单形式的。如果你传递一个 string 而不是一个dict ，那么数据会被直接发布出去。
"""
import requests
import json

url = 'http://hdh.tae-tea.net/yestae-community-api/api/TP0004'
payload = {'jsurl': 'http://localhost:8080', 'sign': '9fe22d86c2cb4b60a9ad5fcc35b04ca9', 'key3': None, }
# r = requests.post(url, data=json.dumps(payload))
r = requests.post(url, json=payload)
print(r.text)
print(r.content)
print(r.json())
print(r.status_code)
print(r.raw)
