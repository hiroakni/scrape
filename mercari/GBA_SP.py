import main as logic

LINE_NOTIFY_TOKEN = "K2wJ45DMRNkgT97IfW6pVyXMLyiwytQruXZsav9AIhU"
SEARCH_URL = "https://jp.mercari.com/search?keyword=gameboy%20advance%20sp&status=on_sale"
LOOP_LIMIT = 10
PRICE_UPPER_LIMIT = 6501
PRICE_LOWER_LIMIT = 2999
# 5minutes
TIME_SLEEP = 180

OVERLAP_LIMIT = 10

logic.main(LINE_NOTIFY_TOKEN, SEARCH_URL, LOOP_LIMIT, PRICE_UPPER_LIMIT, PRICE_LOWER_LIMIT, TIME_SLEEP, OVERLAP_LIMIT)
