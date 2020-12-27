import os

from mitmproxy import http

def request(flow: http.HTTPFlow):
    if 'quote.json' in flow.request.pretty_url:
        with open('C:\\Users\\admin\\Desktop\\xueqiu1.json',encoding='utf-8') as f:
            flow.response=http.HTTPResponse.make(
                200,
                f.read(),
                {'Content-Type': 'application/json'}
            )

if __name__ =='__main__':
    os.system("mitmdump -p 8999 -s 'D:\学习\代码\Code_prataic\mitm\mitm\mitm_response.py'")