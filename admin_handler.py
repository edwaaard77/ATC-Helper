from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from dotenv import load_dotenv
import os

from states.states import States
from keyboards.keyboards import keyboard_admin_exit, keyboard_main
from database.models import async_session
from database.models import User
from sqlalchemy import select

router = Router(name=__name__)

load_dotenv()
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")


@router.message(F.text == ADMIN_PASSWORD)
async def secret_admin_message(message: types.Message, state: FSMContext):
    await state.set_state(States.admin)
    await message.reply("Привет, отец! Желаете отправить послание?")


@router.message(States.admin)
async def announcement_sender(message: types.Message):
    # await message.send_copy(chat_id=290560857)
    async with async_session() as session:
        async with session.begin():
            # Получаем все tg_id из таблицы users
            result = await session.execute(select(User.tg_id))
            user_ids = result.scalars().all()

            # Отправляем сообщение каждому пользователю
            for tg_id in user_ids:
                try:
                    await message.send_copy(chat_id=tg_id)
                except Exception as e:
                    print(f"Не удалось отправить сообщение пользователю с id {tg_id}: {e}")
    await message.answer(text="Ваше послание уже у получателей!",
                         reply_markup=keyboard_admin_exit)


@router.callback_query(F.data == "button_admin_exit_pressed")
async def process_button_admin_exit_press(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.edit_text(
        text="<b>Главное меню</b>",
        reply_markup=keyboard_main
    )
    await callback.answer()
