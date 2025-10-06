import asyncio
import logging
import datetime
from aiogram import Bot, F, Router, types
from aiogram import Dispatcher
from aiogram.enums import ParseMode, ChatAction
from aiogram.client.bot import DefaultBotProperties
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from dotenv import load_dotenv
import os
from files.files import (schedule_rostov_acc_1_2025, schedule_rostov_acc_2_2025, schedule_rostov_acc_3_2025,
                         schedule_rostov_acc_4_2025, schedule_rostov_acc_5_2025,
                         schedule_rostov_acc_6_2025, replace_4, replace_5_1, replace_5_2, document_VK, document_138,
                         document_128, document_293, document_362, document_60, document_297, document_version_answers,
                         schedule_stavropol, sbornik_instructor, sbornik_trainee)
from keyboards.keyboards import keyboard_main, keyboard_work_back, keyboard_dinner_sim_back, \
    keyboard_replace_back, keyboard_schedule_rostov_acc, keyboard_schedule_stavropol, keyboard_docs, keyboard_docs_back, \
    keyboard_version, keyboard_notes_not_set_back, keyboard_notes_set_back, \
    keyboard_study, keyboard_rostov_acc, keyboard_admin_exit, keyboard_sbornik, keyboard_study_back
from commands import router as commands_router
from states.states import States
from database.models import async_session
from database.models import User
from sqlalchemy import select
from database.models import async_main
import database.requests as rq
from admin_handler import router as admin_router

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher()
dp.include_routers(commands_router,
                   admin_router)
router = Router()
scheduler = AsyncIOScheduler(timezone="Europe/Moscow")


@dp.callback_query(F.data == "button_test_pressed")
async def process_button_test_press(callback: CallbackQuery):
    time_of_action = datetime.datetime.now()
    last_seen_time = time_of_action.strftime("%Y-%m-%d %H:%M")
    print(last_seen_time)
    await rq.set_user(callback.from_user.id)
    await rq.set_time(callback.from_user.id, last_seen_time)
    shift = "test"
    await rq.set_shift(callback.from_user.id, shift)
    await callback.message.edit_text(
        text="<b>Главное меню</b>",
        reply_markup=keyboard_main
    )
    await callback.answer()


@dp.callback_query(F.data == "button_stavropol_pressed")
async def process_button_stavropol_press(callback: CallbackQuery):
    time_of_action = datetime.datetime.now()
    last_seen_time = time_of_action.strftime("%Y-%m-%d %H:%M")
    print(last_seen_time)
    await rq.set_user(callback.from_user.id)
    await rq.set_time(callback.from_user.id, last_seen_time)
    shift = "stavropol"
    await rq.set_shift(callback.from_user.id, shift)
    await callback.message.edit_text(
        text="<b>Главное меню</b>",
        reply_markup=keyboard_main
    )
    await callback.answer()

@dp.callback_query(F.data == "button_rostov_acc_pressed")
async def process_button_rostov_acc_press(callback: CallbackQuery):
    time_of_action = datetime.datetime.now()
    last_seen_time = time_of_action.strftime("%Y-%m-%d %H:%M")
    print(last_seen_time)
    await rq.set_user(callback.from_user.id)
    await rq.set_time(callback.from_user.id, last_seen_time)
    await callback.message.edit_text(
        text="Выберите смену:",
        reply_markup=keyboard_rostov_acc
    )
    await callback.answer()

@dp.callback_query(F.data == "button_rostov_acc_1_pressed")
async def process_button_rostov_acc_1_press(callback: CallbackQuery):
    time_of_action = datetime.datetime.now()
    last_seen_time = time_of_action.strftime("%Y-%m-%d %H:%M")
    print(last_seen_time)
    await rq.set_user(callback.from_user.id)
    await rq.set_time(callback.from_user.id, last_seen_time)
    shift = "rostov.acc.1"
    await rq.set_shift(callback.from_user.id, shift)
    await callback.message.edit_text(
            text="<b>Главное меню</b>",
            reply_markup=keyboard_main
        )
    await callback.answer()


@dp.callback_query(F.data == "button_rostov_acc_2_pressed")
async def process_button_rostov_acc_2_press(callback: CallbackQuery):
    time_of_action = datetime.datetime.now()
    last_seen_time = time_of_action.strftime("%Y-%m-%d %H:%M")
    print(last_seen_time)
    await rq.set_user(callback.from_user.id)
    await rq.set_time(callback.from_user.id, last_seen_time)
    shift = "rostov.acc.2"
    await rq.set_shift(callback.from_user.id, shift)
    await callback.message.edit_text(
            text="<b>Главное меню</b>",
            reply_markup=keyboard_main
        )
    await callback.answer()


@dp.callback_query(F.data == "button_rostov_acc_3_pressed")
async def process_button_rostov_acc_3_press(callback: CallbackQuery):
    time_of_action = datetime.datetime.now()
    last_seen_time = time_of_action.strftime("%Y-%m-%d %H:%M")
    print(last_seen_time)
    await rq.set_user(callback.from_user.id)
    await rq.set_time(callback.from_user.id, last_seen_time)
    shift = "rostov.acc.3"
    await rq.set_shift(callback.from_user.id, shift)
    await callback.message.edit_text(
            text="<b>Главное меню</b>",
            reply_markup=keyboard_main
        )
    await callback.answer()


