import os
import requests
import subprocess
import platform
import sys

if __name__ == "__main__":
    # print(len(proxy.proxy_list()))
    # resp = requests.post('http://localhost:8080/users/test')
    # print(resp.text)
    from selenium import webdriver

    browser = webdriver.Chrome()
    print(type(browser))

    browser.get('http://www.baidu.com/')
    print(browser.title)
    print(browser.page_source)
    browser.find_element(by='p')

    kw_edit = browser.find_element_by_id('kw');
    print(type(kw_edit))
    kw_edit.send_keys('google')
    browser.find_element_by_id('su').click()