# bot.py
from telegram.ext import ApplicationBuilder, CommandHandler
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update, context):
    await update.message.reply_text("บอททำงานแล้วจ้า! 🚀")

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    await app.run_polling()

# ไม่ใช้ asyncio.run() เพราะ Render มี event loop อยู่แล้ว
import asyncio
asyncio.get_event_loop().create_task(main())
asyncio.get_event_loop().run_forever()
