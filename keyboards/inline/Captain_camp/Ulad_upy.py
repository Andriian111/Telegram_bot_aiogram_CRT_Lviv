from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
UPY_camp = InlineKeyboardMarkup(row_width=2)
k_camp = InlineKeyboardButton(text="Курінний табір 🏕️", callback_data="choose:kyrinuicamp")# кнопка вибрати курінний табір
UPY_camp.insert(k_camp)
g_camp = InlineKeyboardButton(text="Гуртковий табір 💤", callback_data="choose:gcamp")# кнопка вибрати гуртковий табір
UPY_camp.insert(g_camp)
comeback_to_choise_ulad = InlineKeyboardButton(text="Повернутись на попередню сторінку 🔙",
                                      callback_data="choose:comebacktoulad")# кнопка повернутись на обрання уладу

UPY_camp.insert(comeback_to_choise_ulad)
#вибрати гуртковий, або курінний табір






#Гуртковий табір







