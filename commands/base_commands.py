import datetime
from aiogram import types, Router
from aiogram.enums import ChatAction
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup

from files.files import (schedule_rostov_acc_1_2025, schedule_rostov_acc_2_2025, schedule_rostov_acc_3_2025,
                         schedule_rostov_acc_4_2025, schedule_rostov_acc_5_2025, schedule_rostov_acc_6_2025,
                         schedule_stavropol)
from keyboards.buttons import button_VK, button_138, button_128, button_293, button_362, button_60, button_297
from keyboards.keyboards import keyboard_main, keyboard_center

from database.models import async_session
from database.models import User
from sqlalchemy import select
import database.requests as rq

router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start(message: types.Message, state: FSMContext):
    await state.clear()
    await rq.set_user(message.from_user.id)
    await message.answer(text=f"Приветствую, <b>{(message.from_user.full_name)}</b>!👋\n\nВыберите центр:",
                         reply_markup=keyboard_center)


@router.message(Command("menu", prefix="/"))
async def handle_command_menu(message: types.Message, state: FSMContext):
    await state.clear()
    time_of_action = datetime.datetime.now()
    last_seen_time = time_of_action.strftime("%Y-%m-%d %H:%M")
    print(last_seen_time)
    await rq.set_user(message.from_user.id)
    await rq.set_time(message.from_user.id, last_seen_time)
    await message.answer(
        text="<b>Главное меню</b>",
        reply_markup=keyboard_main
    )


@router.message(Command("myshift", prefix="/"))
async def handle_command_myshift(message: types.Message, state: FSMContext):
    await state.clear()
    time_of_action = datetime.datetime.now()
    last_seen_time = time_of_action.strftime("%Y-%m-%d %H:%M")
    print(last_seen_time)
    await rq.set_user(message.from_user.id)
    await rq.set_time(message.from_user.id, last_seen_time)
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_PHOTO
    )
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == message.from_user.id))
    if user.shift == "rostov.acc.1":
        await message.answer_photo(
            schedule_rostov_acc_1_2025,
            caption="График работы <b><u>Смены №1</u></b>")
    if user.shift == "rostov.acc.2":
        await message.answer_photo(
            schedule_rostov_acc_2_2025,
            caption="График работы <b><u>Смены №2</u></b>")
    if user.shift == "rostov.acc.3":
        await message.answer_photo(
            schedule_rostov_acc_3_2025,
            caption="График работы <b><u>Смены №3</u></b>")
    if user.shift == "rostov.acc.4":
        await message.answer_photo(
            schedule_rostov_acc_4_2025,
            caption="График работы <b><u>Смены №4</u></b>")
    if user.shift == "rostov.acc.5":
        await message.answer_photo(
            schedule_rostov_acc_5_2025,
            caption="График работы <b><u>Смены №5</u></b>")
    if user.shift == "rostov.acc.6":
        await message.answer_photo(
            schedule_rostov_acc_6_2025,
            caption="График работы <b><u>Смены №6</u></b>")
    if user.shift == "stavropol":
        await message.answer_photo(
            schedule_stavropol,
            caption="График работы персонала <b><u>АДЦ Ставрополь</u></b>")


@router.message(Command("docs", prefix="/"))
async def handle_command_docs(message: types.Message, state: FSMContext):
    await state.clear()
    time_of_action = datetime.datetime.now()
    last_seen_time = time_of_action.strftime("%Y-%m-%d %H:%M")
    print(last_seen_time)
    await rq.set_user(message.from_user.id)
    await rq.set_time(message.from_user.id, last_seen_time)
    await message.answer(
        text="<b>Руководящие документы:</b>",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[[button_VK],
                                                           [button_138],
                                                           [button_128],
                                                           [button_293],
                                                           [button_362],
                                                           [button_60],
                                                           [button_297]])
    )


@router.message(Command("help", prefix="/"))
async def handle_command_help(message: types.Message, state: FSMContext):
    await state.clear()
    time_of_action = datetime.datetime.now()
    last_seen_time = time_of_action.strftime("%Y-%m-%d %H:%M")
    print(last_seen_time)
    await rq.set_user(message.from_user.id)
    await rq.set_time(message.from_user.id, last_seen_time)
    await message.answer(
        text="Всё сломалось? К сожалению, с роботами такое бывает...😢 \n\nВведите /start и начните сначала.\n\n✍️ По всем вопросам и предложениям обращаться к @eduard_glazyrin"
    )