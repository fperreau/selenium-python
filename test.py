from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options=
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(chrome_options=options)
driver.get("http://www.python.org")

keyword = input("enter a character or press enter to continue")
driver.quit()
