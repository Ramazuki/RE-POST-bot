from aiogram import Router, F, types
from aiogram.filters import Command

from keyboards.for_posts import create_keyboard

router = Router()


@router.message(Command("start"))
async def start_handler(message: types.Message):
    builder = await create_keyboard()
    await message.reply(text="Кнопки", reply_markup=builder.as_markup())

