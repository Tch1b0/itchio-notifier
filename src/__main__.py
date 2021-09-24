import datetime
import pytz
import itchio
import random
import pathlib
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext


# Read out the tokens and ids
telegram_token = open(pathlib.Path.cwd().joinpath("token/telegram.txt")).read().replace("\n", "")
user_id = open(pathlib.Path.cwd().joinpath("token/telegram-id.txt")).read().replace("\n", "")
itchio_token = open(pathlib.Path.cwd().joinpath("token/itchio.txt")).read().replace("\n", "")

# Initialize Bot
bot = Bot(telegram_token)

# Set up the itchio wrapper
session = itchio.Session(itchio_token)
uc = itchio.UserCollection(session)
gc = itchio.GameCollection(session)

def informational_message(_) -> None:
    user = uc.me()

    introductions = [
        f"Hey {user.display_name}, here is your daily report\!",
        f"Hello, {user.display_name}\! I've got your current analytics\.",
        f"Guess what\? I got your new reports {user.display_name}\!",
        f"Beep boop\nHere are your analytics\!"
    ]

    msg = f"{random.choice(introductions)}\n\n"
    for game in gc.all():
        msg += f"*Title*: {game.title}\n"
        msg += f"*Downloads*: {game.downloads_count}\n"
        msg += f"*Views*: {game.views_count}\n"
        msg += f"*Purchases*: {game.purchase_count}\n"
        msg += f"*Earnings*: {game.earnings.amount_formatted if game.earnings != None else None}\n"
        msg += "\n\n"
    
    bot.send_message(
        text = msg,
        chat_id = user_id,
        parse_mode = "MarkdownV2"
    )

# Command for calling the function via a command
def call_informational_message(update: Update, context: CallbackContext):
    if update.effective_user.id == user_id:
        informational_message(context)

updater = Updater(telegram_token)

# Add /info command
updater.dispatcher.add_handler(CommandHandler('info', call_informational_message))

# Setting up that the function will run daily
updater.job_queue.run_daily(
    informational_message, 
    days=(0, 1, 2, 3, 4, 5, 6),
    time=datetime.time(hour=9, minute=00, second=00, tzinfo=pytz.timezone("Europe/Berlin"))
)

updater.start_polling()
updater.idle()