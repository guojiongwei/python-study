import json
from urllib.request import urlopen

html = urlopen("https://guojiongwei.top/client_demo_api/blog/list?pagesize=100")

# 字符串转为json
json_obj = json.loads(html.read().decode('utf-8'))
if(json_obj['code'] == 1):
  for item in json_obj['data']:
    print(item['title'])