@dp.callback_query(F.data == "button_rostov_acc_4_pressed")
async def process_button_rostov_acc_4_press(callback: CallbackQuery):
    time_of_action = datetime.datetime.now()
    last_seen_time = time_of_action.strftime("%Y-%m-%d %H:%M")
    print(last_seen_time)
    await rq.set_user(callback.from_user.id)
    await rq.set_time(callback.from_user.id, last_seen_time)
    shift = "rostov.acc.4"
    await rq.set_shift(callback.from_user.id, shift)
    await callback.message.edit_text(
            text="<b>Главное меню</b>",
            reply_markup=keyboard_main
        )
    await callback.answer()


@dp.callback_query(F.data == "button_rostov_acc_5_pressed")
async def process_button_rostov_acc_5_press(callback: CallbackQuery):
    time_of_action = datetime.datetime.now()
    last_seen_time = time_of_action.strftime("%Y-%m-%d %H:%M")
    print(last_seen_time)
    await rq.set_user(callback.from_user.id)
    await rq.set_time(callback.from_user.id, last_seen_time)
    shift = "rostov.acc.5"
    await rq.set_shift(callback.from_user.id, shift)
    await callback.message.edit_text(
            text="<b>Главное меню</b>",
            reply_markup=keyboard_main
        )
    await callback.answer()


@dp.callback_query(F.data == "button_rostov_acc_6_pressed")
async def process_button_rostov_acc_6_press(callback: CallbackQuery):
    time_of_action = datetime.datetime.now()
    last_seen_time = time_of_action.strftime("%Y-%m-%d %H:%M")
    print(last_seen_time)
    await rq.set_user(callback.from_user.id)
    await rq.set_time(callback.from_user.id, last_seen_time)
    shift = "rostov.acc.6"
    await rq.set_shift(callback.from_user.id, shift)
    await callback.message.edit_text(
            text="<b>Главное меню</b>",
            reply_markup=keyboard_main
        )
    await callback.answer()


@dp.callback_query(F.data == "button_schedule_pressed")
async def process_button_schedule_press(callback: CallbackQuery):
    time_of_action = datetime.datetime.now()
    last_seen_time = time_of_action.strftime("%Y-%m-%d %H:%M")
    print(last_seen_time)
    await rq.set_user(callback.from_user.id)
    await rq.set_time(callback.from_user.id, last_seen_time)
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == callback.from_user.id))
    if user.shift in ["rostov.acc.1", "rostov.acc.2", "rostov.acc.3", "rostov.acc.4", "rostov.acc.5", "rostov.acc.6"]:
        await callback.message.edit_text(
            text="<b>Графики работы</b>",
            reply_markup=keyboard_schedule_rostov_acc
        )
    if user.shift == "stavropol":
        await callback.message.edit_text(
            text="<b>Графики работы</b>",
            reply_markup=keyboard_schedule_stavropol
        )
    await callback.answer()


@dp.callback_query(F.data == "button_work_pressed")
async def process_button_work_press(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    time_of_action = datetime.datetime.now()
    last_seen_time = time_of_action.strftime("%Y-%m-%d %H:%M")
    print(last_seen_time)
    await rq.set_user(callback.from_user.id)
    await rq.set_time(callback.from_user.id, last_seen_time)
    await state.set_state(States.section_work)
    await callback.message.bot.send_chat_action(
        chat_id=callback.message.chat.id,
        action=ChatAction.UPLOAD_PHOTO
    )
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == callback.from_user.id))
    if user.shift == "rostov.acc.1":
        msg_schedule_rostov_acc_1_2025 = await callback.message.answer_photo(
            schedule_rostov_acc_1_2025,
            caption="График работы <b><u>Смены №1</u></b>",
            reply_markup=keyboard_work_back
        )
        msg_schedule_rostov_acc_1_2025_id = msg_schedule_rostov_acc_1_2025.message_id
        data = await state.update_data(section_work=(msg_schedule_rostov_acc_1_2025_id))
        await callback.answer()
        await asyncio.sleep(150000)
        await bot.delete_message(
            chat_id=callback.message.chat.id,
            message_id=msg_schedule_rostov_acc_1_2025_id
        )
    if user.shift == "rostov.acc.2":
        msg_schedule_rostov_acc_2_2025 = await callback.message.answer_photo(
            schedule_rostov_acc_2_2025,
            caption="График работы <b><u>Смены №2</u></b>",
            reply_markup=keyboard_work_back
        )
        msg_schedule_rostov_acc_2_2025_id = msg_schedule_rostov_acc_2_2025.message_id
        data = await state.update_data(section_work=(msg_schedule_rostov_acc_2_2025_id))
        await callback.answer()
        await asyncio.sleep(150000)
        await bot.delete_message(
            chat_id=callback.message.chat.id,
            message_id=msg_schedule_rostov_acc_2_2025_id
        )
    if user.shift == "rostov.acc.3":
        msg_schedule_rostov_acc_3_2025 = await callback.message.answer_photo(
            schedule_rostov_acc_3_2025,
            caption="График работы <b><u>Смены №3</u></b>",
            reply_markup=keyboard_work_back
        )
        msg_schedule_rostov_acc_3_2025_id = msg_schedule_rostov_acc_3_2025.message_id
        data = await state.update_data(section_work=(msg_schedule_rostov_acc_3_2025_id))
        await callback.answer()
        await asyncio.sleep(150000)
        await bot.delete_message(
            chat_id=callback.message.chat.id,
            message_id=msg_schedule_rostov_acc_3_2025_id
        )
    if user.shift == "rostov.acc.4":
        msg_schedule_rostov_acc_4_2025 = await callback.message.answer_photo(
            schedule_rostov_acc_4_2025,
            caption="График работы <b><u>Смены №4</u></b>",
            reply_markup=keyboard_work_back
        )
        msg_schedule_rostov_acc_4_2025_id = msg_schedule_rostov_acc_4_2025.message_id
        data = await state.update_data(section_work=(msg_schedule_rostov_acc_4_2025_id))
        await callback.answer()
        await asyncio.sleep(150000)
        await bot.delete_message(
            chat_id=callback.message.chat.id,
            message_id=msg_schedule_rostov_acc_4_2025_id
        )
    if user.shift == "rostov.acc.5":
        msg_schedule_rostov_acc_5_2025 = await callback.message.answer_photo(
            schedule_rostov_acc_5_2025,
            caption="График работы <b><u>Смены №5</u></b>",
            reply_markup=keyboard_work_back
        )
        msg_schedule_rostov_acc_5_2025_id = msg_schedule_rostov_acc_5_2025.message_id
        data = await state.update_data(section_work=(msg_schedule_rostov_acc_5_2025_id))
        await callback.answer()
        await asyncio.sleep(150000)
        await bot.delete_message(
            chat_id=callback.message.chat.id,
            message_id=msg_schedule_rostov_acc_5_2025_id
        )
    if user.shift == "rostov.acc.6":
        msg_schedule_rostov_acc_6_2025 = await callback.message.answer_photo(
            schedule_rostov_acc_6_2025,
            caption="График работы <b><u>Смены №6</u></b>",
            reply_markup=keyboard_work_back
        )
        msg_schedule_rostov_acc_6_2025_id = msg_schedule_rostov_acc_6_2025.message_id
        data = await state.update_data(section_work=(msg_schedule_rostov_acc_6_2025_id))
        await callback.answer()
        await asyncio.sleep(150000)
        await bot.delete_message(
            chat_id=callback.message.chat.id,
            message_id=msg_schedule_rostov_acc_6_2025_id
        )
    if user.shift == "stavropol":
        msg_schedule_stavropol = await callback.message.answer_photo(
            schedule_stavropol,
            caption="График работы персонала <b><u>АДЦ Ставрополь</u></b>",
            reply_markup=keyboard_work_back
        )
        msg_schedule_stavropol_id = msg_schedule_stavropol.message_id
        data = await state.update_data(section_work=(msg_schedule_stavropol_id))
        await callback.answer()
        await asyncio.sleep(150000)
        await bot.delete_message(
            chat_id=callback.message.chat.id,
            message_id=msg_schedule_stavropol_id
        )


