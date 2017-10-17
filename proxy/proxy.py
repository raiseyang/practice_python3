"""
http://www.cnblogs.com/hearzeus/p/5157016.html
"""

# encoding=utf8
import re

import requests
from bs4 import BeautifulSoup

User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
header = {}
header['User-Agent'] = User_Agent


def proxy_list():
    """

    :return: list
    """
    url = 'http://www.xicidaili.com/nt/1'  # 代理IP站点

    resp = requests.get(url, headers=header)

    hostnames = []
    array = re.findall("<td>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}</td>\s.+<td>\d+</td>", resp.text)
    for ip_port in array:
        match = re.match('<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td>\n      <td>(\d+)</td>', ip_port)
        hostnames.append(match.group(1) + ":" + match.group(2))  # 找出所有ip
    print("爬去了{}个代理".format(len(hostnames)))

    hostnames_full = ["http://" + hh for hh in hostnames]
    available_hostnames = []
    fail_count = 0
    success_count = 0
    for full in hostnames_full:
        try:
            proxies = {"http": full}
            # print("proxies:", proxies)
            resp = requests.get("http://ip.chinaz.com/getip.aspx", proxies=proxies, timeout=3)
            print("---ok---:", proxies, "  ", success_count)
            success_count += 1
            available_hostnames.append(full)
            with open("proxy_ips.txt", "a") as file:
                file.write(full)
        except BaseException as e:
            print("---fail---:", fail_count)
            fail_count += 1
            # hostnames_full.remove(full)
            continue
    return available_hostnames

# print(list(array))


# with open("proxy1.txt", "wb") as file:
#     file.write(resp.content)


# soup = BeautifulSoup(resp.text)
# print(soup.text)
# ips = soup.findAll('tr')
# f = open("./proxy.txt", "w")
#
# for x in range(1, len(ips)):
#     ip = ips[x]
#     tds = ip.findAll("td")
#     ip_temp = tds[2].contents[0] + "\t" + tds[3].contents[0] + "\n"
#     # print tds[2].contents[0]+"\t"+tds[3].contents[0]
#     f.write(ip_temp)
