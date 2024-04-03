from aiogram import types
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def create_keyboard():
    kb = [
        InlineKeyboardButton(text="Кнопку с ссылкой", callback_data="inline_url"),
        InlineKeyboardButton(text="Кнопку с текстом", callback_data="inline_callback"),
        InlineKeyboardButton(text="Нет", callback_data="form_post")
    ]

    builder = InlineKeyboardBuilder()
    for key in kb[:2]:
        builder.add(key)
    builder.row(kb[2])
    return builder.as_markup()




if __name__ == "__main__":
    pass
