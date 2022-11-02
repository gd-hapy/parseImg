#  爬取ig图片

from selenium import webdriver
import time

PATH = "/usr/local/bin/chromedriver"
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from  selenium.webdriver.common.keys import Keys

import os
import wget

def parseImg():
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.instagram.com/")

    username = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.NAME, 'username'))

    password = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.NAME, 'password'))

    # 用户名
    username.send_keys("")
    # 密码
    password.send_keys("")


    loginBtn = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
    loginBtn.click()


    search = WebDriverWait(driver, timeout=30).until(lambda d: d.find_element(By.CLASS_NAME, '_aauy'))


    # exp = WebDriverWait(driver, timeout=30).until(lambda d: d.find_element(By.CLASS_NAME, '_ab6-'))
    exp = driver.find_element(By.CLASS_NAME, '_ab6-')


    exp.click()

    driver.get("https://www.instagram.com/explore/?next=%2F")
    time.sleep(3)


    for i in range(5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

    imgs = driver.find_elements(By.CLASS_NAME, 'x5yr21d')

    path = os.path.join("explore")
    if not os.path.exists(path):
        os.mkdir(path)

    for img in imgs:
        print(img.get_attribute("src"))
        img_url = img.get_attribute("src")
        img_name = img_url.split("?")[0].split("/")[-1]
        save_as = os.path.join(path, img_name)
        wget.download(img_url, save_as)



