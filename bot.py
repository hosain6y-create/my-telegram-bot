import os
from threading import Thread
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# রেন্ডার সার্ভার সচল রাখার জন্য ফ্লাস্ক অ্যাপ
app = Flask("")


@app.route("/")
def home():
  return "Bot is running 24/7!"


def run_web():
  port = int(os.environ.get("PORT", 8080))
  app.run(host="0.0.0.0", port=port)


def keep_alive():
  t = Thread(target=run_web)
  t.start()


# আপনার বটের মূল স্টার্ট কমান্ড
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text(
      "স্বাগতম! আপনার বট এখন সফলভাবে ২৪ ঘণ্টা সচল রয়েছে।"
  )


if __name__ == "__main__":
  # ওয়েব সার্ভার চালু করা হচ্ছে
  keep_alive()

  # আপনার আসল টেলিগ্রাম বট টোকেন এখানে বসানো হলো
  TOKEN = "8747652767:AAHbqcJEqcp2TCyLbyzBteCTt6wokVsTYvY"

  application = ApplicationBuilder().token(TOKEN).build()
  application.add_handler(CommandHandler("start", start))

  application.run_polling()
