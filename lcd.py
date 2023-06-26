from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import selenium
import requests
import drivers
from datetime import datetime

global tempsline
global risksline

global prayerline1
global prayerline2

t = datetime.now()

display = drivers.Lcd()

updateHour = 6
updateMinute = 0

def getRiskLabel(datatitle):
  if(datatitle=="Thunderstorm Risk"):
    return "TS"
  elif(datatitle=="Rainfall Risk"):
    return "R"
  elif(datatitle=="Snowfall Risk"):
    return "S"
  elif(datatitle=="Freezing Rain Risk"):
    return "FR"
  elif(datatitle=="Wind Risk"):
    return "W"
  else:
    return "?"

def getData():
  global tempsline
  global risksline

  global prayerline1
  global prayerline2
  display.lcd_clear()
  display.lcd_display_string("Collecting data", 1)
  print("######################")
  print(t.day)

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

  risks = [thunderstorm, snowfall, freezingrain, wind, rain]
  risksline = ""

  for i in range(5):
    riskTitleX="/html/body/div[4]/div[4]/div[3]/div[2]/div[2]/div/div[1]/div[1]/div/div["+str(i+2)+"]/div[1]/span[2]"
    riskTitle=driver.find_element(By.XPATH,riskTitleX).text
    riskLabel=getRiskLabel(riskTitle)
    if (int(risks[i]) > 0):
      if (len(risksline) != 0):
        risksline += " "
      if (risks[i] == "10"):
        risksline+=riskLabel
        risksline += "9"
      else:
        risksline+=riskLabel
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

  prayerline1 = fajr+"|"+sunrise+"|"+dhuhr+" "
  prayerline2= asr+"|"+maghrib+"|"+isha+" "
  print(prayerline1)
  print(prayerline2)
  driver.quit()

getData()
lastDayUpdated= t.day
display.lcd_clear()

while(True):
  if(t.hour==updateHour and t.minute==updateMinute):
      if(lastDayUpdated!=t.day):
        getData()
        lastDayUpdated= t.day
        
  display.lcd_display_string(tempsline, 1)  # Write line of text to first line of display
  display.lcd_display_string(risksline,2)
  sleep(5)
  display.lcd_clear()
  display.lcd_display_string(prayerline1, 1)  # Write line of text to first line of display
  display.lcd_display_string(prayerline2,2)
  sleep(5)
  display.lcd_clear()
  t = datetime.now()

