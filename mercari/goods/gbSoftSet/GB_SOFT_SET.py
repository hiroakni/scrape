import sys
sys.path.append('../../')
from logic import main as scraping
import os
from dotenv import load_dotenv

load_dotenv()

LINE_NOTIFY_TOKEN = os.environ['MRCR_GB_LINE_NOTIFY_TOKEN']
SEARCH_URL = os.environ['MRCR_GB_SOFT_SET_SEARCH_URL']
LOOP_LIMIT = int(os.environ['MRCR_GB_SOFT_LOOP_LIMIT'])
PRICE_UPPER_LIMIT = int(os.environ['MRCR_GB_SOFT_SET_PRICE_UPPER_LIMIT'])
PRICE_LOWER_LIMIT = int(os.environ['MRCR_GB_SOFT_SET_PRICE_LOWER_LIMIT'])
TIME_SLEEP = int(os.environ['MRCR_GB_SOFT_TIME_SLEEP'])
OVERLAP_LIMIT = int(os.environ['MRCR_GB_SOFT_OVERLAP_LIMIT'])

TITLE = "GB_SOFT_SET"
filePath = os.path.dirname(__file__) + "\\"

scraping.main(LINE_NOTIFY_TOKEN, SEARCH_URL, LOOP_LIMIT, PRICE_UPPER_LIMIT, PRICE_LOWER_LIMIT, TIME_SLEEP, OVERLAP_LIMIT, TITLE, filePath)
