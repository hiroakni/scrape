
import time
import logic.line_notify_logic as line
from selenium.webdriver.common.by import By

def main(browser, loop_limit, time_sleep, token, notify_goods_list, overlap_limit):
    try:
        parentDatas = browser.find_element(by=By.CLASS_NAME, value="content")
        datas = parentDatas.find_elements(by=By.CLASS_NAME, value="item")
    except Exception as e:
        line.main("find parent data exception", token)
        print(e)
        pass

    loopCount = 0
    for data in datas:
        try:
            if loopCount >= loop_limit:
                break
            else:
                price = data.find_element(by=By.CLASS_NAME, value="item-box__item-price").text.replace("\n", "")
                
                url = data.find_element(by=By.TAG_NAME, value="a").get_attribute("href")
                gooleChromeUrl = data.find_element(by=By.TAG_NAME, value="a").get_attribute("href").replace("https", "googlechrome")
                text = data.find_element(by=By.CLASS_NAME, value="link_search_title").find_element(by=By.TAG_NAME, value="span").text
                # 同じ商品の通知が何度も来ないようにする（前回の結果を一時的に格納して比較する）
                appendFlag = True
                if len(notify_goods_list) > 0:
                    for notifyed_goods in notify_goods_list:
                        if ((notifyed_goods["price"] == price) and (notifyed_goods["url"] == url) and (notifyed_goods["text"] == text)):
                            appendFlag = False
                            break
                if appendFlag == True:
                    notify_goods_list.append({"price": price, "url": url, "text": text})
                    line.main(url + "\n" + text + "\n" + price +  "\n" + "\n" + gooleChromeUrl, token)
            loopCount = loopCount + 1
                
        except Exception as e:
            line.main("element loop exception", token)
            print(e)
            pass

    browser.quit()
    print("END")
    print(notify_goods_list)
    print(len(notify_goods_list))
    time.sleep(time_sleep)

    if len(notify_goods_list) > overlap_limit:
        notify_goods_list = []

    return notify_goods_list