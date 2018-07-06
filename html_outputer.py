import os

import pymongo


from hashlib import md5

import requests

from config import *




class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.extend(data)

    def output_html(self):
        fout = open('output.html', 'w', encoding='utf-8')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<ul>")
        num = 1
        for data in self.datas:

            fout.write("<li>")

            fout.write('<a href="%s" target="_blank">%s</a>' % (data['URL'], num))
            fout.write('<img src="%s" width="640" height="640">' % data['URL'])
            fout.write("<br /><b>LikeCount:%s</b><br />" % data['Like_Count'])
            fout.write("<b>CommenCount:%s</b>" % data['Commen_Count'])

            fout.write("</li>")
            num += 1

        fout.write("</ul>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()

    def save_to_mongo(self):
        client = pymongo.MongoClient(MONGO_URL)
        db = client[DATEBASE_DB]
        count = 1
        for data in self.datas:
            if db[DATEBASE_TABLE].insert(data):
                print('存储第{0:d}条内容到Mongo成功'.format(count), data['URL'])
            count += 1
        return True

    def save_image(self):
        count = 1
        for data in self.datas:
            print('正在下载第{0:d}张图片'.format(count), data['URL'])

            if data['URL'] is None:
                return None

            kv = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36',
                'referer': 'https://www.instagram.com/',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'cookie': '用户登录的cookie'
            }
            response = requests.get(data['URL'], headers=kv)
            response.encoding = response.apparent_encoding

            if response.status_code != 200:
                return None
            file_path = '{0}/{1}.{2}'.format(os.getcwd(), md5(response.content).hexdigest(), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                    f.close()
            count += 1
