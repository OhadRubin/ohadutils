import os
from slack import WebClient

CACHE_PATH = user_cache_dir("alerts", "alerts")

def send_message(message):

  slack_token = os.environ.get('SLACK_API_TOKEN')
  client = WebClient(token=slack_token)
  
  client.chat_postMessage(
    channel="ohad_alerts",
    text=message,
  )