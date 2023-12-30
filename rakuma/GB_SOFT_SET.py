import logic.main as scraping
import os
from dotenv import load_dotenv

load_dotenv()

LINE_NOTIFY_TOKEN = os.environ['RKM_GB_LINE_NOTIFY_TOKEN']
LOOP_LIMIT = int(os.environ['RKM_GB_SOFT_LOOP_LIMIT'])
PRICE_UPPER_LIMIT = os.environ['RKM_GB_SOFT_SET_PRICE_UPPER_LIMIT']
PRICE_LOWER_LIMIT = os.environ['RKM_GB_SOFT_SET_PRICE_LOWER_LIMIT']
TIME_SLEEP = int(os.environ['RKM_GB_SOFT_TIME_SLEEP'])
OVERLAP_LIMIT = int(os.environ['RKM_GB_SOFT_OVERLAP_LIMIT'])
SEARCH_URL = os.environ['RKM_GB_SOFT_SET_SEARCH_URL'] + "&min=" + PRICE_LOWER_LIMIT + "&max=" + PRICE_UPPER_LIMIT

scraping.main(LINE_NOTIFY_TOKEN, SEARCH_URL, LOOP_LIMIT, TIME_SLEEP, OVERLAP_LIMIT)
