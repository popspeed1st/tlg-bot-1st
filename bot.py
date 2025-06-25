from telegram.ext import ApplicationBuilder, CommandHandler
import os
from dotenv import load_dotenv
import asyncio

load_dotenv(dotenv_path="env")

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update, context):
    await update.message.reply_text("บอททำงานแล้วจ้า! 🚀")

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
