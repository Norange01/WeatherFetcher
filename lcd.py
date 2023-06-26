from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import selenium
import datetime
import requests


driver =webdriver.Chrome()
driver.get('https://www.theweathernetwork.com/ca/hourly-weather-forecast/ontario/milton')

driver.implicitly_wait(5)

morningTemp = driver.find_element(
  By.XPATH,
  '/html/body/div[5]/div[2]/div[3]/div[2]/div/div/div[2]/div/div[1]/div[4]/div[2]/div[2]/span[2]'
).text
print(morningTemp)

afternoonTemp = driver.find_element(
  By.XPATH,
  '/html/body/div[5]/div[2]/div[3]/div[2]/div/div/div[2]/div/div[2]/div[4]/div[2]/div[2]/span[2]'
).text
print(afternoonTemp)

nightTemp = driver.find_element(
  By.XPATH,
  '/html/body/div[5]/div[2]/div[3]/div[2]/div/div/div[2]/div/div[3]/div[4]/div[2]/div[2]/span[2]'
).text
print(nightTemp)

morningDesc = driver.find_element(
  By.XPATH,
  '/html/body/div[5]/div[2]/div[3]/div[2]/div/div/div[2]/div/div[1]/div[2]'
).text
print(morningDesc)

afternoonDesc = driver.find_element(
  By.XPATH,
  '/html/body/div[5]/div[2]/div[3]/div[2]/div/div/div[2]/div/div[2]/div[2]'
).text
print(afternoonDesc)

nightDesc = driver.find_element(
  By.XPATH,
  '/html/body/div[5]/div[2]/div[3]/div[2]/div/div/div[2]/div/div[3]/div[2]'
).text
print(nightDesc)

tempsline = "MO"
if (morningTemp.startswith('-')):
  tempsline += morningTemp
else:
  tempsline += " "
  tempsline += morningTemp
tempsline += " AN"
if (afternoonTemp.startswith('-')):
  tempsline += afternoonTemp
else:
  tempsline += " "
  tempsline += afternoonTemp
tempsline += " N"
if (nightTemp.startswith('-')):
  tempsline += nightTemp
else:
  tempsline += " "
  tempsline += nightTemp

print(tempsline)

##############################################################

driver.get(
  'https://www.theweathernetwork.com/ca/severe-weather-outlook/ontario/milton')
driver.implicitly_wait(5)

#TS
thunderstorm = driver.find_element(
  By.XPATH,
  '/html/body/div[4]/div[4]/div[3]/div[2]/div[2]/div/div[1]/div[1]/div/div[2]/div[2]'
).text

#S
snowfall = driver.find_element(
  By.XPATH,
  '/html/body/div[4]/div[4]/div[3]/div[2]/div[2]/div/div[1]/div[1]/div/div[3]/div[2]'
).text

#FR
freezingrain = driver.find_element(
  By.XPATH,
  '/html/body/div[4]/div[4]/div[3]/div[2]/div[2]/div/div[1]/div[1]/div/div[4]/div[2]'
).text

#W
wind = driver.find_element(
  By.XPATH,
  '/html/body/div[4]/div[4]/div[3]/div[2]/div[2]/div/div[1]/div[1]/div/div[5]/div[2]'
).text

#R
rain = driver.find_element(
  By.XPATH,
  '/html/body/div[4]/div[4]/div[3]/div[2]/div[2]/div/div[1]/div[1]/div/div[6]/div[2]'
).text

risklabels = ["TS", "S", "FR", "W", "R"]
risks = [thunderstorm, snowfall, freezingrain, wind, rain]
risksline = ""

for i in range(5):
  if (int(risks[i]) > 0):
    if (len(risksline) != 0):
      risksline += " "
    if (risks[i] == "10"):
      risksline += "9"
    else:
      risksline += risks[i]
print("riskline")
print(risksline)

#################################################################

driver.get(
  'https://www.icnamilton.com/')
driver.implicitly_wait(5)

fajr = driver.find_element(
  By.XPATH,
  '/html/body/div/div[3]/div/article/div/div/div/div[1]/div/div[1]/div/div/div/table/tbody/tr[2]/td[2]'
).text
sunrise = driver.find_element(
  By.XPATH,
  '/html/body/div/div[3]/div/article/div/div/div/div[1]/div/div[1]/div/div/div/table/tbody/tr[2]/td[3]'
).text
dhuhr = driver.find_element(
  By.XPATH,
  '/html/body/div/div[3]/div/article/div/div/div/div[1]/div/div[1]/div/div/div/table/tbody/tr[2]/td[4]'
).text
asr = driver.find_element(
  By.XPATH,
  '/html/body/div/div[3]/div/article/div/div/div/div[1]/div/div[1]/div/div/div/table/tbody/tr[2]/td[5]'
).text
maghrib = driver.find_element(
  By.XPATH,
  '/html/body/div/div[3]/div/article/div/div/div/div[1]/div/div[1]/div/div/div/table/tbody/tr[2]/td[6]'
).text
isha = driver.find_element(
  By.XPATH,
  '/html/body/div/div[3]/div/article/div/div/div/div[1]/div/div[1]/div/div/div/table/tbody/tr[2]/td[7]'
).text

#prayerline1=x:xx|x:xx|xx:xx
#prayerline2=x:xx|x:xx|xx:xx

#remove first digit of some prayers:
fajr = fajr[1:5]
sunrise = sunrise[1:5]
dhuhr = dhuhr[0:5]
asr = asr[1:5]
maghrib = maghrib[1:5]
isha = isha[0:5]

prayerline1 = fajr+"|"+sunrise+"|"+dhuhr
prayerline2= asr+"|"+maghrib+"|"+isha
print(prayerline1)
print(prayerline2)
driver.quit()