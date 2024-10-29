from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome! Please upload a file using /upload.')

def upload(update: Update, context: CallbackContext) -> None:
    if update.message.document:
        file_id = update.message.document.file_id
        new_file = context.bot.get_file(file_id)
        
        # Forward the file to the desired channel
        channel_id = '-1002064680981'  # Replace with your channel username or ID
        message = context.bot.forward_message(chat_id=channel_id, from_chat_id=update.message.chat_id, message_id=update.message.message_id)

        # Generate a unique link for the forwarded message
        unique_link = f"https://t.me/{channel_id}/{message.message_id}"

        # Generate Blogspot link
        blogspot_link = f"https://teraboxtoplayer.blogspot.com/2024/10/redirecting-to-your-link-code-credit.html?redirect={unique_link}"
        update.message.reply_text(f'Your file has been uploaded! You can download it [here]({blogspot_link}).', parse_mode='Markdown')
    else:
        update.message.reply_text('Please upload a valid file.')

def main() -> None:
    updater = Updater("7156757667:AAGZRdBHCsQxR-fU4VlofUeFS-ozdSAk0CY")  # Replace with your bot token

    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(MessageHandler(Filters.document, upload))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
