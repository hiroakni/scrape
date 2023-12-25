import main as logic

LINE_NOTIFY_TOKEN = "bVepr7jzQ0yW32BZQEDfqZr7d0hIDFTEd3O4wjeaZXo"
SEARCH_URL = "https://jp.mercari.com/search?keyword=ゲームボーイミクロ%20本体&status=on_sale"
# 取得件数指定
LOOP_LIMIT = 10
# 高値
PRICE_UPPER_LIMIT = 14001
# 安値
PRICE_LOWER_LIMIT = 3999
# ループ時間
TIME_SLEEP = 300
# 同商品格納件数閾値
OVERLAP_LIMIT = 10


logic.main(LINE_NOTIFY_TOKEN, SEARCH_URL, LOOP_LIMIT, PRICE_UPPER_LIMIT, PRICE_LOWER_LIMIT, TIME_SLEEP, OVERLAP_LIMIT)

