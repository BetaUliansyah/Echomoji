#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot to reply to Telegram messages
# This program is dedicated to the public domain under the CC0 license.
"""
This Bot uses the Updater class to handle the bot.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram import Emoji
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import configparser
import unicodedata

from future.utils import bytes_to_native_str as n

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

logger = logging.getLogger(__name__)

class EmojiKoe(object):
    LETTER_A = n(b'\xF0\x9F\x87\xA6')
    LETTER_B = n(b'\xF0\x9F\x87\xA7')
    LETTER_C = n(b'\xF0\x9F\x87\xA8')
    LETTER_D = n(b'\xF0\x9F\x87\xA9')
    LETTER_E = n(b'\xF0\x9F\x87\xAA')
    LETTER_F = n(b'\xF0\x9F\x87\xAB')
    LETTER_G = n(b'\xF0\x9F\x87\xAC')
    LETTER_H = n(b'\xF0\x9F\x87\xAD')
    LETTER_I = n(b'\xF0\x9F\x87\xAE')
    LETTER_J = n(b'\xF0\x9F\x87\xAF')
    LETTER_K = n(b'\xF0\x9F\x87\xB0')
    LETTER_L = n(b'\xF0\x9F\x87\xB1')
    LETTER_M = n(b'\xF0\x9F\x87\xB2')
    LETTER_N = n(b'\xF0\x9F\x87\xB3')
    LETTER_O = n(b'\xF0\x9F\x87\xB4')
    LETTER_P = n(b'\xF0\x9F\x87\xB5')
    LETTER_Q = n(b'\xF0\x9F\x87\xB6')
    LETTER_R = n(b'\xF0\x9F\x87\xB7')
    LETTER_S = n(b'\xF0\x9F\x87\xB8')
    LETTER_T = n(b'\xF0\x9F\x87\xB9')
    LETTER_U = n(b'\xF0\x9F\x87\xBA')
    LETTER_V = n(b'\xF0\x9F\x87\xBB')
    LETTER_W = n(b'\xF0\x9F\x87\xBC')
    LETTER_X = n(b'\xF0\x9F\x87\xBD')
    LETTER_Y = n(b'\xF0\x9F\x87\xBE')
    LETTER_Z = n(b'\xF0\x9F\x87\xBF')

chars = {
    '1':Emoji.DIGIT_ONE_PLUS_COMBINING_ENCLOSING_KEYCAP,
    '2':Emoji.DIGIT_TWO_PLUS_COMBINING_ENCLOSING_KEYCAP,
    '3':Emoji.DIGIT_THREE_PLUS_COMBINING_ENCLOSING_KEYCAP,
    '4':Emoji.DIGIT_FOUR_PLUS_COMBINING_ENCLOSING_KEYCAP,
    '5':Emoji.DIGIT_FIVE_PLUS_COMBINING_ENCLOSING_KEYCAP,
    '6':Emoji.DIGIT_SIX_PLUS_COMBINING_ENCLOSING_KEYCAP,
    '7':Emoji.DIGIT_SEVEN_PLUS_COMBINING_ENCLOSING_KEYCAP,
    '8':Emoji.DIGIT_EIGHT_PLUS_COMBINING_ENCLOSING_KEYCAP,
    '9':Emoji.DIGIT_NINE_PLUS_COMBINING_ENCLOSING_KEYCAP,
    '0':Emoji.DIGIT_ZERO_PLUS_COMBINING_ENCLOSING_KEYCAP,
    'a':EmojiKoe.LETTER_A+" ",
    'b':EmojiKoe.LETTER_B+" ",
    'c':EmojiKoe.LETTER_C+" ",
    'd':EmojiKoe.LETTER_D+" ",
    'e':EmojiKoe.LETTER_E+" ",
    'f':EmojiKoe.LETTER_F+" ",
    'g':EmojiKoe.LETTER_G+" ",
    'h':EmojiKoe.LETTER_H+" ",
    'i':EmojiKoe.LETTER_I+" ",
    'j':EmojiKoe.LETTER_J+" ",
    'k':EmojiKoe.LETTER_K+" ",
    'l':EmojiKoe.LETTER_L+" ",
    'm':EmojiKoe.LETTER_M+" ",
    'n':EmojiKoe.LETTER_N+" ",
    'o':EmojiKoe.LETTER_O+" ",
    'p':EmojiKoe.LETTER_P+" ",
    'q':EmojiKoe.LETTER_Q+" ",
    'r':EmojiKoe.LETTER_R+" ",
    's':EmojiKoe.LETTER_S+" ",
    't':EmojiKoe.LETTER_T+" ",
    'u':EmojiKoe.LETTER_U+" ",
    'v':EmojiKoe.LETTER_V+" ",
    'w':EmojiKoe.LETTER_W+" ",
    'x':EmojiKoe.LETTER_X+" ",
    'y':EmojiKoe.LETTER_Y+" ",
    'z':EmojiKoe.LETTER_Z+" "
}

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hi! Just type anything you want, Echomoji Bot will convert your text to Emoji based alphabets and numbers.\n\nCreated by @BetaUli')


def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='Help!')


def echo(bot, update):
    #bot.sendMessage(update.message.chat_id, text=update.message.text)
    bot.sendMessage(update.message.chat_id, text=convert_to_emoji(update.message.text))


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

def convert_to_emoji(number):
    y = str(number)
    result = []
    for i in range(0, len(y)):
        x = unicodedata.normalize('NFD', y[i])[0].lower()
        print(x)
        try:
            result.append(chars[x])
        except:
            result.append(x)
    return ''.join(result)



def main():
    # Create the EventHandler and pass it your bot's token.
    mytoken = open('echomoji.token', 'r').read().strip()
    updater = Updater(mytoken)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler([Filters.text], echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
    
