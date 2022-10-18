from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button_camp_leader = KeyboardButton(text='Я комендант табору 🏕') # Я комендант табору
participant = KeyboardButton(text='Я учасник табору ⛺️') #Я учасник табору
team_help = KeyboardButton(text='Таборовий помічник 🔰')
training = KeyboardButton(text='Все про мандрівки ⛰')
crs_DMD = KeyboardButton(text='Курси домедичної допомоги ⛑')
all_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_camp_leader,participant).\
    add(team_help,training).add(crs_DMD)
#Основна клавіатура
