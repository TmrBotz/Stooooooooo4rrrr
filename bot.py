from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome! Please upload a file using /upload.')

def upload(update: Update, context: CallbackContext) -> None:
    if update.message.document:
        file_id = update.message.document.file_id
        new_file = context.bot.get_file(file_id)
        
        # Generate a unique link (you can replace this with your actual file storage logic)
        unique_link = f"https://t.me/TMR_File_Storee_bot?start{file_id}"

        # Generate Blogspot link
        blogspot_link = f"https://teraboxtoplayer.blogspot.com/2024/10/redirecting-to-your-link-code-credit.html?redirect={unique_link}"
        update.message.reply_text(f'Your file has been uploaded! You can download it [here]({blogspot_link}).', parse_mode='Markdown')
    else:
        update.message.reply_text('Please upload a valid file.')

def main() -> None:
    updater = Updater("7156757667:AAGZRdBHCsQxR-fU4VlofUeFS-ozdSAk0CY")  # Replace with your bot token

    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("upload", upload))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
      
