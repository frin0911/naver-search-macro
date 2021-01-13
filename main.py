from selenium import webdriver
import pyperclip
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import json

driver = webdriver.Chrome('chromedriver')
count = 0
base_url = 'https://naver.com'
login_url = 'https://nid.naver.com/nidlogin.login?url=https://search.naver.com/search.naver?ie=UTF-8&sm=whl_hty&query=%EB%AF%B8%EC%8A%A4%ED%84%B0%ED%8A%B8%EB%A1%AF+%EC%95%8C%ED%8E%98%EC%8A%A4'
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


while True:
    driver.get(login_url)
    driver.implicitly_wait(10)

    clipboard_input('//*[@id="id"]', config()['id'])
    clipboard_input('//*[@id="pw"]', config()['pwd'])
    driver.find_element_by_xpath('//*[@id="log.login"]').click()
    time.sleep(0.5)

    if driver.current_url == 'https://nid.naver.com/nidlogin.login':
        print('로그인에 실패했습니다. 유저 정보를 올바르게 입력 후 다시 실행해주세요.')
        driver.close()
        break

    print('페이지 접속 완료. 30초 대기합니다.')

    time.sleep(30)
    count += 1
    print(f'30초 대기 완료. {count}번 실행하였습니다.')
