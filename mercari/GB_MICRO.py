import logic.main as scraping
import os
from dotenv import load_dotenv

load_dotenv()

LINE_NOTIFY_TOKEN = os.environ['GB_LINE_NOTIFY_TOKEN']
SEARCH_URL = os.environ['GB_MICRO_SEARCH_URL']
LOOP_LIMIT = int(os.environ['GB_MICRO_LOOP_LIMIT'])
PRICE_UPPER_LIMIT = int(os.environ['GB_MICRO_PRICE_UPPER_LIMIT'])
PRICE_LOWER_LIMIT = int(os.environ['GB_MICRO_PRICE_LOWER_LIMIT'])
TIME_SLEEP = int(os.environ['GB_MICRO_TIME_SLEEP'])
OVERLAP_LIMIT = int(os.environ['GB_MICRO_OVERLAP_LIMIT'])

scraping.main(LINE_NOTIFY_TOKEN, SEARCH_URL, LOOP_LIMIT, PRICE_UPPER_LIMIT, PRICE_LOWER_LIMIT, TIME_SLEEP, OVERLAP_LIMIT)
