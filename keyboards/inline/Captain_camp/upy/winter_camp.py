from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

all_camp = InlineKeyboardMarkup(row_width=2)
summer_camp = InlineKeyboardButton(text="Літній табір ", callback_data="choose:summercamp")# кнопка вибрати упю
winter_camp = InlineKeyboardButton(text= "Міжсезонний табір ", callback_data="choose:wintercamp")# кнопка вибрати упн

all_camp.insert(summer_camp)
all_camp.insert(winter_camp)