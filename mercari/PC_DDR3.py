import main as logic

LINE_NOTIFY_TOKEN = "lGntROvMPypBNHkw0NepRbstQIKgMYIbZ9EVlBdZZsE"
SEARCH_URL = "https://jp.mercari.com/search?keyword=ddr3%208gb&category_id=1156&status=on_sale"
# 取得件数指定
LOOP_LIMIT = 10
# 高値
PRICE_UPPER_LIMIT = 1001
# 安値
PRICE_LOWER_LIMIT = 299
# ループ時間
TIME_SLEEP = 100
# 同商品格納件数閾値
OVERLAP_LIMIT = 100

logic.main(LINE_NOTIFY_TOKEN, SEARCH_URL, LOOP_LIMIT, PRICE_UPPER_LIMIT, PRICE_LOWER_LIMIT, TIME_SLEEP, OVERLAP_LIMIT)

