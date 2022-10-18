from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

trip_upy_child = InlineKeyboardMarkup(row_width=1)
Claim_camp = InlineKeyboardButton(text="Вимоги для проведення мандрівок 💬📌",
                                  url="https://docs.google.com/document/d/1aWO3KCOHHNxtux_QmoO45UEElBCNNnWkj-rvpGIejWM/edit?usp=sharing")#кнопка вимоги для проведення мандрівко
trip_upy_child.insert(Claim_camp)
reporting_camp = InlineKeyboardButton(text="Зголошення мандрівок 🆘📢",
                                      url="https://docs.google.com/forms/d/182bUcztEdKguDflh2zAq4QwDErhANmcBnY-kqurTNB4/edit")#кнопка зголосити мандрівку
trip_upy_child.insert(reporting_camp)

book_camp = InlineKeyboardButton(text="Ідеї для маршрутів мандрівок 📍",
                                      url="https://plastovabanka.org.ua/mandrivky/")#кнопка на лінк на мандріви
trip_upy_child.insert(book_camp)

# кнопки обрання по мандрівках інформації

