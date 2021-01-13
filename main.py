from selenium import webdriver
import pyperclip
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import json
import random

count = 0
base_url = 'https://naver.com'
login_url = 'https://nid.naver.com/nidlogin.login'
search_url = 'https://search.naver.com/search.naver?query=%EB%AF%B8%EC%8A%A4%ED%84%B0%ED%8A%B8%EB%A1%AF+%EC%95%8C%ED%8E%98%EC%8A%A4'


def config():
    with open('config.json', 'r', encoding='utf-8-sig') as f:
        cfg = json.load(f)
    return cfg


def clipboard_input(user_xpath, user_input):
    pyperclip.copy(user_input)

    driver.find_element_by_xpath(user_xpath).click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    time.sleep(0.5)
    return


driver = webdriver.Chrome('chromedriver')
driver.get(login_url)
driver.implicitly_wait(10)
clipboard_input('//*[@id="id"]', config()['id'])
clipboard_input('//*[@id="pw"]', config()['pwd'])
driver.find_element_by_xpath('//*[@id="log.login"]').click()
time.sleep(0.5)

if driver.current_url == 'https://nid.naver.com/nidlogin.login':
    print('로그인에 실패했습니다. 유저 정보를 올바르게 입력 후 다시 실행해주세요.')
    driver.close()


while True:
    wait_time = 30
    driver.get(search_url)
    print('페이지 접속 완료.')

    rate = random.randrange(1, 3)

    for i in range(1, rate):
        page_value = random.randrange(1, 7)
        driver.find_element_by_xpath(f'//*[@id="main_pack"]/section[1]/div/div[2]/panel-list/div/ul/li[{page_value}]').click()
        sleep_interval = random.randrange(1, 5)
        wait_time -= sleep_interval
        time.sleep(sleep_interval)
        driver.switch_to_window(driver.window_handles[1])
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
    
    time.sleep(wait_time)
    count += 1
    print(f'{count}번 실행하였습니다.')
