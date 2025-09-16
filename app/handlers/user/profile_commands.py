import traceback
import logging

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import orm_read, User

logger = logging.getLogger(__name__)

profile_router = Router()


@profile_router.message(Command("profile"))
async def profile_command(message: Message, session: AsyncSession):
    try:
        tg_id = str(message.from_user.id)
        user = await orm_read(session, User, as_iterable=False, tg_id=tg_id)
        
        if user:
            profile_text = f"""
👤 <b>Your Profile</b>

<b>User ID:</b> {user.tg_id}
<b>Username:</b> @{user.username or 'Not set'}
<b>Registration:</b> {user.created_at.strftime('%Y-%m-%d %H:%M') if hasattr(user, 'created_at') else 'Unknown'}
            """
        else:
            profile_text = "❌ Profile not found. Please use /start to register."
            
        await message.answer(profile_text)
    except Exception as e:
        logger.error(f"Short error message: {e}")
        logger.error(traceback.format_exc())
        await message.answer("There was an error 😞...")


@profile_router.message(Command("settings"))
async def settings_command(message: Message):
    try:
        settings_text = """
⚙️ <b>Settings</b>

<b>Available Settings:</b>
• Language preferences
• Notification settings
• Privacy settings
• Theme preferences

<i>Settings functionality coming soon!</i>
        """
        await message.answer(settings_text)
    except Exception as e:
        logger.error(f"Short error message: {e}")
        logger.error(traceback.format_exc())
        await message.answer("There was an error 😞...")
