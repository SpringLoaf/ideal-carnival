from selenium import webdriver
import pyperclip
from selenium.webdriver.common.by import By
import time
import re
from selenium.common import exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.install_addon('./ublock_origin-1.49.2.xpi', temporary=True)
driver.get("https://www.truepeoplesearch.com")

def main():
    temp = ""
    while True:
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "/html/body")))
        get_source = driver.find_element(By.XPATH, "/html/body").text
        numbers = re.findall("(\([0-9]{3}\) [0-9]{3}-[0-9]{4})", get_source)
        if not numbers:
            continue
        elif temp != numbers[0]:
            temp = numbers[0]
            print(numbers[0])
            pyperclip.copy(numbers[0])
        else:
            pass

while True:
    try:
        main()
            # x = WebDriverWait(driver, 900).until(EC.presence_of_all_elements_located((By.XPATH, "/html/body")))
            
    except exceptions.StaleElementReferenceException:
        pass
    except exceptions.NoSuchElementException:
        pass