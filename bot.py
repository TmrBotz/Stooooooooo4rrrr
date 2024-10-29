from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext

def upload(update: Update, context: CallbackContext) -> None:
    if update.message is None or update.message.document is None:
        logger.warning("Received an update without a message or document.")
        return  # Exit if there's no message or document

    file_id = update.message.document.file_id
    new_file = context.bot.get_file(file_id)

    channel_id = '-1002064680981'  # Replace with your channel username or ID
    message = context.bot.forward_message(chat_id=channel_id, from_chat_id=update.message.chat_id, message_id=update.message.message_id)

    unique_link = f"https://t.me/{channel_id}/{message.message_id}"
    blogspot_link = f"https://teraboxtoplayer.blogspot.com/2024/10/redirecting-to-your-link-code-credit.html?redirect={unique_link}"
    update.message.reply_text(f'Your file has been uploaded! You can download it [here]({blogspot_link}).', parse_mode='Markdown')

    else:
        update.message.reply_text('Please upload a valid file.')

def main() -> None:
    application = ApplicationBuilder().token("7156757667:AAGZRdBHCsQxR-fU4VlofUeFS-ozdSAk0CY").build()  # Updated initialization

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.Document.ALL, upload))  # Updated filter

    application.run_polling()

if __name__ == '__main__':
    main()
    
