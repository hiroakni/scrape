import time
from selenium import webdriver
from .scraping_logic import main as scraping
import sys
sys.path.append('../')
from common import line_notify as line
import json
# required
import chromedriver_binary

def main(token, search_url, loop_limit, time_sleep, overlap_limit, title, path):
    try:
        targetPath = path
        while True:
            try:
                with open(file=targetPath + title + ".json", mode="r", encoding="utf-8_sig") as file:
                    time.sleep(0.1)
                    work_notify_goods_list = json.load(file)
                    option = webdriver.ChromeOptions()
                    # option.add_argument("--headless")
                    option.add_argument("--blink-settings=imagesEnabled=false")  
                    option.add_argument("--incognito")
                    option.add_argument('--start-maximized')
                    browser = webdriver.Chrome(options=option)

                    print("started auto search")
                    
                    try:
                        browser.get(search_url)
                        # 画面描画待ち
                        time.sleep(10)

                    except Exception as e:
                        line.main("browser get exception: ", token, title)
                        print(e)
                        break

                    print("START")
                    returned_notify_goods_list = scraping(browser, loop_limit, token, work_notify_goods_list, overlap_limit, title)
                with open(file=targetPath + title + ".json", mode="w", encoding="utf-8_sig") as file:
                    file.write(json.dumps(returned_notify_goods_list))
                time.sleep(time_sleep)
            except Exception as e:
                print(e)
                line.main("json file exception: ", token, title)
                break
    except Exception as e:
        print(e)
        line.main("main loop exception", token, title)
