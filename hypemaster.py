import logging
import random
import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Set up logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Define the ChatGPT API URL
API_URL = "https://api.openai.com/v1/engines/davinci/completions"

# Define the ChatGPT API parameters
API_PARAMS = {
    "prompt": "Tell me a story",
    "temperature": 0.7,
    "max_tokens": 1024,
    "n": 1,
    "stop": "\n\n",
}


# Define a command handler
def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Hello, Welcome to the group"
    )


# Define a message handler
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


# Define a user activity handler
def activity(update, context):
    # Check user activity here (e.g. time since last message)
    if user_is_active:
        # Make a request to the ChatGPT API and retrieve a random story
        response = requests.post(
            API_URL,
            headers={"Authorization": "6173745258:AAHA7uA2VdBbduMZ0phaAxZoEdFc2OZCTEw"},
            json=API_PARAMS,
        )
        story = response.json()["choices"][0]["text"]
        context.bot.send_message(chat_id=update.effective_chat.id, text=story)
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="User is inactive."
        )


# Set up the bot and add handlers
def main():
    # Create an Updater object and pass in your bot token
    # updater = Updater(
    #     token="6173745258:AAHA7uA2VdBbduMZ0phaAxZoEdFc2OZCTE", use_context=True
    # )

    updater = Updater("6173745258:AAHA7uA2VdBbduMZ0phaAxZoEdFc2OZCTEw")
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add command handler
    dispatcher.add_handler(CommandHandler("start", start))

    # Add message handler
    dispatcher.add_handler(MessageHandler(Filters.text, echo))

    # Add user activity handler
    dispatcher.add_handler(MessageHandler(Filters.all, activity))

    # Start the bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()


if __name__ == "__main__":
    main()
