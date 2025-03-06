from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv
import os
import requests
import subprocess

# Load environment variables
load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Command: /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Welcome to 🐮oooo-diator🫱🏻‍🫲🏼💌! Send me a voice message to analyze your emotion.")

# Command: /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("This bot detects emotions from your voice. Send a voice message to get started.")

# Handler: Voice Message
async def process_voice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        # Step 1: Download the voice file
        voice_file = await update.message.voice.get_file()
        ogg_path = f"temp/{voice_file.file_id}.ogg"
        wav_path = f"temp/{voice_file.file_id}.wav"
        await voice_file.download_to_drive(ogg_path)

        # Step 2: Convert OGG to WAV
        subprocess.run(["ffmpeg", "-i", ogg_path, wav_path], check=True)

        # Step 3: Placeholder for backend processing (e.g., send WAV file to backend)
        # Simulate emotion detection
        emotion = "happy"  # Replace with actual backend integration
        await update.message.reply_text(f"I detected that you're feeling {emotion}.")
    
    except Exception as e:
        # Handle exceptions and notify the user
        print(f"Error occurred: {e}")
        await update.message.reply_text("An error occurred while processing your voice message.")
    
    # finally:
    #     # Step 4: Cleanup temporary files (whether successful or not)
    #     if os.path.exists(ogg_path):
    #         os.remove(ogg_path)
    #     if os.path.exists(wav_path):
    #         os.remove(wav_path)

# Main function
def main():
    # Create the application
    application = Application.builder().token(BOT_TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Add message handler for voice messages
    application.add_handler(MessageHandler(filters.VOICE, process_voice))

    # Run the bot
    application.run_polling()

if __name__ == "__main__":
    main()