from .admin_commands import admin_router as admin_cmd_router
from .stats_commands import stats_router
from .broadcast_commands import broadcast_router

# Combine all admin routers
from aiogram import Router

admin_router = Router()
admin_router.include_router(admin_cmd_router)
admin_router.include_router(stats_router)
admin_router.include_router(broadcast_router)

__all__ = ['admin_router']
