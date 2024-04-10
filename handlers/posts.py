from aiogram import Router, F, types
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from keyboards.for_posts import create_keyboard

router = Router()


class CreatePost(StatesGroup):
    writing_post_text = State()
    adding_post_url_button = State()
    adding_post_button = State()
    setting_button_name = State()


@router.message(Command("start"), StateFilter(None))
async def start_handler(message: types.Message):
    await message.reply(text="Приветик, спасибо за подписку!")


@router.message(StateFilter(None), Command("newpost"))
async def create_new_post(message: types.Message, state: FSMContext):
    await message.reply(text="Введи текст поста")
    await state.set_state(CreatePost.writing_post_text)


@router.message(CreatePost.writing_post_text, F.text)
async def set_post_text(message: types.Message, state: FSMContext):
    await state.update_data(post_text=message.html_text)
    keyboard = await create_keyboard()
    await message.answer(text="Хотите добавить кнопку на пост?", reply_markup=keyboard)


@router.message(CreatePost.adding_post_url_button, F.text)
async def set_url_for_button(message: types.Message, state: FSMContext):
    await state.set_state(CreatePost.setting_button_name)
    await state.update_data(button_url=message.text.lower(), is_url=True)
    await message.answer(text="Введите текст на кнопке")


@router.message(CreatePost.setting_button_name, F.text)
async def set_button_name(message: types.Message, state: FSMContext):
    data = await state.get_data()
    builder = InlineKeyboardBuilder()
    button: InlineKeyboardButton
    if data["is_url"]:
        button = InlineKeyboardButton(text=message.text, url=data["button_url"])
        builder.add(button)
    await message.answer("Ваше сообщение")
    try:
        await message.answer(text=data["post_text"], reply_markup=builder.as_markup())
    except TelegramBadRequest:
        await message.answer(text=data["post_text"])
        await message.answer("Ошибка в ссылке")
    await state.clear()


@router.callback_query(CreatePost.writing_post_text, F.data == "inline_url")
async def answer_callback(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(CreatePost.adding_post_url_button)
    await callback.message.answer(text="Введите ссылку")
    await callback.answer()
