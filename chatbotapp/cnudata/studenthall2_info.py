from enum import Enum
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
import requests
from bs4 import BeautifulSoup
import datetime
import time

# 현재 날짜 생성
raw_date = datetime.datetime.now()
now = raw_date.strftime('%Y-%m-%d')

options = webdriver.ChromeOptions()
browser = webdriver.Chrome("./chromedriver.exe",options=options)


def get_soup(frame):
    url = "http://cnuis.cnu.ac.kr/jsp/etc/weekMenuFrame.jsp"
    browser.get(url)
    element = browser.find_element_by_name(frame)
    browser.switch_to.frame(element)
    soup = BeautifulSoup(browser.page_source, "lxml")
    return soup