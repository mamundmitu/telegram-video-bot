from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters
import yt_dlp
import os

TOKEN = os.getenv("8540571491:AAF-nsxRsLi9rF_PcfAhVnZaPlVtLky1VnE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me any video link (YouTube, FB, Instagram, TikTok). I will download it!")

async def download_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text

    await update.message.reply_text("Downloading... please wait!")

    ydl_opts = {
        "format": "mp4",
        "outtmpl": "video.mp4"
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        await update.message.reply_video("video.mp4")
        os.remove("video.mp4")
    except Exception as e:
        await update.message.reply_text(f"Failed: {e}")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_video))

if __name__ == "__main__":
    app.run_polling()
