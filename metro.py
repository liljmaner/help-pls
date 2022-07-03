
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium_stealth import stealth
import time
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
import csv

# options.add_argument("--headless")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path=r"C:\\parser\\chromedriver.exe")

stealth(driver,
        languages=["ru-RU", "ru"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

products = input("Продукт:")
url = "https://online.metro-cc.ru/search?q=" + products
driver.get(url)
name_list = []
subs = driver.find_element(By.ID, "products-inner") #base-product-name reset-link
status = subs.find_elements(By.XPATH, '//div[@class="base-product-item__content-details"]')
price = subs.find_elements(By.XPATH, '//span[@class="base-product-prices__actual-sum"]')
for statused in price:
        print(statused.text)
        with open("text.csv", 'a', newline='') as file:
                writer = csv.writer(file, delimiter=',')
                writer.writerow(
                        statused.text
                )

time.sleep(5)
driver.quit()
