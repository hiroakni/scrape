import main as logic

LINE_NOTIFY_TOKEN = "ksneiyQVa9YQRNC7lpzBEvTaRx9bCf7JWm93XdDOpjL"
SEARCH_URL = "https://jp.mercari.com/search?keyword=%E3%82%B2%E3%83%BC%E3%83%A0%E3%83%9C%E3%83%BC%E3%82%A4%20%E3%82%BD%E3%83%95%E3%83%88&status=on_sale&category_id=704"
# 取得件数指定
LOOP_LIMIT = 10
# 高値
PRICE_UPPER_LIMIT = 1001
# 安値
PRICE_LOWER_LIMIT = 299
# ループ時間
TIME_SLEEP = 100
# 同商品格納件数閾値
OVERLAP_LIMIT = 300

logic.main(LINE_NOTIFY_TOKEN, SEARCH_URL, LOOP_LIMIT, PRICE_UPPER_LIMIT, PRICE_LOWER_LIMIT, TIME_SLEEP, OVERLAP_LIMIT)
