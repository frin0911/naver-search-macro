from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import json
import random

driver = webdriver.Chrome('chromedriver')
count = 0
base_url = 'https://naver.com'
login_url = 'https://nid.naver.com/nidlogin.login?url=https://search.naver.com/search.naver?ie=UTF-8&sm=whl_hty&query=%EB%AF%B8%EC%8A%A4%ED%84%B0%ED%8A%B8%EB%A1%AF+%EC%95%8C%ED%8E%98%EC%8A%A4'
search_url = 'https://search.naver.com/search.naver?query=미스터트롯+알페스'


def config():
    with open('config.json', 'r', encoding='utf-8-sig') as f:
        cfg = json.load(f)
    return cfg
try:
    with open('./config/config.json') as file:
        data = json.load(file)
        id = data["id"]
        pw = data["pwd"]
    driver.get(login_url)
    driver.find_element_by_id('id').send_keys(id)    
    driver.find_element_by_id('pw').send_keys(pw)
    driver.find_element_by_xpath('//*[@id="log.login"]').click()
    time.sleep(15.0)

    if driver.current_url == 'https://nid.naver.com/nidlogin.login':
        print('로그인에 실패했습니다. 유저 정보를 올바르게 입력 후 다시 실행해주세요.')
        driver.close()

while True:      
    driver.get(search_url) # 접속
    
    rate = random.randint(1, 3)
    for i in range(1, rate):
        page_value = random.randint(1, 7)
        driver.find_element_by_xpath(f'//*[@id="main_pack"]/section[1]/div/div[2]/panel-list/div/ul/li[{page_value}]').click()
        sleep_interval = random.randint(1, 5)
        time.sleep(sleep_interval) # 대기
        #FIXME: 여기서 계속 IndexError남(IndexError: list index out of range)
        driver.switch_to_window(driver.window_handles[1]) # 2번째 탭으로 변경
        driver.close() # 2번째 탭 닫기
        driver.switch_to_window(driver.window_handles[0]) # 1번쨰 탭으로 변경
    print('페이지 접속 완료. 30초 대기합니다.')

    time.sleep(30.0)
    count += 1
    print(f'30초 대기 완료. {count}번 실행하였습니다.')
