import traceback
import logging

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

logger = logging.getLogger(__name__)

help_router = Router()


@help_router.message(Command("help"))
async def help_command(message: Message):
    try:
        help_text = """
🤖 <b>Bot Help</b>

<b>Available Commands:</b>
/start - Start using the bot
/help - Show this help message
/profile - View your profile
/settings - Bot settings

<b>Need more help?</b>
Contact support or use /start to begin.
        """
        await message.answer(help_text)
    except Exception as e:
        logger.error(f"Short error message: {e}")
        logger.error(traceback.format_exc())
        await message.answer("There was an error 😞...")


@help_router.message(Command("info"))
async def info_command(message: Message):
    try:
        info_text = """
ℹ️ <b>Bot Information</b>

This is a sample Telegram bot built with aiogram.
It demonstrates command organization and user management.

<b>Features:</b>
• User registration
• Command handling
• Admin functionality
• Database integration
        """
        await message.answer(info_text)
    except Exception as e:
        logger.error(f"Short error message: {e}")
        logger.error(traceback.format_exc())
        await message.answer("There was an error 😞...")
