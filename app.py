import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import subprocess

TOKEN = "9217579359:AAG8nhbQHV78-TrNa-oH19hhB9vk0LIh30w"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Сәлем! /check никнейм деп жаз.")

async def check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Никнеймді жаз: /check my_name")
        return
    username = context.args[0]
    await update.message.reply_text(f"🔍 {username} ізделуде...")
    try:
        result = subprocess.run(["sherlock", "--print-found", username], capture_output=True, text=True, timeout=60)
        if result.stdout:
            await update.message.reply_text(f"✅ Нәтиже:\n{result.stdout[:3000]}")
        else:
            await update.message.reply_text("❌ Ештеңе табылмады.")
    except Exception as e:
        await update.message.reply_text(f"Қате: {e}")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("check", check))
    app.run_polling()

if __name__ == "__main__":
    main()
