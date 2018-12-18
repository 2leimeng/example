# -*- coding: utf-8 -*-
from selenium import webdriver
import random
import time

def autoBrushProblem(account, password):
    driver = webdriver.Firefox()
    driver.get('http://physics.swjtu.edu.cn/newton/default.htm')
    time.sleep(3)

    driver.find_element_by_name('pID').clear()
    driver.find_element_by_name('pID').send_keys(account)
    driver.find_element_by_name('Password').clear()
    driver.find_element_by_name('Password').send_keys(password)
    driver.find_element_by_id('submit1').click()
    driver.find_element_by_xpath("//input[contains(@onclick, 'endD')]").click()

    for i in range(30):
        try:
            value = random.randint(1,2)
            driver.find_element_by_xpath("//input[@Name='exAns{number}' and@Value={value}]"
                                         .format(number=i,value=value)).click()
        except:
            pass
    driver.find_element_by_xpath("//input[contains(@value, '提交')]").click()
    time.sleep(3)
    driver.find_element_by_xpath("//a[contains(@href,'stuExSelect_select')]").click()
    driver.find_element_by_xpath("//input[contains(@onclick, 'endD')]").click()

    for i in range(40):
        try:
            number_value = random.randint(65,68)
            value = chr(number_value)
            driver.find_element_by_xpath("//input[@Name='exAns{number}' and @Value='{value}']"
                                         .format(number=i, value=value)).click()
        except:
            pass
    driver.find_element_by_xpath("//input[contains(@value, '提交')]").click()
    time.sleep(6)

    driver.close()
    driver.quit()
    print('你最新一期的网上物理作业已刷完。')

if __name__ == '__main__':
    autoBrushProblem(1234567890,'******')

