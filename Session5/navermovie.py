from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
from selenium.webdriver.common.action_chains import ActionChains



# 디버깅 모드
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver = "./chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, options= chrome_options)

# 실행할 웹페이지 불러오기 (네이버 차트)
driver.get("https://movie.naver.com/")




# 멜론 차트 버튼 클릭 
chartbtn = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/div[1]/div/div/ul/li[3]/a')
chartbtn.click()
time.sleep(3)

# 1위부터 20위까지 가져오기{}
for i in range(2,12):
   titles = driver.find_element(By.XPATH,f"/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[{i}]/td[2]/div/a").text
   print(titles)
time.sleep(1)

for i in range(13,23):
   titles = driver.find_element(By.XPATH,f"/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[{i}]/td[2]/div/a").text
   print(titles)
   time.sleep(1)


for i in range(2,12):
    try:
        driver.find_element(By.XPATH,f'/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[{i}]/td[2]/div/a').click()
        outline = driver.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/div[1]/div[2]/div[1]/dl/dd[1]/p").text
        director = driver.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/div[1]/div[2]/div[1]/dl/dd[2]/p").text
        grade = driver.find_element(By.XPATH, '/html/body/div/div[4]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/a/div/span').text

        print ("개요 :", outline, "감독 :", director,"평점 :", grade)

        driver.back()
        time.sleep(1)

    except:
        print("개봉전 영화입니다.")
        
        driver.back()
        time.sleep(1)

        continue

for i in range(13,23):
    try:
        driver.find_element(By.XPATH,f'/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[{i}]/td[2]/div/a').click()
        outline = driver.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/div[1]/div[2]/div[1]/dl/dd[1]/p").text
        director = driver.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/div[1]/div[2]/div[1]/dl/dd[2]/p").text
        grade = driver.find_element(By.XPATH, '/html/body/div/div[4]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/a/div/span').text

        print ("개요 :", outline, "감독 :", director,"평점 :", grade)

        driver.back()
        time.sleep(1)

    except:
        print("개봉전 영화입니다.")
        
        driver.back()
        time.sleep(1)
        
        continue

searchbox = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/fieldset/div/span/input')
time.sleep(3)
searchbox.send_keys("스즈메의 문단속")
time.sleep(3)
searchbox.send_keys(Keys.ENTER)
time.sleep(3)

driver.find_element(By.XPATH,'/html/body/div/div[4]/div/div/div/div/div[1]/ul[2]/li/p/a').click()
title = driver.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/div[1]/div[2]/div[1]/h3/a[1]").text
director = driver.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/div[1]/div[2]/div[1]/dl/dd[2]/p").text

for c in range(0,3):
    driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

grade = driver.find_element(By.XPATH, '/html/body/div/div[4]/div[2]/div[1]/div[4]/div[5]/div[2]/div[2]/div[1]/div/div/em').text
Count = driver.find_element(By.XPATH, '/html/body/div/div[4]/div[2]/div[1]/div[4]/div[5]/div[2]/div[3]/strong/em').text

file = open('navermovie.csv', mode="w", newline='')
writer = csv.writer(file)

writer.writerow(("제목", "감독", "성적", "리뷰수"))

writer.writerow((title, director, grade, Count))


file.close()

