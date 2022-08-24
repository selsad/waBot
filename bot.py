from driver import driver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
save_dialog_ok_button = '//*[@id="main"]/footer/div[2]/div/div[1]/div/div/div[2]/div[3]/div'
search_box = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'


# def findElement(element_xpath, isNecessaryToWait):
#     if isNecessaryToWait:
#         while True:
#             try:
#                 # find search box by xpath
#                 return driver.find_element(By.XPATH, element_xpath)
#             except:
#                 # if search_box doesn't exist, do nothing
#                 pass
#     else:
#         try:
#             return driver.find_element(By.XPATH, element_xpath)
#         except:
#             return None

def findElement(element_xpath, isNecessaryToWait):
    if isNecessaryToWait:
        while True:
            try:
                return WebDriverWait(driver, 200).until(
                    EC.presence_of_element_located((By.XPATH, element_xpath)))
            except:
                pass
    else:
        try:
            return WebDriverWait(driver, 200).until(
                EC.presence_of_element_located((By.XPATH, element_xpath)))
        except:
            return None
