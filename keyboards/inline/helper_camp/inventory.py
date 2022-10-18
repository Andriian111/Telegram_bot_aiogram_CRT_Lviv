from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.helper_camp.place_camp import reurn_to_list_of_help

inventory_of_camp = InlineKeyboardMarkup(row_width=2)
tent_camp = InlineKeyboardButton(text="Наметовий табір ⛺️",
                                      url="https://docs.google.com/document/d/1cY5df6_bnx6e7kefcFvS67e7"
                                                    "vYIkevW_uqbcQPObqP4/edit")# кнопка вибрати наметовийтабір
inventory_of_camp.insert(tent_camp)
statinary_camp =  InlineKeyboardButton(text="Стаціонарний табір 🏠",
                                      url="https://docs.google.com/document/d/1cY5df6_bnx6e7kefcFvS67e7vYIkevW_"
                                          "uqbcQPObqP4/edit")# кнопка вибрати стаціонарний табіртабір
inventory_of_camp.insert(statinary_camp)
inventory_of_camp.insert(reurn_to_list_of_help)


