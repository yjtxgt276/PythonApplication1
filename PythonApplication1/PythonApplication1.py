# OK now this is on git
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

import urllib
from urllib import request
import bs4
from bs4 import BeautifulSoup

import re

chrome_driver = "C:\Programs\Python\Python36\Lib\site-packages\chromedriver_binary\chromedriver.exe"
snkrs_launch_page = "https://www.nike.com/launch/"

def check_out():
    uname_str = "xiazhang86@gmail.com"
    passwd_str = "Xxxsnow1985,"
    browser = webdriver.Chrome(chrome_driver)
    browser.get('https://www.nike.com/checkout/tunnel')
    user = browser.find_element(by = By.NAME, value = 'emailAddress')
    passwd = browser.find_element(by = By.NAME, value = 'password')
    user.send_keys(uname_str)
    passwd.send_keys(passwd_str)
    try:
        checkout_button = browser.find_element(by = By.XPATH, value = "//input[@value='MEMBER CHECKOUT']")
    except Exception as e:
        print(e)
    else:
        checkout_button.click()

def check_snkrs_web():
    browser = webdriver.Chrome(chrome_driver)
    browser.get(snkrs_launch_page)
    try:
        # TODO need to get the correct size to add to cart
        in_stock = browser.find_elements(by = By.XPATH, value = "//a[contains(@href, 'react-element-87-pure-platinum-photo-blue')]")
    except Exception as e:
        print(e)
    else:
        print(in_stock)
        if len(in_stock):
            in_stock[0].click()

def check_snkrs_back():
    page = request.urlopen(snkrs_launch_page)
    soup = BeautifulSoup(page, 'html.parser')
    for base in soup.find_all("base"):
        print(base)

    for tag in soup.find_all("a", href = re.compile("react-element-87-pure-platinum-photo-blue")):
        #tmp_pg = request.urlopen(tag.get("href"))  #TODO: need to figure out how to goto the relative url like this
        print(tag)



    #print(soup.prettify()) #print the whole page
    

            
def main():
    err = 0
    check_snkrs_web()
    #check_snkrs_back()
    return err


if __name__ == "__main__":
    main()