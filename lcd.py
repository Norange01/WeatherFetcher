from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FXService
from pyvirtualdisplay import Display

display = Display(visible=0, size=(1024, 768))
display.start()

driver_path = './webdrivers/geckodriver'
driver = webdriver.Firefox(service=FXService(driver_path))
driver.get('http://raspberrypi.stackexchange.com/')
driver.quit()

display.stop()