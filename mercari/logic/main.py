import time
from selenium import webdriver
import logic.scraping_logic as scraping
import logic.line_notify_logic as line
from selenium.webdriver.chrome.options import Options
# required
import chromedriver_binary

def main(token, search_url, loop_limit, price_upper_limit, price_lower_limit, time_sleep, overlap_limit):
    try:
        work_notify_goods_list = []
        while True:            
            option = webdriver.ChromeOptions()
            option.add_argument("--headless")  
            option.add_argument("--incognito")
            option.add_argument('--window-size=1024,768')
            browser = webdriver.Chrome(options=option)

            print("started auto search")
            
            try:
                browser.get(search_url)
                # 画面描画待ち
                time.sleep(5)

            except Exception as e:
                line.main("browser get exception", token)
                print(e)
                break

            print("START")
            returned_notify_goods_list = scraping.main(browser, loop_limit, price_upper_limit, price_lower_limit, time_sleep, token, work_notify_goods_list, overlap_limit)
            work_notify_goods_list = returned_notify_goods_list
    except Exception as e:
        print(e)
        line.main("main loop exception", token)
