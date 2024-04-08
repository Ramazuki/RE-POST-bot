from aiogram import Router, F, types
from aiogram.filters import Command, StateFilter
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot import bot

router = Router()


@router.message(Command("secret"), StateFilter(None))
async def print_secret(message: types.Message):
    builder = InlineKeyboardBuilder()
    key = InlineKeyboardButton(text="Оплатить", callback_data="payment")
    builder.add(key)
    await message.answer(text="<b>Donation!</b>", reply_markup=builder.as_markup())


@router.callback_query(F.data == "payment")
async def payment_options(callback: types.CallbackQuery):
    id = callback.from_user.id
    name = callback.from_user.full_name
    text = (f"Привет, {name}\n\n"
            f"Оплата вебинара ЛЮБОЙ суммой от сердца\n\nпо номеру телефона\n<b>+79243041773</b>\nСбербанк"
            "\n\nКарта\n<b>4276 7014 2105 2624</b>")
    builder = InlineKeyboardBuilder()
    key = InlineKeyboardButton(text="Перевод через сбер",
                               url="https://www.sberbank.com/sms/pbpn?requisiteNumber=79243041773")
    builder.add(key)
    try:
        await bot.send_message(chat_id=id, text=text, reply_markup=builder.as_markup())
    except:
        await callback.message.answer(text, reply_markup=builder.as_markup())
    await callback.answer("Спасибо за интерес!")
