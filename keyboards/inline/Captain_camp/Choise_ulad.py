from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

lead_camp = InlineKeyboardMarkup(row_width=3)
upy = InlineKeyboardButton(text="УПЮ 🦅", callback_data="choose:upy")# кнопка вибрати упю
UPN = InlineKeyboardButton(text= "УПН 🐥", callback_data="choose:upn")# кнопка вибрати упн
UPP = InlineKeyboardButton(text="УПП 🐣", callback_data="choose:upp")# кнопка вибрати упп
comeback_to_time_camp = InlineKeyboardButton(text="Повернутись на попередню сторінку", callback_data="choose:timecamp")
lead_camp.insert(UPP)
lead_camp.insert(UPN)
lead_camp.insert(upy)
lead_camp.insert(comeback_to_time_camp)