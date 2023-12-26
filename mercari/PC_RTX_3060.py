import logic.main as scraping

LINE_NOTIFY_TOKEN = "lGntROvMPypBNHkw0NepRbstQIKgMYIbZ9EVlBdZZsE"
SEARCH_URL = "https://jp.mercari.com/search?keyword=rtx3060%E3%80%80%E3%82%B0%E3%83%A9%E3%83%9C&status=on_sale"
# 取得件数指定
LOOP_LIMIT = 10
# 高値
PRICE_UPPER_LIMIT = 31001
# 安値
PRICE_LOWER_LIMIT = 9999
# ループ時間
TIME_SLEEP = 300
# 同商品格納件数閾値
OVERLAP_LIMIT = 10

scraping.main(LINE_NOTIFY_TOKEN, SEARCH_URL, LOOP_LIMIT, PRICE_UPPER_LIMIT, PRICE_LOWER_LIMIT, TIME_SLEEP, OVERLAP_LIMIT)
