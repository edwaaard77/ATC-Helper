from aiogram.types import InlineKeyboardMarkup

from keyboards.buttons import button_schedule, button_docs, button_version, button_work_back, \
    button_dinner_sim_back, button_replace_back, button_work, button_replace, button_dinner, button_sim, \
    button_main_menu, button_VK, button_138, button_128, button_293, button_362, button_60, button_297, \
    button_docs_back, button_version_apple, button_version_google, button_version_website, button_version_answers, \
    button_study_back, button_rostov_acc_1, button_rostov_acc_2, button_rostov_acc_3, button_rostov_acc_4, button_rostov_acc_5, \
    button_rostov_acc_6, button_notes, button_delete_a_note, button_study, button_etian, button_version_back, button_radar, \
    button_vpn, button_admin_exit, button_stavropol, button_rostov_acc, button_transport, button_sbornik, button_instructor, \
    button_trainee

keyboard_center = InlineKeyboardMarkup(
    inline_keyboard=[[button_rostov_acc], [button_stavropol]]
)
keyboard_rostov_acc_1st_row = [button_rostov_acc_1, button_rostov_acc_2, button_rostov_acc_3]
keyboard_rostov_acc_2nd_row = [button_rostov_acc_4, button_rostov_acc_5, button_rostov_acc_6]
keyboard_rostov_acc = InlineKeyboardMarkup(
    inline_keyboard=[keyboard_rostov_acc_1st_row,
                     keyboard_rostov_acc_2nd_row]
)
keyboard_main_1st_row = [button_schedule, button_notes]
keyboard_main_2nd_row = [button_radar]
keyboard_main_3rd_row = [button_docs, button_study]
keyboard_main_4th_row = [button_vpn]
keyboard_main = InlineKeyboardMarkup(
    inline_keyboard=[keyboard_main_1st_row,
                     keyboard_main_2nd_row,
                     keyboard_main_3rd_row,
                     keyboard_main_4th_row]
)
keyboard_work_back = InlineKeyboardMarkup(
    inline_keyboard=[[button_work_back]]
)
keyboard_dinner_sim_back = InlineKeyboardMarkup(
    inline_keyboard=[[button_dinner_sim_back]]
)
keyboard_replace_back = InlineKeyboardMarkup(
    inline_keyboard=[[button_replace_back]]
)
keyboard_schedule_rostov_acc_1st_row = [button_work, button_replace]
keyboard_schedule_rostov_acc_2nd_row = [button_dinner, button_sim]
keyboard_schedule_rostov_acc_rows = [keyboard_schedule_rostov_acc_1st_row,
                                     keyboard_schedule_rostov_acc_2nd_row,
                                     [button_main_menu]]
keyboard_schedule_rostov_acc = InlineKeyboardMarkup(
    inline_keyboard=keyboard_schedule_rostov_acc_rows
)
keyboard_schedule_stavropol = InlineKeyboardMarkup(
    inline_keyboard=[[button_work], [button_transport], [button_main_menu]]
)
keyboard_docs = InlineKeyboardMarkup(
    inline_keyboard=[[button_VK],
                     [button_138],
                     [button_128],
                     [button_293],
                     [button_362],
                     [button_60],
                     [button_297],
                     [button_main_menu]]
)
keyboard_docs_back = InlineKeyboardMarkup(
    inline_keyboard=[[button_docs_back]]
)
keyboard_version_1st_row = [button_version_apple, button_version_google]
keyboard_version_rows = [keyboard_version_1st_row,
                         [button_version_website],
                         [button_version_answers],
                         [button_version_back]]
keyboard_version = InlineKeyboardMarkup(
    inline_keyboard=keyboard_version_rows
)
keyboard_study_back = InlineKeyboardMarkup(
    inline_keyboard=[[button_study_back]]
)
keyboard_notes_not_set_back = InlineKeyboardMarkup(
    inline_keyboard=[[button_main_menu]]
)
keyboard_notes_set_back = InlineKeyboardMarkup(
    inline_keyboard=[[button_delete_a_note],
                     [button_main_menu]]
)
keyboard_study = InlineKeyboardMarkup(
    inline_keyboard=[[button_version],
                     [button_etian],
                     [button_sbornik],
                     [button_main_menu]]
)
keyboard_sbornik = InlineKeyboardMarkup(
    inline_keyboard=[[button_instructor],
                     [button_trainee],
                     [button_version_back]]
)
keyboard_admin_exit = InlineKeyboardMarkup(
    inline_keyboard=[[button_admin_exit]]
)
