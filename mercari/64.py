import main as logic

LINE_NOTIFY_TOKEN = "vr6Spdwh35gYsf0vyJWnbmcbV9e2twEEqIaWzCdFPH4"
SEARCH_URL = "https://jp.mercari.com/search?keyword=%E3%83%8B%E3%83%B3%E3%83%86%E3%83%B3%E3%83%89%E3%83%BC64%20%E6%9C%AC%E4%BD%93&status=on_sale"
LOOP_LIMIT = 10
PRICE_UPPER_LIMIT = 5001
PRICE_LOWER_LIMIT = 1999
TIME_SLEEP = 3600
OVERLAP_LIMIT = 10

logic.main(LINE_NOTIFY_TOKEN, SEARCH_URL, LOOP_LIMIT, PRICE_UPPER_LIMIT, PRICE_LOWER_LIMIT, TIME_SLEEP, OVERLAP_LIMIT)