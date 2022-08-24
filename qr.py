# importing libraries
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

qrCode = '//*[@id="app"]/div/div/div[2]/div[1]/div/div[2]/div/canvas'


def captureQR(driver=None):
    qrCodeXPath = qrCode
    while True:
        sleep(5)
        try:
            qrCodeElement = WebDriverWait(driver, 200).until(
                EC.presence_of_element_located((By.XPATH, qrCodeXPath)))
            qrCodeElement.screenshot('assets/qrCode.png')
            print('QR Code Captured')
        except:
            driver.refresh()
            print('QR Code not found')
