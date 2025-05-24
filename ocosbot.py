import openai
import os
from telegram.ext import Updater, MessageHandler, Filters

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_KEY")

openai.api_key = OPENAI_KEY

def ocos_reply(update, context):
    user_text = update.message.text
    prompt = f"""
You are OCOSBot, the official assistant of the OCOS blockchain ecosystem.
Always respond positively and helpfully in the same language as the user.
User message: {user_text}
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    answer = response['choices'][0]['message']['content']
    update.message.reply_text(answer)

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, ocos_reply))
    updater.start_polling()
    print("OCOSBot is running...")
    updater.idle()

if __name__ == '__main__':
    main()
