from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()


@router.message(Command("secret"))
async def print_secret(message: types.Message):
    builder = InlineKeyboardBuilder()
    key = InlineKeyboardButton(text="Оплатить", callback_data="payment")
    builder.add(key)
    await message.answer(text="Какой-то текст тут", reply_markup=builder.as_markup())


@router.callback_query(F.data == "payment")
async def payment_options(callback: types.CallbackQuery):
    name = callback.from_user.full_name
    text = (f"Привет, {name}\n\n"
            f"Оплата вебинара ЛЮБОЙ суммой от сердца\n\nпо номеру телефона\n<b>+79243041773</b>\nСбербанк"
            "\n\nКарта\n<b>4276 7014 2105 2624</b>")
    builder = InlineKeyboardBuilder()
    key = InlineKeyboardButton(text="Перевод через сбер",
                               url="https://www.sberbank.com/sms/pbpn?requisiteNumber=79243041773")
    builder.add(key)
    await callback.message.answer(text, reply_markup=builder.as_markup())
    await callback.answer("Спасибо за интерес!")
