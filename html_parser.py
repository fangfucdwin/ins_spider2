import re
import json
from bs4 import BeautifulSoup
from lxml import etree


class HtmlParser(object):
    def get_next_url(self, var_value):
        new_url = 'https://www.instagram.com/graphql/query/?query_hash=42323d64886122307be10013ad2dcc44&variables=&variables={0}'.format(json.dumps(var_value))
        return new_url

    def _get_new_data_baseurl(self, pic_data):
        pic_data_list = []
        pics = pic_data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges']
        end_cursor = pic_data["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_owner_to_timeline_media"]["page_info"]["end_cursor"]
        has_next_page = pic_data["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_owner_to_timeline_media"]["page_info"]["has_next_page"]
        for pic in pics:
            if pic['node'] != None:
                pic_data_dic = {}
                id = pic['node']['owner']['id']
                pic_url = pic['node']['display_url']
                like_count = pic['node']['edge_media_preview_like']['count']
                comment_count = pic['node']['edge_media_to_comment']['count']
                pic_data_dic['URL'] = pic_url
                pic_data_dic['Like_Count'] = like_count
                pic_data_dic['Commen_Count'] = comment_count
                pic_data_list.append(pic_data_dic)

        return pic_data_list, has_next_page, end_cursor, id

    def parse_base(self, base_html_cont):
        if base_html_cont is None:
            return
        html = etree.HTML(base_html_cont.content.decode())
        h = html.xpath('''//script[@type="text/javascript"]''')[3].text.replace('window._sharedData = ', '').strip()[:-1]
        pic_data = json.loads(h, encoding='utf-8')
        new_data_base = self._get_new_data_baseurl(pic_data)[0]
        has_next_page = self._get_new_data_baseurl(pic_data)[1]
        end_cursor = self._get_new_data_baseurl(pic_data)[2]
        id = self._get_new_data_baseurl(pic_data)[3]
        return new_data_base, has_next_page, end_cursor, id


    def _get_new_data_nexturl(self, pic_data):
        pic_data_list = []
        pics = pic_data['data']['user']['edge_owner_to_timeline_media']['edges']
        end_cursor = pic_data["data"]["user"]["edge_owner_to_timeline_media"]["page_info"]["end_cursor"]
        has_next_page = pic_data["data"]["user"]["edge_owner_to_timeline_media"]["page_info"]["has_next_page"]
        for pic in pics:
            if pic['node'] != None:
                pic_data_dic = {}
                pic_url = pic['node']['display_url']
                like_count = pic['node']['edge_media_preview_like']['count']
                comment_count = pic['node']['edge_media_to_comment']['count']
                pic_data_dic['URL'] = pic_url
                pic_data_dic['Like_Count'] = like_count
                pic_data_dic['Commen_Count'] = comment_count
                pic_data_list.append(pic_data_dic)

        return pic_data_list, has_next_page, end_cursor

    def parse_next(self, next_html_cont):
        if next_html_cont is None:
            return
        pic_data = json.loads(next_html_cont, encoding='uft-8')
        new_data_next = self._get_new_data_nexturl(pic_data)[0]
        has_next_page = self._get_new_data_nexturl(pic_data)[1]
        end_cursor = self._get_new_data_nexturl(pic_data)[2]

        return new_data_next, has_next_page, end_cursor
