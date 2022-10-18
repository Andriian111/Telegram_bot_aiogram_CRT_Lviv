from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Upn_camp = InlineKeyboardMarkup(row_width=2)
g_camp = InlineKeyboardButton(text="Гніздовий табір", callback_data="choose:gnizcamp")# кнопка вибрати гніздового табір
Upn_camp.insert(g_camp)
rov_camp = InlineKeyboardButton(text="Ройовий табір", callback_data="choose:rovcamp")# кнопка вибрати ройового табір
Upn_camp.insert(rov_camp)
comeback_to_choise_ulad = InlineKeyboardButton(text="Повернутись на попередню сторінку 🔙",
                                      callback_data="choose:comebacktoulad")# кнопка повернутись на обрання уладу

Upn_camp.insert(comeback_to_choise_ulad)
#вибрати гніздовий або табір


