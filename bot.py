import telegram.ext
from run import ask, append_interaction_to_chat_log
import logging, os

PORT = int(os.environ.get('PORT', '8443'))

TOKEN = '5806730205:AAEbW7VDeMOuvtaP1p8siu34uSQ6be2lG8I'

session = {}

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text("Hello! Welcome to Vincent-GPT")


def help(update, context):
    update.message.reply_text("""
    The Following commands are available:
    /start -> Welcome to Vincent-GPT
    /help ->This Message
    /about -> About Vincent-GPT
    /contact -> Developer Info

    """)


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', context)


def about(update, context):
    update.message.reply_text("""
            Vincent-GPT is not just a chatbot. It's so much more than that. It's an AI-enabled customer service solution that answers your questions, responds to your tweets, and helps you find the products you're looking for. Vincent-GPT has the power to save you time, increase your sales, and make your customer service operation more efficient.
        """)


def contact(update, context):
    update.message.reply_text("Developer: Hacker Lord\n")


def handle_message(update, context):
    chat_log = session.get('chat_log')
    answer = ask(update.message.text, chat_log)
    session['chat_log'] = append_interaction_to_chat_log(update.message.text, answer,
                                                         chat_log)
    update.message.reply_text(f"{str(answer)}")


def main():
    updater = telegram.ext.Updater(TOKEN, use_context=True)
    bot = updater.dispatcher

    bot.add_handler(telegram.ext.CommandHandler("start", start))
    bot.add_handler(telegram.ext.CommandHandler("help", help))
    bot.add_handler(telegram.ext.CommandHandler("about", about))
    bot.add_handler(telegram.ext.CommandHandler("contact", contact))
    bot.add_handler(telegram.ext.MessageHandler(
        telegram.ext.Filters.text, handle_message))

    bot.add_error_handler(error)
    updater.start_polling()

    updater.start_webhook(
        listen="0.0.0.0",
        port=int(PORT),
        url_path=TOKEN,
        webhook_url='https://web3taskbot.herokuapp.com/' + TOKEN
    )

    updater.idle()


if __name__ == '__main__':
    main()