@dp.callback_query(States.section_work, F.data == "button_work_back_pressed")
async def process_button_work_back_press(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == callback.from_user.id))
    if user.shift in ["rostov.acc.1", "rostov.acc.2", "rostov.acc.3", "rostov.acc.4", "rostov.acc.5", "rostov.acc.6"]:
        await bot.delete_message(
            chat_id=callback.message.chat.id,
            message_id=(data.get("section_work"))
        )
    if user.shift == "stavropol":
        await bot.delete_message(
            chat_id=callback.message.chat.id,
            message_id=(data.get("section_work"))
        )
    await state.clear()


@dp.callback_query(F.data == "button_replace_pressed")
async def process_button_replace_press(callback: CallbackQuery, state: FSMContext):
    time_of_action = datetime.datetime.now()
    last_seen_time = time_of_action.strftime("%Y-%m-%d %H:%M")
    print(last_seen_time)
    await rq.set_user(callback.from_user.id)
    await rq.set_time(callback.from_user.id, last_seen_time)
    await state.set_state(States.section_replace)
    await callback.message.bot.send_chat_action(
        chat_id=callback.message.chat.id,
        action=ChatAction.UPLOAD_PHOTO
    )
    msg_replace_4 = await callback.message.answer_photo(replace_4)
    msg_replace_4_id = msg_replace_4.message_id
    msg_replace_5_1 = await callback.message.answer_photo(replace_5_1)
    msg_replace_5_1_id = msg_replace_5_1.message_id
    msg_replace_5_2 = await callback.message.answer_photo(replace_5_2)
    msg_replace_5_2_id = msg_replace_5_2.message_id
    msg_replace_text = await callback.message.answer(
        text="<b>График подмены персонала ОВД</b>",
        reply_markup=keyboard_replace_back
    )
    msg_replace_text_id = msg_replace_text.message_id
    data = await state.update_data(section_replace=(msg_replace_4_id,
                                                    msg_replace_5_1_id,
                                                    msg_replace_5_2_id,
                                                    msg_replace_text_id))
    await callback.answer()
    await asyncio.sleep(150000)
    await bot.delete_message(
        chat_id=callback.message.chat.id,
        message_id=msg_replace_4_id
    )
    await bot.delete_message(
        chat_id=callback.message.chat.id,
        message_id=msg_replace_5_1_id
    )
    await bot.delete_message(
        chat_id=callback.message.chat.id,
        message_id=msg_replace_5_2_id
    )
    await bot.delete_message(
        chat_id=callback.message.chat.id,
        message_id=msg_replace_text_id
    )


