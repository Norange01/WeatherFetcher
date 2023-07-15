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

updateHour1 = 6
updateMinute1 = 0
updateHour2 = 18
updateMinute2 = 0

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
  
def getTempLabels(datatitle):
  datatitle_words = datatitle.split(" ")
  timesArr = ["M", "AN", "E"]
  if(datatitle_words[1].lower()=="morning"):
    timesArr = ["M", "AN", "E"]
  elif(datatitle_words[1].lower()=="afternoon"):
    timesArr = ["AN", "E", "N"]
  elif(datatitle_words[1].lower()=="evening"):
    timesArr = ["E", "N", "M"]
  elif(datatitle_words[1].lower()=="overnight"):
    timesArr = ["N", "M", "AN"]
  return timesArr

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

  driver.implicitly_wait(10)

  morningTemp = driver.find_element(By.CLASS_NAME, "today").find_element(By.CLASS_NAME,"feels-like").find_element(By.CLASS_NAME, "value").text
  print(morningTemp)

  afternoonTemp = driver.find_element(By.CLASS_NAME, "afternoon").find_element(By.CLASS_NAME,"feels-like").find_element(By.CLASS_NAME, "value").text
  print(afternoonTemp)

  nightTemp = driver.find_element(By.CLASS_NAME, "overnight").find_element(By.CLASS_NAME,"feels-like").find_element(By.CLASS_NAME, "value").text
  print(nightTemp)

  timeTitle=driver.find_element(By.CLASS_NAME, "today").find_element(By.CLASS_NAME,"title").text
  TimeArr = getTempLabels(timeTitle)
  tempsline = TimeArr[0]
  if (morningTemp.startswith('-')):
    tempsline += morningTemp
  else:
    tempsline += " "
    tempsline += morningTemp
  tempsline += " "+TimeArr[1]
  if (afternoonTemp.startswith('-')):
    tempsline += afternoonTemp
  else:
    tempsline += " "
    tempsline += afternoonTemp
  tempsline += " "+TimeArr[2]
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
  thunderstorm = driver.find_element(By.CLASS_NAME, "data-table").find_element(
    By.XPATH,
    './/div/div[2]/div[2]'
  ).text

  #S
  snowfall = driver.find_element(By.CLASS_NAME, "data-table").find_element(
    By.XPATH,
    './/div/div[3]/div[2]'
  ).text

  #FR
  freezingrain = driver.find_element(By.CLASS_NAME, "data-table").find_element(
    By.XPATH,
    './/div/div[4]/div[2]'
  ).text

  #W
  wind = driver.find_element(By.CLASS_NAME, "data-table").find_element(
    By.XPATH,
    './/div/div[5]/div[2]'
  ).text

  #R
  rain = driver.find_element(By.CLASS_NAME, "data-table").find_element(
    By.XPATH,
    './/div/div[6]/div[2]'
  ).text

  risks = [thunderstorm, snowfall, freezingrain, wind, rain]
  risksline = ""

  for i in range(5):
    riskTitleX=".//div["+str(i+2)+"]/div[1]/span[2]"
    riskTitle=driver.find_element(By.CLASS_NAME, "data-table").find_element(By.XPATH,riskTitleX).text
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
    'https://timesprayer.com/en/prayer-times-in-milton.html')
  driver.implicitly_wait(5)

  fajr = driver.find_element(By.CLASS_NAME, "ptTable").find_element(
    By.XPATH,
    './/tbody/tr[1]/td[2]'
  ).text
  sunrise = driver.find_element(By.CLASS_NAME, "ptTable").find_element(
    By.XPATH,
    './/tbody/tr[2]/td[2]'
  ).text
  dhuhr = driver.find_element(By.CLASS_NAME, "ptTable").find_element(
    By.XPATH,
    './/tbody/tr[3]/td[2]'
  ).text
  asr = driver.find_element(By.CLASS_NAME, "ptTable").find_element(
    By.XPATH,
    './/tbody/tr[4]/td[2]'
  ).text
  maghrib = driver.find_element(By.CLASS_NAME, "ptTable").find_element(
    By.XPATH,
    './/tbody/tr[5]/td[2]'
  ).text
  isha = driver.find_element(By.CLASS_NAME, "ptTable").find_element(
    By.XPATH,
    './/tbody/tr[6]/td[2]'
  ).text

  #prayerline1=x:xx|x:xx|xx:xx
  #prayerline2=x:xx|x:xx|xx:xx

  #remove first digit of some prayers:
  fajr = fajr[0:4]
  sunrise = sunrise[0:4]
  dhuhr = dhuhr[0:5]
  asr = asr[0:4]
  maghrib = maghrib[0:4]
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
  if((t.hour==updateHour1 and t.minute==updateMinute1) or (t.hour==updateHour2 and t.minute==updateMinute2)):
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

