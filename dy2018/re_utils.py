import re


def re_get_actor(html):
    a = re.search(r'<p>◎主　　演　(.*)</p>\n(<p>　　　　　　(.*)</p>\n)*', html).group(0)
    line_list = a.split("\n")
    actors = [re.match(r'<p>(◎主\u3000\u3000演)?[\u3000]+(.*)</p>', tag_p).group(2) for tag_p in line_list if re.match(r'<p>(◎主\u3000\u3000演)?[\u3000]+(.*)</p>', tag_p)]
    return actors
