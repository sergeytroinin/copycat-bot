import json
import os

FROM_BLACKLIST = ['JokesBot', 'Kim', 'Combot', 'Sublime Bot', 'Дядя Стёпа милиционер', 'ЧГК', '✨🚙ActiveFlood🚙❄️', 'Jin Bot', 'Gamee']


def open_json(name):
  path = os.path.join(os.getcwd(), 'data', name)
  f = open(path)
  data = json.load(f)
  f.close()
  return data

def extract_text_by_user(source):
  extracted_text_by_user = {}
  for message in source['messages']:
    if 'from_id' not in message.keys() or 'forwarded_from' in message.keys():
      continue
    from_id = message['from_id']
    text = message['text']

    if not from_id or text == '' or type(text) is list or message['from'] in FROM_BLACKLIST:
      continue

    if from_id not in extracted_text_by_user.keys():
      extracted_text_by_user[from_id] = []
    extracted_text_by_user[from_id].append(text)

  return extracted_text_by_user


def save_text_by_user(user_id, text):
  path = os.path.join(os.getcwd(), 'data', f'{user_id}.txt')
  file = open(path, 'w')
  for line in text:
    file.write(f'{line}\n')
  file.close()