import os
from slack import WebClient


def send_message(message):

  slack_token = os.environ.get('SLACK_API_TOKEN')
  client = WebClient(token=slack_token)
  
  client.chat_postMessage(
    channel="ohad_alerts",
    text=message,
  )