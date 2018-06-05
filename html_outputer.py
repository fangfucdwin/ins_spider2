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

            fout.write('<a href="%s" target="_blank">%s</a>' % (data['URL'],num))
            fout.write('<img src="%s" width="640" height="640">' % data['URL'])
            fout.write("<br /><b>LikeCount:%s</b><br />" % data['Like_Count'])
            fout.write("<b>CommenCount:%s</b>" % data['Commen_Count'])

            fout.write("</li>")
            num += 1

        fout.write("</ul>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()