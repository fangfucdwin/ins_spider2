import time
import html_parser
import html_outputer
import html_downloader
from config import *



class SpiderMain(object):
    def __init__(self):  # 初始化

        self.downloader = html_downloader.HtmlDownloader()  # 下载器
        self.parser = html_parser.HtmlParser()  # 解析器
        self.outputer = html_outputer.HtmlOutputer()  # 输出器

    def craw(self, base_url):
        try:
            start_base = time.perf_counter()
            print('crawing base_url')

            html_cont_base = self.downloader.download_base(base_url)
            new_data = self.parser.parse_base(html_cont_base)[0]
            self.outputer.collect_data(new_data)

            end_base = time.perf_counter() - start_base
            print('crawed base_url %.2fs' % end_base)

            has_next_page = self.parser.parse_base(html_cont_base)[1]
            end_cursor = self.parser.parse_base(html_cont_base)[2]

            var_value = {"id": "", "first": 12, "after": ""}
            var_value['id'] = self.parser.parse_base(html_cont_base)[3]

            count = 1

            while has_next_page:

                start_next = time.perf_counter()
                print('\ncrawing next_url_%d ' % count)

                var_value['after'] = end_cursor
                next_url = self.parser.get_next_url(var_value)
                html_cont_next = self.downloader.download_next(next_url)
                new_data = self.parser.parse_next(html_cont_next)[0]
                self.outputer.collect_data(new_data)

                end_next = time.perf_counter() - start_next
                print('crawed next_url_%d %.2fs' % (count, end_next))

                has_next_page = self.parser.parse_next(html_cont_next)[1]
                end_cursor = self.parser.parse_next(html_cont_next)[2]

                if count >= PAGE_COUNT:
                    break


                count += 1


        except Exception as e:
            print(str(e))
            # 根据报错信息提示错误
        
        self.outputer.output_html() #以html格式输出
        self.outputer.save_to_mongo() #保存在mongodb中
        self.outputer.save_image() #将图片保存到本地


if __name__ == '__main__':
    start_main = time.perf_counter()

    obj_spider = SpiderMain()
    obj_spider.craw(BASE_URL)

    end_main = time.perf_counter() - start_main

    print('\ncrawed %.2fs' % end_main)
