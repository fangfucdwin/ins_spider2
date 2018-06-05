import string
from urllib import request
from urllib.parse import quote

import requests


class HtmlDownloader(object):
    def download_base(self, base_url):
        if base_url is None:
            return None

        kv = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36',
            'referer': 'https://www.instagram.com/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'cookie': 'ds_user_id=7835676456; csrftoken=z5yp7F7g7AApLBGWQUsNDiu34c48j5NF; shbid=8778; rur=ATN; sessionid=IGSCf1391681e97905f7a957d125894583f3c191115565cd1adb4355760592be42dd%3AII76wH33uF4BeIOeXm3ZYs60V6lXUa5z%3A%7B%22_auth_user_id%22%3A7835676456%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%227835676456%3ALYhvsUR47Z7M61ksdm0YSKUcyoBAuiO9%3Ad4440c309c046f0980db215d1066ed3002932e8e4dc98a0e3d191ba865308e1c%22%2C%22last_refreshed%22%3A1527504417.3028142452%7D; mid=WwveFwALAAHWbyG__sTFw6noH6n3; mcd=3; fbm_124024574287414=base_domain=.instagram.com; urlgen="{\"time\": 1527504407\054 \"65.49.225.176\": 25820}:1fNFnV:LtI0lwhjY-dLK3wMQfD_1sxb140"; fbsr_124024574287414=aciYeBVvspIqaeLxn2CRSx0mza0ayhjLXcWqvk6uUPU.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUURScE1tY3lPdExQMkxXb1lORDNoeTF0c3J3ZzRBSnNSZ0VqUS00a21veXhCTjlPRUd1eXd0MUItMXdiR28yX3kwS1RYU0RBMVNvbzZpcVZPOUNGQTdnbWx6Rk1Md3JMMmctOURxa3pfVHd2XzN1eGkzM0NjR3p1TDQtVnZVSmZSMW12ZkUxUFg5ZWxNT0tRdl9yMEl2Vll5UjlvTFJMRUlwaUQ4S3BxUVFmNUVkMXJwVWRkRS1laDQ4aXhXMXFtN0s0M2g1eXpaR0U3WUVmbTJCVDlxam9uMFVDOVQyZko0MjEtVXJJWGs0WXZRUzlqbzhwLVNHejdsWEdJMnEyeW5LT2NGVVppUS1BbTJoVEdvSjU0MmZvMVIzR3pucC1GVDZCZ3JMd2RfeDZqX084am1MRE4yUEw5NlhyWHhYT2NPZmNJSTRfYVg0RWRHVkVCLTZUcTZxeCIsImlzc3VlZF9hdCI6MTUyNzUwNTAzOCwidXNlcl9pZCI6IjEwMDAyNTY3NzM1MDc5NSJ9'
        }

        response = requests.get(base_url, headers=kv)
        response.encoding = response.apparent_encoding

        if response.status_code != 200:
            return None

        return response

    def download_next(self, next_page):
        if next_page is None:
            return None

        kv = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36',
            'referer': 'https://www.instagram.com/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'cookie': 'ds_user_id=7835676456; csrftoken=z5yp7F7g7AApLBGWQUsNDiu34c48j5NF; shbid=8778; rur=ATN; sessionid=IGSCf1391681e97905f7a957d125894583f3c191115565cd1adb4355760592be42dd%3AII76wH33uF4BeIOeXm3ZYs60V6lXUa5z%3A%7B%22_auth_user_id%22%3A7835676456%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%227835676456%3ALYhvsUR47Z7M61ksdm0YSKUcyoBAuiO9%3Ad4440c309c046f0980db215d1066ed3002932e8e4dc98a0e3d191ba865308e1c%22%2C%22last_refreshed%22%3A1527504417.3028142452%7D; mid=WwveFwALAAHWbyG__sTFw6noH6n3; mcd=3; fbm_124024574287414=base_domain=.instagram.com; urlgen="{\"time\": 1527504407\054 \"65.49.225.176\": 25820}:1fNFnV:LtI0lwhjY-dLK3wMQfD_1sxb140"; fbsr_124024574287414=aciYeBVvspIqaeLxn2CRSx0mza0ayhjLXcWqvk6uUPU.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUURScE1tY3lPdExQMkxXb1lORDNoeTF0c3J3ZzRBSnNSZ0VqUS00a21veXhCTjlPRUd1eXd0MUItMXdiR28yX3kwS1RYU0RBMVNvbzZpcVZPOUNGQTdnbWx6Rk1Md3JMMmctOURxa3pfVHd2XzN1eGkzM0NjR3p1TDQtVnZVSmZSMW12ZkUxUFg5ZWxNT0tRdl9yMEl2Vll5UjlvTFJMRUlwaUQ4S3BxUVFmNUVkMXJwVWRkRS1laDQ4aXhXMXFtN0s0M2g1eXpaR0U3WUVmbTJCVDlxam9uMFVDOVQyZko0MjEtVXJJWGs0WXZRUzlqbzhwLVNHejdsWEdJMnEyeW5LT2NGVVppUS1BbTJoVEdvSjU0MmZvMVIzR3pucC1GVDZCZ3JMd2RfeDZqX084am1MRE4yUEw5NlhyWHhYT2NPZmNJSTRfYVg0RWRHVkVCLTZUcTZxeCIsImlzc3VlZF9hdCI6MTUyNzUwNTAzOCwidXNlcl9pZCI6IjEwMDAyNTY3NzM1MDc5NSJ9'
        }

        response = requests.get(next_page, headers=kv)
        response.encoding = response.apparent_encoding

        if response.status_code != 200:
            return None

        return response.text