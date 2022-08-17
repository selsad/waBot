# importing libraries
from email import message
from lib2to3.pgen2 import driver
from optparse import Option
import os
import sys
import time
from tkinter import N
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from tkinter import *

driver = None
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
qrCode = '//*[@id="app"]/div/div/div[2]/div[1]/div/div[2]/div/canvas'

def createDriver(user_agent_option):
    options = webdriver.ChromeOptions()
    options.add_argument(f'user-agent={user_agent_option}')
    # options.add_argument('--headless')
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    url = 'https://web.whatsapp.com/'
    driver.get(url)

def captureQR(qrCodeXPath):
    try:
        qrCodeElement = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, qrCodeXPath)))
        qrCodeElement.screenshot('qrCode.png')
        print('QR Code Captured')
    except:
        print('QR Code not found')

def main():
    createDriver(user_agent)
    captureQR(qrCode)
    #experimental code
    ws = Tk()
    ws.title('PythonGuides')
    ws.geometry('500x500')

    canvas = Canvas(
        ws,
        width = 500, 
        height = 500
        )      
    canvas.pack()      
    img = PhotoImage(file='qrCode.png')    
    canvas.create_image(
        10,
        10, 
        anchor=NW, 
        image=img
        )      
    ws.mainloop() 
    # end of experimental code

if __name__ == '__main__':
    main()