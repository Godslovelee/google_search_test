from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# #User default chrome
# service_args = Service()
# driver = webdriver.Chrome(service=service_args)
# driver.get("https://google.fcom")

service_args = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service_args)
driver.get("https://google.com")


