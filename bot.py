#!/usr/bin/env python3
"""Example bot that returns a synchronous response."""

from flask import Flask, request, json
from api import server_api
import requests


app = Flask(__name__)
message = ""
action = ""
def call_api(user_action,event):
  command = apis[user_action][0]
  server_name = apis[user_action][2]
  url = command
  response = requests.get(url)
  response_data = response.json()
  code  = response_data['code']
  if code == 200:
    status = "success!"
  else:
    status = "something went wrong!,please contact sharon!"
  
  message = response.getContentText();
  message = "Command :" + request + "\nCommand executed " + "by: " + event.user.displayName +"\n" + "Server :" + server_name + "\nServer Status : " + action + "\nResponse Code: " + response.getResponseCode() + "\nResult: " + status;


def check_command(user_action):
  return user_action in apis

def send_notification():
  pass

apis = server_api()
@app.route('/', methods=['POST'])
def on_event():
  """Handles an event from Hangouts Chat."""
  event = request.get_json()
  if event['type'] == 'ADDED_TO_SPACE' and event['space']['type'] == 'ROOM':
    message = 'Thanks for adding me to "%s"!' % event['space']['displayName']
  elif event['type'] == 'MESSAGE':
    #bot logic
    command = event['message']['text']
    user_action = command.split('-').lower()
    if user_action == 'start':
      action = 'Started'
    elif user_action == 'stop':
      action = 'Stoppped'
    
    if check_command(user_action):
      call_api(user_action,event)
    else:
        message = message + " I do not understand your command, please refer the guide and retry! or you can ask sharon for help ! :)"
        return { "text": message }
      
      #send notification to google chat

  else:
    return json.jsonify({'text': message})


if __name__ == '__main__':
  app.run(port=8080, debug=True)