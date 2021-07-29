from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bot_settings import chrome_user, chromedriver_path
import os
clear = lambda: os.system('cls')

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=' + chrome_user + ' Data/Default')
options.add_argument('--profile-directory=Default')

def sender(msg, phones_list):
    counter = 0
    driver = webdriver.Chrome(chromedriver_path, options = options)
    for phone in phones_list:        
        try:
            url='https://web.whatsapp.com/send?phone='+phone
            driver.get(url)
            time.sleep(5)
            message_box = driver.find_element_by_xpath('//div[@id="main"]/footer[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]')
            for m in msg:
                message_box.send_keys(m + Keys.SHIFT + Keys.ENTER)
            send_button = driver.find_element_by_xpath('//button[@class="_4sWnG"]')
            send_button.click()
            time.sleep(1)
            counter += 1
            clear()
            print(counter)
        except:
            continue
    
    print('Your message sent to {} number.'.format(counter))
    driver.quit()

    #C:/Users/Rodi/AppData/Local/Google/Chrome/User
