from copycat_bot.data_preparation.telegram import open_json, extract_text_by_user, save_text_by_user


if __name__ == '__main__':
  source = open_json('telegram.json')
  text_by_user = extract_text_by_user(source)
  for user_id in text_by_user.keys():
    save_text_by_user(user_id, text_by_user[user_id])
