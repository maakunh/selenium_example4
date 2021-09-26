#covid19_get.py for Windows
#Author: Masafumi Hiura
#This code access covid19 web site of toyokeizai.net in Japan, and get screenshot of the web page.
#Japanese site is https://toyokeizai.net/sp/visual/tko/covid19/
#English site is https://toyokeizai.net/sp/visual/tko/covid19/en.html
#You need to install selenium by using pip before execute this code.
#You need to download chromedriver for your OS.
#This code see select tag(id="select-prefecture") of html, and get screenshot of the result of prefecture one by one.

from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import datetime

dt_now = datetime.datetime.now()
dt_now_s = dt_now.strftime('%Y%m%d%H%M%S')

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('.\\chromedriver.exe',options=options)

driver.get('https://toyokeizai.net/sp/visual/tko/covid19/')
w = driver.execute_script("return document.body.scrollWidth;")
h = driver.execute_script("return document.body.scrollHeight;")
driver.set_window_size(w, h)
driver.execute_script('window.scrollTo(0, document.body.scrollWidth);')
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
dropdown = driver.find_element_by_id('select-prefecture')
select = Select(dropdown)

all_options = select.options
for option in all_options:
    print(option.text)
    print(option.get_attribute('outerHTML'))
    print(option.get_attribute('value'))
    print('----------------------------')
    select.select_by_value(option.get_attribute('value')) #
    driver.save_screenshot(".\\screen_shot\\" + dt_now_s + "_" + option.get_attribute('value') + ".png")
    time.sleep(2)

driver.quit()
