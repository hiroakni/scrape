import time
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome import service as fs
# from selenium.webdriver.chrome.options import Options
# from selenium.common.exceptions import WebDriverException
# import chromedriver_binary
import scraping_logic as scraping
import line_notify_logic as line

# required
import chromedriver_binary

def main(token, search_url, loop_limit, price_upper_limit, price_lower_limit, time_sleep, overlap_limit):
    try:
        notify_goods_list = []
        while True:
            browser = webdriver.Chrome()

            print("started auto search")
            
            try:
                browser.get(search_url)
                # browser.get("https://jp.mercari.com/search?keyword=gameboy%20advance%20sp&status=on_sale")
                # element = browser.find_element(by=By.XPATH, value="//*[@id='__next']/div/header/div/div/div[3]/mer-autocomplete/div[1]/form/div[1]/input")
                # element.send_keys("gameboy advance sp\n")

            except Exception as e:
                line.main("browser get exception", token)
                print(e)
                break

            # 画面描画待ち
            print("frist waiting...")
            time.sleep(10)
            returned_notify_goods_list = scraping.main(browser, loop_limit, price_upper_limit, price_lower_limit, time_sleep, token, notify_goods_list, overlap_limit)
            notify_goods_list = returned_notify_goods_list
            
    except Exception as e:
        print(e)
        line.main("main loop exception", token)
        pass
