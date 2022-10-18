from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

help_of_camp = InlineKeyboardMarkup(row_width=1)
inventory_camp = InlineKeyboardButton(text="Рекомендований список реманенту 🪓 ",
                                      callback_data="choose:inventorycamp")# кнопка вибрати реманент на табір
help_of_camp.insert(inventory_camp)
program_of_camp = InlineKeyboardButton(text="Ідея для наповнення програми табору 📝", callback_data="choose:programofcamp")# кнопка вибрати реманент на табір
help_of_camp.insert(program_of_camp)
place_of_camp = InlineKeyboardButton(text="Місце для таборування 🏞 ", callback_data="choose:placeofcamp")# кнопка вибрати місцет на табір
help_of_camp.insert(place_of_camp)
virus_of_camp = InlineKeyboardButton(text="Коронавірусна безпека 🤒😷", url="https://docs.google.com/document/d/1pConT82uO2Wm"
                                                                       "Hhb5pEZOefU6MokA05VzMCAJedME2SE/edit")# кнопка вибрати реманент на табір
help_of_camp.insert(virus_of_camp)
aptechaka = InlineKeyboardButton(text="Таборова аптечка 💊 ", callback_data="choose:placeofcamp")# кнопка вибрати реманент на табір
help_of_camp.insert(aptechaka)
#список допомоги на табір

program_ideas_of_camp = InlineKeyboardMarkup(row_width=1)
share_ideas = InlineKeyboardButton(text="Поділитись ідеями",
                                      callback_data="choose:shareideas")# кнопка щоб поділитись ідеями
program_ideas_of_camp.insert(share_ideas)
plast_banka = InlineKeyboardButton(text="Пластова банка",
                                      url="https://plastovabanka.org.ua/")# кнопка на інк на пластову банку
program_ideas_of_camp.insert(plast_banka)
#список по ідеях програми


# допомога по обранню місць