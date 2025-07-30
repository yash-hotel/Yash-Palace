# bot/middleware/init.py

from aiogram import BaseMiddleware, Dispatcher
from aiogram.types import Message
from typing import Callable, Dict, Any, Awaitable


class LanguageMiddleware(BaseMiddleware):
    async def call(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        user_lang = "hi" if "hi" in event.from_user.language_code else "en"
        data["lang"] = user_lang
        return await handler(event, data)


def register_middlewares(dp: Dispatcher):
    dp.message.middleware(LanguageMiddleware())
