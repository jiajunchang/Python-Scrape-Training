"""
<html_output.py>
Return data as Table
"""
import time

class HtmlOutput(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        file_name = time.strftime("%Y-%m-%d_%H-%M-%S")
        with open("out_%s.html" % file_name, "w", encoding='utf-8') as f_out:
            f_out.write("<html>")
            f_out.write(r'<head>'
                        r'<link rel="stylesheet"'
                        r'href="cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css"'
                        r'integerity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u"'
                        r'crossorigin="anonymous"></head>')
            f_out.write("<body>")
            f_out.write(r'<table class="table table-bordered table-hover">')

            item_css = ['active', 'success', 'warning', 'info']
            for data in self.datas:
                index = self.datas.index(data) % len(item_css)
                f_out.write(r'<tr class="' + item_css[index] + r'">')
                f_out.write('<td>{}</td>'.format(data["url"]))
                f_out.write('<td>{}</td>'.format(data["title"]))
                f_out.write('<td>{}</td>'.format(data["summary"]))
                f_out.write("</tr>")

            f_out.write("</table>")
            f_out.write("</body>")
            f_out.write("<html>")