@dp.callback_query(States.section_replace, F.data == "button_replace_back_pressed")
async def process_button_replace_back_press(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await bot.delete_messages(
        chat_id=callback.message.chat.id,
        message_ids=(data.get("section_replace"))
    )
    await state.clear()


@dp.callback_query(F.data == "button_dinner_pressed")
async def process_button_dinner_press(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    time_of_action = datetime.datetime.now()
    last_seen_time = time_of_action.strftime("%Y-%m-%d %H:%M")
    print(last_seen_time)
    await rq.set_user(callback.from_user.id)
    await rq.set_time(callback.from_user.id, last_seen_time)
    await callback.message.edit_text(
            text="Режим работы столовой:<b>\n\n10:30 — 13:30\n16:30 — 18:00</b>",
            reply_markup=keyboard_dinner_sim_back
        )
    await callback.answer()


@dp.callback_query(F.data == "button_sim_pressed")
async def process_button_sim_press(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    time_of_action = datetime.datetime.now()
    last_seen_time = time_of_action.strftime("%Y-%m-%d %H:%M")
    print(last_seen_time)
    await rq.set_user(callback.from_user.id)
    await rq.set_time(callback.from_user.id, last_seen_time)
    await callback.message.edit_text(
            text="График работы тренажерного центра:\n\n<b>Утро:</b> 1-й заход: 08:15 — 10:40\n           2-й заход: 10:50 — 13:15\n<b>День:</b> 1-й заход: 15:00 — 17:25\n            2-й заход: 17:30 — 19:55",
            reply_markup=keyboard_dinner_sim_back
        )
    await callback.answer()


@dp.callback_query(F.data == "button_transport_pressed")
async def process_button_transport_press(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    time_of_action = datetime.datetime.now()
    last_seen_time = time_of_action.strftime("%Y-%m-%d %H:%M")
    print(last_seen_time)
    await rq.set_user(callback.from_user.id)
    await rq.set_time(callback.from_user.id, last_seen_time)
    await callback.message.edit_text(
            text="График движения служебного транспорта:\n\n<b>Утро:</b> 07:25 от ТЦ Европейский (нижний рынок)\n<b>День:</b> 13:20 Гостиница Интурист\n<b>Ночь:</b> 20:45 Гостиница Интурист",
            reply_markup=keyboard_dinner_sim_back
        )
    await callback.answer()


@dp.callback_query(F.data == "button_dinner_sim_back_pressed")
async def process_button_dinner_sim_back_press(callback: CallbackQuery):
    time_of_action = datetime.datetime.now()
    last_seen_time = time_of_action.strftime("%Y-%m-%d %H:%M")
    print(last_seen_time)
    await rq.set_user(callback.from_user.id)
    await rq.set_time(callback.from_user.id, last_seen_time)
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == callback.from_user.id))
    if user.shift in ["rostov.acc.1", "rostov.acc.2", "rostov.acc.3", "rostov.acc.4", "rostov.acc.5", "rostov.acc.6"]:
        await callback.message.edit_text(
                text="<b>Графики работы</b>",
                reply_markup=keyboard_schedule_rostov_acc
            )
    if user.shift == "stavropol":
        await callback.message.edit_text(
            text="<b>Графики работы</b>",
            reply_markup=keyboard_schedule_stavropol
        )
    await callback.answer()


@dp.callback_query(F.data == "button_main_menu_pressed")
async def process_button_main_menu_press(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    time_of_action = datetime.datetime.now()
    last_seen_time = time_of_action.strftime("%Y-%m-%d %H:%M")
    print(last_seen_time)
    await rq.set_user(callback.from_user.id)
    await rq.set_time(callback.from_user.id, last_seen_time)
    await callback.message.edit_text(
        text="<b>Главное меню</b>",
        reply_markup=keyboard_main
    )
    await callback.answer()


@dp.callback_query(F.data == "button_docs_pressed")
async def process_button_docs_press(callback: CallbackQuery):
    time_of_action = datetime.datetime.now()
    last_seen_time = time_of_action.strftime("%Y-%m-%d %H:%M")
    print(last_seen_time)
    await rq.set_user(callback.from_user.id)
    await rq.set_time(callback.from_user.id, last_seen_time)
    await callback.message.edit_text(
            text="<b>Руководящие документы:</b>",
            reply_markup=keyboard_docs
        )
    await callback.answer()


@dp.callback_query(F.data == "button_VK_pressed")
async def process_button_VK_press(callback: CallbackQuery):
    time_of_action = datetime.datetime.now()
    last_seen_time = time_of_action.strftime("%Y-%m-%d %H:%M")
    print(last_seen_time)
    await rq.set_user(callback.from_user.id)
    await rq.set_time(callback.from_user.id, last_seen_time)
    await callback.message.bot.send_chat_action(
        chat_id=callback.message.chat.id,
        action=ChatAction.UPLOAD_DOCUMENT
    )
    msg_vk = await callback.message.answer_document(
            document=document_VK,
            caption="Воздушный кодекс РФ",
            reply_markup=keyboard_docs_back)
    msg_vk_id = msg_vk.message_id
    await callback.answer()
    await asyncio.sleep(150000)
    await bot.delete_message(
        chat_id=callback.message.chat.id,
        message_id=msg_vk_id
    )


@dp.callback_query(F.data == "button_docs_back_pressed")
async def process_button_docs_back_pressed(callback: CallbackQuery):
    await callback.message.delete()


@dp.callback_query(F.data == "button_138_pressed")
async def process_button_138_press(callback: CallbackQuery):
    time_of_action = datetime.datetime.now()
    last_seen_time = time_of_action.strftime("%Y-%m-%d %H:%M")
    print(last_seen_time)
    await rq.set_user(callback.from_user.id)
    await rq.set_time(callback.from_user.id, last_seen_time)
    await callback.message.bot.send_chat_action(
        chat_id=callback.message.chat.id,
        action=ChatAction.UPLOAD_DOCUMENT
    )
    msg_138 = await callback.message.answer_document(
            document=document_138,
            caption="Федеральные правила использования воздушного пространства РФ",
            reply_markup=keyboard_docs_back)
    msg_138_id = msg_138.message_id
    await callback.answer()
    await asyncio.sleep(150000)
    await bot.delete_message(
        chat_id=callback.message.chat.id,
        message_id=msg_138_id
    )


@dp.callback_query(F.data == "button_128_pressed")
async def process_button_128_press(callback: CallbackQuery):
    time_of_action = datetime.datetime.now()
    last_seen_time = time_of_action.strftime("%Y-%m-%d %H:%M")
    print(last_seen_time)
    await rq.set_user(callback.from_user.id)
    await rq.set_time(callback.from_user.id, last_seen_time)
    await callback.message.bot.send_chat_action(
        chat_id=callback.message.chat.id,
        action=ChatAction.UPLOAD_DOCUMENT
    )
    msg_128 = await callback.message.answer_document(
            document=document_128,
            caption="ФАП \"Подготовка и выполнение полетов в гражданской авиации РФ\"",
            reply_markup=keyboard_docs_back)
    msg_128_id = msg_128.message_id
    await callback.answer()
    await asyncio.sleep(150000)
    await bot.delete_message(
        chat_id=callback.message.chat.id,
        message_id=msg_128_id
    )


@dp.callback_query(F.data == "button_293_pressed")
async def process_button_293_press(callback: CallbackQuery):
    time_of_action = datetime.datetime.now()
    last_seen_time = time_of_action.strftime("%Y-%m-%d %H:%M")
    print(last_seen_time)
    await rq.set_user(callback.from_user.id)
    await rq.set_time(callback.from_user.id, last_seen_time)
    await callback.message.bot.send_chat_action(
        chat_id=callback.message.chat.id,
        action=ChatAction.UPLOAD_DOCUMENT
    )
    msg_293 = await callback.message.answer_document(
            document=document_293,
            caption="ФАП \"Подготовка и выполнение полетов в гражданской авиации РФ\"",
            reply_markup=keyboard_docs_back)
    msg_293_id = msg_293.message_id
    await callback.answer()
    await asyncio.sleep(150000)
    await bot.delete_message(
        chat_id=callback.message.chat.id,
        message_id=msg_293_id
    )


@dp.callback_query(F.data == "button_362_pressed")
async def process_button_362_press(callback: CallbackQuery):
    time_of_action = datetime.datetime.now()
    last_seen_time = time_of_action.strftime("%Y-%m-%d %H:%M")
    print(last_seen_time)
    await rq.set_user(callback.from_user.id)
    await rq.set_time(callback.from_user.id, last_seen_time)
    await callback.message.bot.send_chat_action(
        chat_id=callback.message.chat.id,
        action=ChatAction.UPLOAD_DOCUMENT
    )
    msg_362 = await callback.message.answer_document(
            document=document_362,
            caption="ФАП \"Порядок осуществления радиосвязи в воздушном пространстве РФ\"",
            reply_markup=keyboard_docs_back)
    msg_362_id = msg_362.message_id
    await callback.answer()
    await asyncio.sleep(150000)
    await bot.delete_message(
        chat_id=callback.message.chat.id,
        message_id=msg_362_id
    )


@dp.callback_query(F.data == "button_60_pressed")
async def process_button_60_press(callback: CallbackQuery):
    time_of_action = datetime.datetime.now()
    last_seen_time = time_of_action.strftime("%Y-%m-%d %H:%M")
    print(last_seen_time)
    await rq.set_user(callback.from_user.id)
    await rq.set_time(callback.from_user.id, last_seen_time)
    await callback.message.bot.send_chat_action(
        chat_id=callback.message.chat.id,
        action=ChatAction.UPLOAD_DOCUMENT
    )
    msg_60 = await callback.message.answer_document(
            document=document_60,
            caption="ФАП \"Предоставление метеорологической информации для обеспечения полетов воздушных судов\"",
            reply_markup=keyboard_docs_back)
    msg_60_id = msg_60.message_id
    await callback.answer()
    await asyncio.sleep(150000)
    await bot.delete_message(
        chat_id=callback.message.chat.id,
        message_id=msg_60_id
    )


@dp.callback_query(F.data == "button_297_pressed")
async def process_button_297_press(callback: CallbackQuery):
    time_of_action = datetime.datetime.now()
    last_seen_time = time_of_action.strftime("%Y-%m-%d %H:%M")
    print(last_seen_time)
    await rq.set_user(callback.from_user.id)
    await rq.set_time(callback.from_user.id, last_seen_time)
    await callback.message.bot.send_chat_action(
        chat_id=callback.message.chat.id,
        action=ChatAction.UPLOAD_DOCUMENT
    )
    msg_297 = await callback.message.answer_document(
            document=document_297,
            caption="ФАП \"Радиотехническое обеспечение полетов воздушных судов и авиационная электросвязь в гражданской авиации\"",
            reply_markup=keyboard_docs_back)
    msg_297_id = msg_297.message_id
    await callback.answer()
    await asyncio.sleep(150000)
    await bot.delete_message(
            chat_id=callback.message.chat.id,
            message_id=msg_297_id
        )


@dp.callback_query(F.data == "button_version_pressed")
async def process_button_version_press(callback: CallbackQuery):
    time_of_action = datetime.datetime.now()
    last_seen_time = time_of_action.strftime("%Y-%m-%d %H:%M")
    print(last_seen_time)
    await rq.set_user(callback.from_user.id)
    await rq.set_time(callback.from_user.id, last_seen_time)
    await callback.message.edit_text(
            text="<b>15-я версия</b>",
            reply_markup=keyboard_version
        )
    await callback.answer()


@dp.callback_query(F.data == "button_sbornik_pressed")
async def process_button_version_press(callback: CallbackQuery):
    time_of_action = datetime.datetime.now()
    last_seen_time = time_of_action.strftime("%Y-%m-%d %H:%M")
    print(last_seen_time)
    await rq.set_user(callback.from_user.id)
    await rq.set_time(callback.from_user.id, last_seen_time)
    await callback.message.edit_text(
        text="<b>Для кого нужен сборник?</b>",
        reply_markup=keyboard_sbornik
    )
    await callback.answer()


@dp.callback_query(F.data == "button_instructor_pressed")
async def process_button_instructor_press(callback: CallbackQuery):
    time_of_action = datetime.datetime.now()
    last_seen_time = time_of_action.strftime("%Y-%m-%d %H:%M")
    print(last_seen_time)
    await rq.set_user(callback.from_user.id)
    await rq.set_time(callback.from_user.id, last_seen_time)
    await callback.message.bot.send_chat_action(
        chat_id=callback.message.chat.id,
        action=ChatAction.UPLOAD_DOCUMENT
    )
    msg_sbornik_instructor = await callback.message.answer_document(
        document=sbornik_instructor,
        caption="Сборник задач потенциально конфликтных ситуаций при ОВД <b>для инструктора</b>",
        reply_markup=keyboard_study_back)
    msg_sbornik_instructor_id = msg_sbornik_instructor.message_id
    await callback.answer()
    await asyncio.sleep(150000)
    await bot.delete_message(
        chat_id=callback.message.chat.id,
        message_id=msg_sbornik_instructor_id
    )


@dp.callback_query(F.data == "button_trainee_pressed")
async def process_button_trainee_press(callback: CallbackQuery):
    time_of_action = datetime.datetime.now()
    last_seen_time = time_of_action.strftime("%Y-%m-%d %H:%M")
    print(last_seen_time)
    await rq.set_user(callback.from_user.id)
    await rq.set_time(callback.from_user.id, last_seen_time)
    await callback.message.bot.send_chat_action(
        chat_id=callback.message.chat.id,
        action=ChatAction.UPLOAD_DOCUMENT
    )
    msg_sbornik_trainee = await callback.message.answer_document(
        document=sbornik_trainee,
        caption="Сборник задач потенциально конфликтных ситуаций при ОВД <b>для стажера</b>",
        reply_markup=keyboard_study_back)
    msg_sbornik_trainee_id = msg_sbornik_trainee.message_id
    await callback.answer()
    await asyncio.sleep(150000)
    await bot.delete_message(
        chat_id=callback.message.chat.id,
        message_id=msg_sbornik_trainee_id
    )


@dp.callback_query(F.data == "button_version_answers_pressed")
async def process_button_version_answers_press(callback: CallbackQuery):
    time_of_action = datetime.datetime.now()
    last_seen_time = time_of_action.strftime("%Y-%m-%d %H:%M")
    print(last_seen_time)
    await rq.set_user(callback.from_user.id)
    await rq.set_time(callback.from_user.id, last_seen_time)
    await callback.message.bot.send_chat_action(
        chat_id=callback.message.chat.id,
        action=ChatAction.UPLOAD_DOCUMENT
    )
    msg_version = await callback.message.answer_document(
        document=document_version_answers,
        caption="Ответы на 15-ю версию",
        reply_markup=keyboard_study_back)
    msg_version_id = msg_version.message_id
    await callback.answer()
    await asyncio.sleep(150000)
    await bot.delete_message(
        chat_id=callback.message.chat.id,
        message_id=msg_version_id
    )


@dp.callback_query(F.data == "button_study_back_pressed")
async def process_button_study_back_pressed(callback: CallbackQuery):
    await callback.message.delete()


@dp.callback_query(F.data == "button_notes_pressed")
async def process_button_notes_press(callback: CallbackQuery, state: FSMContext):
    time_of_action = datetime.datetime.now()
    last_seen_time = time_of_action.strftime("%Y-%m-%d %H:%M")
    print(last_seen_time)
    await rq.set_user(callback.from_user.id)
    await rq.set_time(callback.from_user.id, last_seen_time)
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == callback.from_user.id))
        if user.notes is None:
            await state.set_state(States.section_notes)
            await callback.message.edit_text(
                text="Здесь вы можете оставить любую заметку:\n\n· даты отпуска или доработок;\n· логин/пароль от рабочего места;\n· любую другую информацию или напоминание.\n\nПросто пришлите сообщение с необходимым текстом, а я его запомню📝",
                reply_markup=keyboard_notes_not_set_back
            )
            await callback.answer()
        else:
            await callback.message.edit_text(
                text=f"Ваша заметка:\n\n<i>{user.notes}</i>",
                reply_markup=keyboard_notes_set_back
            )
            await callback.answer()


@dp.message(F.text, States.section_notes)
async def set_notes(message: types.Message, state: FSMContext):
    await state.get_state()
    note_text = message.text
    await rq.set_notes(message.from_user.id, note_text)
    await message.answer(text=f"Ваша заметка:\n\n<i>{note_text}</i>",
                         reply_markup=keyboard_notes_set_back
                         )


@dp.callback_query(F.data == "button_delete_a_note_pressed")
async def process_button_delete_a_note_press(callback: CallbackQuery, state: FSMContext):
    time_of_action = datetime.datetime.now()
    last_seen_time = time_of_action.strftime("%Y-%m-%d %H:%M")
    print(last_seen_time)
    await rq.set_user(callback.from_user.id)
    await rq.set_time(callback.from_user.id, last_seen_time)
    await rq.delete_notes(callback.from_user.id)
    await callback.message.edit_text(
        text="<b>Заметка удалена</b>\n\nЕсли желаете оставить новую, просто пришлите мне текст в ответном сообщении✍️",
        reply_markup=keyboard_notes_not_set_back
    )
    await state.set_state(States.section_notes)
    await callback.answer()


@dp.callback_query(F.data == "button_study_pressed")
async def process_button_study_press(callback: CallbackQuery):
    time_of_action = datetime.datetime.now()
    last_seen_time = time_of_action.strftime("%Y-%m-%d %H:%M")
    print(last_seen_time)
    await rq.set_user(callback.from_user.id)
    await rq.set_time(callback.from_user.id, last_seen_time)
    await callback.message.edit_text(
        text="<b>Обучающие материалы:</b>",
        reply_markup=keyboard_study
    )
    await callback.answer()


@dp.callback_query(F.data == "button_version_back_pressed")
async def process_button_version_back_press(callback: CallbackQuery):
    time_of_action = datetime.datetime.now()
    last_seen_time = time_of_action.strftime("%Y-%m-%d %H:%M")
    print(last_seen_time)
    await rq.set_user(callback.from_user.id)
    await rq.set_time(callback.from_user.id, last_seen_time)
    await callback.message.edit_text(
        text="<b>Обучающие материалы:</b>",
        reply_markup=keyboard_study
    )
    await callback.answer()


async def notification_sender_rostov_acc_1():
    user_ids = await rq.find_rostov_acc_1()
    for tg_id in user_ids:
        try:
            await bot.send_message(chat_id=tg_id,
                                   text="Добрый вечер!\n\nЯ тут, чтобы напомнить, что завтра техучёба...😒\nНе забудьте завести будильник⏰"
                                   )
        except Exception as e:
            print(f"Не удалось отправить сообщение пользователю с id {tg_id}: {e}")


scheduler.add_job(notification_sender_rostov_acc_1, 'date', run_date=datetime.datetime(2025, 1, 28, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_1, 'date', run_date=datetime.datetime(2025, 2, 27, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_1, 'date', run_date=datetime.datetime(2025, 3, 23, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_1, 'date', run_date=datetime.datetime(2025, 4, 22, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_1, 'date', run_date=datetime.datetime(2025, 5, 27, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_1, 'date', run_date=datetime.datetime(2025, 6, 26, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_1, 'date', run_date=datetime.datetime(2025, 7, 20, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_1, 'date', run_date=datetime.datetime(2025, 8, 26, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_1, 'date', run_date=datetime.datetime(2025, 9, 25, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_1, 'date', run_date=datetime.datetime(2025, 10, 19, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_1, 'date', run_date=datetime.datetime(2025, 11, 23, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_1, 'date', run_date=datetime.datetime(2025, 12, 23, 20, 0))


async def notification_sender_rostov_acc_2():
    user_ids = await rq.find_rostov_acc_2()
    for tg_id in user_ids:
        try:
            await bot.send_message(chat_id=tg_id,
                                   text="Добрый вечер!\n\nЯ тут, чтобы напомнить, что завтра техучёба...😒\nНе забудьте завести будильник⏰"
                                   )
        except Exception as e:
            print(f"Не удалось отправить сообщение пользователю с id {tg_id}: {e}")


scheduler.add_job(notification_sender_rostov_acc_2, 'date', run_date=datetime.datetime(2025, 1, 28, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_2, 'date', run_date=datetime.datetime(2025, 2, 27, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_2, 'date', run_date=datetime.datetime(2025, 3, 23, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_2, 'date', run_date=datetime.datetime(2025, 4, 22, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_2, 'date', run_date=datetime.datetime(2025, 5, 29, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_2, 'date', run_date=datetime.datetime(2025, 6, 22, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_2, 'date', run_date=datetime.datetime(2025, 7, 22, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_2, 'date', run_date=datetime.datetime(2025, 8, 26, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_2, 'date', run_date=datetime.datetime(2025, 9, 25, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_2, 'date', run_date=datetime.datetime(2025, 10, 19, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_2, 'date', run_date=datetime.datetime(2025, 11, 25, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_2, 'date', run_date=datetime.datetime(2025, 12, 25, 20, 0))


async def notification_sender_rostov_acc_3():
    user_ids = await rq.find_rostov_acc_3()
    for tg_id in user_ids:
        try:
            await bot.send_message(chat_id=tg_id,
                                   text="Добрый вечер!\n\nЯ тут, чтобы напомнить, что завтра техучёба...😒\nНе забудьте завести будильник⏰"
                                   )
        except Exception as e:
            print(f"Не удалось отправить сообщение пользователю с id {tg_id}: {e}")


scheduler.add_job(notification_sender_rostov_acc_3, 'date', run_date=datetime.datetime(2025, 1, 30, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_3, 'date', run_date=datetime.datetime(2025, 2, 23, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_3, 'date', run_date=datetime.datetime(2025, 3, 25, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_3, 'date', run_date=datetime.datetime(2025, 4, 24, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_3, 'date', run_date=datetime.datetime(2025, 5, 29, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_3, 'date', run_date=datetime.datetime(2025, 6, 22, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_3, 'date', run_date=datetime.datetime(2025, 7, 22, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_3, 'date', run_date=datetime.datetime(2025, 8, 28, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_3, 'date', run_date=datetime.datetime(2025, 9, 21, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_3, 'date', run_date=datetime.datetime(2025, 10, 21, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_3, 'date', run_date=datetime.datetime(2025, 11, 25, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_3, 'date', run_date=datetime.datetime(2025, 12, 25, 20, 0))


async def notification_sender_rostov_acc_4():
    user_ids = await rq.find_rostov_acc_4()
    for tg_id in user_ids:
        try:
            await bot.send_message(chat_id=tg_id,
                                   text="Добрый вечер!\n\nЯ тут, чтобы напомнить, что завтра техучёба...😒\nНе забудьте завести будильник⏰"
                                   )
        except Exception as e:
            print(f"Не удалось отправить сообщение пользователю с id {tg_id}: {e}")


scheduler.add_job(notification_sender_rostov_acc_4, 'date', run_date=datetime.datetime(2025, 1, 30, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_4, 'date', run_date=datetime.datetime(2025, 2, 23, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_4, 'date', run_date=datetime.datetime(2025, 3, 25, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_4, 'date', run_date=datetime.datetime(2025, 4, 24, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_4, 'date', run_date=datetime.datetime(2025, 5, 25, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_4, 'date', run_date=datetime.datetime(2025, 6, 24, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_4, 'date', run_date=datetime.datetime(2025, 7, 24, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_4, 'date', run_date=datetime.datetime(2025, 8, 28, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_4, 'date', run_date=datetime.datetime(2025, 9, 21, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_4, 'date', run_date=datetime.datetime(2025, 10, 21, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_4, 'date', run_date=datetime.datetime(2025, 11, 27, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_4, 'date', run_date=datetime.datetime(2025, 12, 21, 20, 0))


async def notification_sender_rostov_acc_5():
    user_ids = await rq.find_rostov_acc_5()
    for tg_id in user_ids:
        try:
            await bot.send_message(chat_id=tg_id,
                                   text="Добрый вечер!\n\nЯ тут, чтобы напомнить, что завтра техучёба...😒\nНе забудьте завести будильник⏰"
                                   )
        except Exception as e:
            print(f"Не удалось отправить сообщение пользователю с id {tg_id}: {e}")


scheduler.add_job(notification_sender_rostov_acc_5, 'date', run_date=datetime.datetime(2025, 1, 26, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_5, 'date', run_date=datetime.datetime(2025, 2, 25, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_5, 'date', run_date=datetime.datetime(2025, 3, 27, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_5, 'date', run_date=datetime.datetime(2025, 4, 20, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_5, 'date', run_date=datetime.datetime(2025, 5, 25, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_5, 'date', run_date=datetime.datetime(2025, 6, 24, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_5, 'date', run_date=datetime.datetime(2025, 7, 24, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_5, 'date', run_date=datetime.datetime(2025, 8, 24, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_5, 'date', run_date=datetime.datetime(2025, 9, 23, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_5, 'date', run_date=datetime.datetime(2025, 10, 23, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_5, 'date', run_date=datetime.datetime(2025, 11, 27, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_5, 'date', run_date=datetime.datetime(2025, 12, 21, 20, 0))


async def notification_sender_rostov_acc_6():
    user_ids = await rq.find_rostov_acc_6()
    for tg_id in user_ids:
        try:
            await bot.send_message(chat_id=tg_id,
                                   text="Добрый вечер!\n\nЯ тут, чтобы напомнить, что завтра техучёба...😒\nНе забудьте завести будильник⏰"
                                   )
        except Exception as e:
            print(f"Не удалось отправить сообщение пользователю с id {tg_id}: {e}")


scheduler.add_job(notification_sender_rostov_acc_6, 'date', run_date=datetime.datetime(2025, 1, 26, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_6, 'date', run_date=datetime.datetime(2025, 2, 25, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_6, 'date', run_date=datetime.datetime(2025, 3, 27, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_6, 'date', run_date=datetime.datetime(2025, 4, 20, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_6, 'date', run_date=datetime.datetime(2025, 5, 27, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_6, 'date', run_date=datetime.datetime(2025, 6, 26, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_6, 'date', run_date=datetime.datetime(2025, 7, 20, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_6, 'date', run_date=datetime.datetime(2025, 8, 24, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_6, 'date', run_date=datetime.datetime(2025, 9, 23, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_6, 'date', run_date=datetime.datetime(2025, 10, 23, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_6, 'date', run_date=datetime.datetime(2025, 11, 23, 20, 0))
scheduler.add_job(notification_sender_rostov_acc_6, 'date', run_date=datetime.datetime(2025, 12, 23, 20, 0))


async def notification_sender_stavropol():
    user_ids = await rq.find_stavropol()
    for tg_id in user_ids:
        try:
            await bot.send_message(chat_id=tg_id,
                                   text="Добрый вечер!\n\nЯ тут, чтобы напомнить, что завтра техучёба...😒\nНе забудьте завести будильник⏰"
                                   )
        except Exception as e:
            print(f"Не удалось отправить сообщение пользователю с id {tg_id}: {e}")


@dp.message(F.text == "urmtadmin")
async def secret_urmtadmin_message(message: types.Message, state: FSMContext):
    await state.set_state(States.urmt_admin)
    await message.reply("Батёк в здании!\n\nКидай график 📸")


@dp.message(F.photo, States.urmt_admin)
async def replace_schedule(message: types.Message):
    photo = message.photo[-1]
    stv_schedule_path = "/root/OrVD/files/schedule_stavropol.jpg"
    file_info = await bot.get_file(photo.file_id)
    await bot.download_file(file_info.file_path, stv_schedule_path)
    await message.answer(text="Загрузил новый график на сервер ✅",
                         reply_markup=keyboard_admin_exit)


async def main():
    await async_main()
    scheduler.start()
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
