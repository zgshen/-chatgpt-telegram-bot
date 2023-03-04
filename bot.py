import os
import openai
import telebot

bot = telebot.TeleBot(os.getenv('TELEGRAM_BOT_TOKEN'))


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(message.text)
    openai.api_key = os.getenv('OPENAI_API_KEY')
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message.text}
        ]
    )
    bot.send_message(message.chat.id, completion.choices[0].message.content, parse_mode='Markdown')


if __name__ == '__main__':
    print('==================>')
    print('start running....')
    print("test t:" + os.getenv('TELEGRAM_BOT_TOKEN'))
    bot.infinity_polling()
