from aiogram.types import BotCommand, BotCommandScopeChat
from aiogram import Bot

admin_private = [
    BotCommand(command="admin", description="Адмін панель"),
]


async def set_admin_commands(admin_list: list, bot: Bot):
    if not admin_list:
        return

    for admin in admin_list:
        scope = BotCommandScopeChat(chat_id=admin)
        await bot.set_my_commands(admin_private, scope=scope)


user_private = [
    BotCommand(command="start", description="Запуск бота"),
    BotCommand(command="menu", description="Меню"),
    BotCommand(command="help", description="Информация о боте"),
]
