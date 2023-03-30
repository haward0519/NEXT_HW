from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup 


# 디버깅 모드
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver = "./chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, options= chrome_options)

# 실행할 웹페이지 불러오기 (멜론 차트)
driver.get("https://www.melon.com/index.htm")

# 좋아하는 가수의 곡명 10개
searchbox = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/fieldset/input[1]')
time.sleep(3)
searchbox.send_keys("잔나비")
time.sleep(3)
searchbox.send_keys(Keys.ENTER)
time.sleep(3)

driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

search_result = soup.select_one('tbody')
song_list = search_result.select('a.fc_gray')

titles = []
for song in song_list[:5]:
    title = song['title']
    titles.append(title)

print(titles)
