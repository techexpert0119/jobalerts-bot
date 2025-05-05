import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Slack configuration
SLACK_BOT_TOKEN = os.environ.get('SLACK_BOT_TOKEN')
JOB_ALERTS_CHANNEL = os.environ.get('JOB_ALERTS_CHANNEL')
DAILY_REPORT_CHANNEL = os.environ.get('DAILY_REPORT_CHANNEL')

# File storage settings
COUNT_FILE = 'applied_count.txt'

# Application settings
DAILY_TARGET_COUNT = int(os.environ.get('DAILY_TARGET_COUNT', 60))  # Target number of applications per day

# Flask settings
DEBUG = True
PORT = 5000 