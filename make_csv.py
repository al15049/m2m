#/usr/bin/env python
# coding:utf-8

import sys
import requests
import http.server
import urllib
import csv
import datetime

# サーバの立ち上げ
def run(port, handler):
    address = ("", int(port))
    server = http.server.HTTPServer(address, handler)
    server.serve_forever()

#コールバック関数の指定
class CallbackServer(http.server.BaseHTTPRequestHandler):

    #GETに対する応答
    def do_GET(self):
        # queryにGETのクエリ内容の文字列が入る（lux=100&temp=10）
        parsed_path = urllib.parse.urlparse(self.path)
        d = datetime.datetime.today()
        
        Time_List = []
        
        Time_List.append(d.month)
        Time_List.append("/")
        Time_List.append(d.day)
        Time_List.append(" ")
        Time_List.append(d.hour)
        Time_List.append(":")
        Time_List.append(d.minute)
        Time_List.append(" ")
        Time_List.append(d.second)
        
        maped_list = map(str,Time_List)
        str_time = "".join(maped_list)


        # 解析した結果は辞書型({'lux' : [100], 'temp' : [10]}) 
        query = urllib.parse.parse_qs(parsed_path.query)
        with open('./cgi-bin/sound.csv','a',newline="")as f:
            for row in query['lux'][0]:
                f.write(str(row))
            f.write(",")
            f.write(str_time)
            f.write("\n")

        print (query['lux'][0])

        self.send_response(200)
        self.end_headers()
        self.wfile.write(parsed_path.query.encode())

        return

if __name__ == '__main__':
    run(sys.argv[1], CallbackServer)

