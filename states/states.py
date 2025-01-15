from aiogram.fsm.state import StatesGroup, State


class States (StatesGroup):
    section_work = State()
    section_replace = State()
    section_notes = State()
    admin = State()
    urmt_admin = State()
