import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Welcome! Please upload a file using /upload.')

async def upload(update: Update, context: CallbackContext) -> None:
    if update.message is None or update.message.document is None:
        logger.warning("Received an update without a message or document.")
        return  # Exit if there's no message or document

    file_id = update.message.document.file_id
    new_file = await context.bot.get_file(file_id)  # Add await here

    channel_id = '-1002064680981'  # Replace with your channel username or ID
    message = await context.bot.forward_message(chat_id=channel_id, from_chat_id=update.message.chat_id, message_id=update.message.message_id)  # Add await here

    unique_link = f"https://t.me/{channel_id}/{message.message_id}"
    blogspot_link = f"https://teraboxtoplayer.blogspot.com/2024/10/redirecting-to-your-link-code-credit.html?redirect={unique_link}"
    await update.message.reply_text(f'Your file has been uploaded! You can download it [here]({blogspot_link}).', parse_mode='Markdown')  # Add await here

def main() -> None:
    application = ApplicationBuilder().token("7156757667:AAELbKDvIsZZO4Z2Byd0fECdPAbgE-uG-FU").build()  # Update with your bot token

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.Document.ALL, upload))  # Updated filter

    application.run_polling()

if __name__ == '__main__':
    main()
    
