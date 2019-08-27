import telebot, RandomArticles, time, logging, datetime
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

logging.basicConfig(filename='logger.log', filemode='w')
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

def get_chat_id(message):
    return message.chat.id

@bot.message_handler(commands=['start'])
def send_message(message):
    bot.reply_to(message, 'Welcome!')

@bot.message_handler(commands=['article'])
def send_article(message):
    bot.reply_to(message, RandomArticles.get_random_article())

@bot.message_handler(commands=['another'])
def send_another(message):
    bot.send_video(get_chat_id(message), open('Media/Thor_another.gif', 'rb'))
    time.sleep(1)
    bot.reply_to(message, RandomArticles.get_random_article())

bot.polling()

# TO-DO: Logger folder based on date