from aiogram.types import Message

from loader import dp


@dp.message_handler(commands=['help']) #команда, щоб відкрити вікно допомоги
async def unknown_message(msg: Message):
    await msg.reply('/start - розпочати/перезапустити додаток ☑️ \n'
                    '\n/aboutus - інформація про ЦРТ 🆘 \n'
                    '\n/contacts - контакти 📞\n'
                    '\n/help - отримати список команд 💡')