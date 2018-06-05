import html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):  # 初始化

        self.downloader = html_downloader.HtmlDownloader()  # 下载器
        self.parser = html_parser.HtmlParser()  # 解析器
        self.outputer = html_outputer.HtmlOutputer()  # 输出器

    def craw(self, base_url):
        count = 1
        try:
            print('crawing %d ' % count)
            html_cont_base = self.downloader.download_base(base_url)
            new_data = self.parser.parse_base(html_cont_base)[0]
            self.outputer.collect_data(new_data)
            has_next_page = self.parser.parse_base(html_cont_base)[1]
            end_cursor = self.parser.parse_base(html_cont_base)[2]

            var_value = {"id": "", "first": 12, "after": ""}
            var_value['id'] = self.parser.parse_base(html_cont_base)[3]
            count = 2

            while has_next_page:

                print('crawing %d ' % count)
                var_value['after'] = end_cursor
                next_url = self.parser.get_next_url(var_value)
                html_cont_next = self.downloader.download_next(next_url)
                new_data = self.parser.parse_next(html_cont_next)[0]
                self.outputer.collect_data(new_data)
                has_next_page = self.parser.parse_next(html_cont_next)[1]
                end_cursor = self.parser.parse_next(html_cont_next)[2]

                if count >= 5:
                    break
                count += 1

        except Exception as e:
            print(str(e))
            # 根据报错信息提示错误

        self.outputer.output_html()



if __name__ == '__main__':
    base_url = 'https://www.instagram.com/nasa/'
    obj_spider = SpiderMain()
    obj_spider.craw(base_url)
