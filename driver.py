# importing libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = None
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
url = 'https://web.whatsapp.com/'


def createDriver(user_agent_option=user_agent):
    global driver
    global url
    options = webdriver.ChromeOptions()
    options.add_argument(f'user-agent={user_agent_option}')
    # options.add_argument('--headless')
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)
    driver.get(url)

def getDriver():
    global driver
    if driver is None:
        createDriver()
        return driver
    else:
        return driver


