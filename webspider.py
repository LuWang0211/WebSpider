import urllib
import urllib.request

import requests

import selenium
from selenium import webdriver

import time

# urllib_test = urllib.request.urlopen('https://www.weibo.com/huangbo?is_hot=1')
# print(urllib_test)

# requests_test = requests.get('https://www.weibo.com/huangbo?is_hot=1')
# print(requests_test)
# print(requests_test.text)

dirver = selenium.webdriver.Chrome()

target_website = 'https://www.weibo.com/u/1197191492?is_hot=1' #刘涛tamia
# target_website = 'https://www.weibo.com/hu_ge?is_hot=1' #胡歌
dirver.get(target_website)

for times in range(3):
    # print(times)
    current_website = dirver.current_url # get current website address
    # origin web
    # https://passport.weibo.com/visitor/visitor?entry=miniblog&a=enter&url=https%3A%2F%2Fweibo.com%2Fhu_ge%3Fis_hot%3D1&domain=.weibo.com&ua=php-sso_sdk_client-0.6.28&_rand=1556872101.8915
    # print(f"before sleep: {current_website}")
    time.sleep(15)  # wait for web response
    if current_website == target_website:
        web_source = dirver.page_source
        f = open('/home/lududu/Documents/python_vm/WebSpider/page_source.txt', 'w+')
        f.write(web_source)
        f.close()
        break
    # current_website = dirver.current_url # get current website address
    # print(current_website)  