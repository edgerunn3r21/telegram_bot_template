import traceback
import logging

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.filters import IsAdmin

logger = logging.getLogger(__name__)

broadcast_router = Router()
broadcast_router.message.filter(IsAdmin())


@broadcast_router.message(Command("broadcast"))
async def broadcast_message(message: Message):
    try:
        # Placeholder for broadcast functionality
        await message.answer("📢 Broadcast Message:\n• Send message to all users\n• Schedule broadcasts\n• View broadcast history")
    except Exception as e:
        logger.error(f"Short error message: {e}")
        logger.error(traceback.format_exc())
        await message.answer("There was an error 😞...")


@broadcast_router.message(Command("announce"))
async def announce(message: Message):
    try:
        # Placeholder for announcement functionality
        await message.answer("📢 Announcement:\n• Create announcements\n• Manage announcements\n• View announcement history")
    except Exception as e:
        logger.error(f"Short error message: {e}")
        logger.error(traceback.format_exc())
        await message.answer("There was an error 😞...")
