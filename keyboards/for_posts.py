from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def create_keyboard() -> InlineKeyboardBuilder:
    kb = [
        InlineKeyboardButton(text="Кнопка 1", url="https://google.com")
    ]

    builder = InlineKeyboardBuilder()
    for key in kb:
        builder.add(key)
    return builder


if __name__ == "__main__":
    pass
