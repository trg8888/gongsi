import random
import time
from selenium import webdriver
option = webdriver.ChromeOptions()
option.add_argument("--no-sandbox")
# option.add_argument("--headless")       # 无头模式

driver = webdriver.Chrome(options=option,executable_path=r'D:\webdriver\chromedriver.exe')
driver.get('https://reg.taobao.com/member/reg/fast/fast_reg?_regfrom=CBU')
time.sleep(1)
driver.find_element_by_xpath('//button[@class="next-btn next-btn-primary next-btn-medium"]').click()
driver.find_element_by_id('nick').send_keys('tangasdsad')
driver.find_element_by_id('password').send_keys('12345tangasdsad6')
driver.find_element_by_id('rePassword').send_keys('12345tangasdsad6')
driver.find_element_by_xpath('//span[@class="next-input next-input-single next-input-large mobile-input"]/input').send_keys('18808888888')
def is_element_exist(element):
    try:
        driver.find_element_by_xpath(element)
        return True
    except:
        return False

hover = driver.find_element_by_id('nc_1_n1z')
# ActionChains类方法
action = webdriver.ActionChains(driver)
# 点击保持不松开
action.click_and_hold(hover).perform()
# 设置滑动距离，横向滑动340px 纵向滑动 0px
action.move_by_offset(random.randint(60,259), 0)
# time.sleep(1)
# # time.sleep(1)
action.move_by_offset(260, 0)
# 松开鼠标
action.release().perform()
while True:
    if is_element_exist(element='//i[@class="nc_iconfont icon_warn"]'):
        driver.find_element_by_xpath('//a[@href="javascript:noCaptcha.reset(1)"]').click()
        hover = driver.find_element_by_id('nc_1_n1z')
        # ActionChains类方法
        action = webdriver.ActionChains(driver)
        # 点击保持不松开
        action.click_and_hold(hover).perform()
        # 设置滑动距离，横向滑动340px 纵向滑动 0px
        action.move_by_offset(random.randint(60, 259), 0)
        # time.sleep(1)
        # # time.sleep(1)
        action.move_by_offset(260, 0)
        # 松开鼠标
        action.release().perform()
        # 松开鼠标
    else:
        break
driver.find_element_by_xpath('//div[@class="form-checkbox"]/label/input').click()
time.sleep(1)
driver.find_element_by_name('loginAction').click()
time.sleep(2)
driver.find_element_by_xpath('//div[@class="next-col-16 next-form-item-control"]/button').click()
time.sleep(1)