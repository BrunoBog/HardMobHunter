import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler

def settings(bot, update):
    """
        Configure the messages language using a custom keyboard.
    """
    # Languages message
    msg = "Please, choose a language:\n"
    msg += "en_US - English (US)\n"
    msg += "pt_BR - Português (Brasil)\n"

    # Languages menu
    languages_keyboard = [
        [telegram.KeyboardButton('en_US - English (US)')],
        [telegram.KeyboardButton('pt_BR - Português (Brasil)')]
    ]
    reply_kb_markup = telegram.ReplyKeyboardMarkup(languages_keyboard,
                                                   resize_keyboard=True,
                                                   one_time_keyboard=True)

    # Sends message with languages menu
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg,
                     reply_markup=reply_kb_markup)


def kb_settings_select(bot, update, groups):
    """
        Updates the user's language based on it's choice.
    """
    chat_id = update.message.chat_id
    language = groups[0]

    # Available languages
    languages = {"pt_BR": "Português (Brasil)",
                 "en_US": "English (US)"}

    # If the language choice matches the expression AND is a valid choice
    if language in languages.keys():
        # Sets the user's language
        db.set(str(chat_id), language)
        bot.send_message(chat_id=chat_id,
                         text="Language updated to {0}"
                         .format(languages[language]))
    else:
        # If it is not a valid choice, sends an warning
        bot.send_message(chat_id=chat_id,
                         text="Unknown language! :(")

settings_handler = CommandHandler('settings', settings)
get_language_handler = RegexHandler('^([a-z]{2}_[A-Z]{2}) - .*',
                                    kb_settings_select,
                                    pass_groups=True)

