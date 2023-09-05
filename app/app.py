from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(ChromeDriverManager(driver_version="114.0.5735.90").install())
driver.get("https://google.com")
sleep(5)

