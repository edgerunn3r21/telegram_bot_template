import traceback
import logging

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.filters import IsAdmin

logger = logging.getLogger(__name__)

stats_router = Router()
stats_router.message.filter(IsAdmin())


@stats_router.message(Command("stats"))
async def get_stats(message: Message):
    try:
        # Placeholder for stats functionality
        await message.answer("📊 Bot Statistics:\n• Total users: 0\n• Active today: 0\n• Messages processed: 0")
    except Exception as e:
        logger.error(f"Short error message: {e}")
        logger.error(traceback.format_exc())
        await message.answer("There was an error 😞...")


@stats_router.message(Command("users"))
async def get_users(message: Message):
    try:
        # Placeholder for users list functionality
        await message.answer("👥 User Management:\n• View all users\n• User details\n• User activity")
    except Exception as e:
        logger.error(f"Short error message: {e}")
        logger.error(traceback.format_exc())
        await message.answer("There was an error 😞...")
