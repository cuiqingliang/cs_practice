import json
import os

from mitmproxy import http
def response(flow: http.HTTPFlow):
    if 'quote.json' in flow.request.pretty_url and 'x=' in flow.request.pretty_url:
        data=json.loads(flow.response.content)
        data['data']['items'][1]['quote']['name'] *= 2
        data['data']['items'][2]['quote']['name']=''
        flow.response.text=json.dumps(data)
if __name__ =='__main__':
    os.system("mitmdump -p 8999 -s 'D:\学习\代码\Code_prataic\mitm\mitm\mitm_response.py'")