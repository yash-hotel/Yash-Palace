import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from bot.config import load_config
from bot.handlers import start, booking, payment, admin
from bot.database import create_db
from bot.middleware import register_middlewares

logger = logging.getLogger(__name__)

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )

    config = load_config()

    bot = Bot(token=config.bot_token, parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    # Include all routers
    dp.include_routers(
        start.router,
        booking.router,
        payment.router,
        admin.router,
    )

    # Initialize the database
    await create_db()

    # Register middlewares (like logging, throttling, etc.)
    register_middlewares(dp)

    logger.info("🤖 Bot is starting...")

    # Start polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("🚫 Bot stopped.")
