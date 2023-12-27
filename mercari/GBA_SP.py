import logic.main as scraping
import os
from dotenv import load_dotenv

load_dotenv()

LINE_NOTIFY_TOKEN = os.environ['GB_LINE_NOTIFY_TOKEN']
SEARCH_URL = os.environ['GBA_SP_SEARCH_URL']
LOOP_LIMIT = int(os.environ['GBA_SP_LOOP_LIMIT'])
PRICE_UPPER_LIMIT = int(os.environ['GBA_SP_PRICE_UPPER_LIMIT'])
PRICE_LOWER_LIMIT = int(os.environ['GBA_SP_PRICE_LOWER_LIMIT'])
TIME_SLEEP = int(os.environ['GBA_SP_TIME_SLEEP'])
OVERLAP_LIMIT = int(os.environ['GBA_SP_OVERLAP_LIMIT'])

scraping.main(LINE_NOTIFY_TOKEN, SEARCH_URL, LOOP_LIMIT, PRICE_UPPER_LIMIT, PRICE_LOWER_LIMIT, TIME_SLEEP, OVERLAP_LIMIT)
